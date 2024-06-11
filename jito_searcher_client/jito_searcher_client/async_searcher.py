import time
import os
from typing import List, Optional, Tuple

from grpc import ssl_channel_credentials
from grpc.aio import (
    ClientCallDetails,
    UnaryStreamClientInterceptor,
    UnaryUnaryClientInterceptor,
    secure_channel,
    insecure_channel,
)
from solders.keypair import Keypair

from jito_searcher_client.generated.auth_pb2 import (
    GenerateAuthChallengeRequest,
    GenerateAuthTokensRequest,
    GenerateAuthTokensResponse,
    RefreshAccessTokenRequest,
    RefreshAccessTokenResponse,
    Role,
)
from jito_searcher_client.generated.auth_pb2_grpc import AuthServiceStub
from jito_searcher_client.generated.searcher_pb2_grpc import SearcherServiceStub
from jito_searcher_client.token import JwtToken


class AsyncSearcherInterceptor(
    UnaryUnaryClientInterceptor,
    UnaryStreamClientInterceptor,
):
    """
    AsyncSearcherInterceptor is responsible for authenticating with the block engine.
    Authentication happens in a challenge-response handshake.
    1. Request a challenge and provide your public key.
    2. Get challenge and sign a message "{pubkey}-{challenge}".
    3. Get back a refresh token and access token.

    When the access token expires, use the refresh token to get a new one.
    When the refresh token expires, perform the challenge-response handshake again.
    """

    def __init__(self, url: str, kp: Keypair):
        """

        :param url: url of the Block Engine without http or https.
        :param kp: block engine authentication keypair
        """
        self._url = url
        self._kp = kp

        self._access_token: Optional[JwtToken] = None
        self._refresh_token: Optional[JwtToken] = None
        self.no_auth = os.getenv('NO_AUTH', 'false').lower() == 'true'

    async def intercept_unary_stream(
        self,
        continuation,
        client_call_details,
        request,
    ):
        if not self.no_auth:
            await self.authenticate_if_needed()
            client_call_details = self._insert_headers(
                [("authorization", f"Bearer {self._access_token.token}")],
                client_call_details,
            )
        call = await continuation(client_call_details, request)
        return call

    async def intercept_unary_unary(
        self,
        continuation,
        client_call_details,
        request,
    ):
        if not self.no_auth:
            await self.authenticate_if_needed()
            client_call_details = self._insert_headers(
                [("authorization", f"Bearer {self._access_token.token}")],
                client_call_details,
            )
        undone_call = await continuation(client_call_details, request)
        response = await undone_call
        return response

    @staticmethod
    def _insert_headers(new_metadata: List[Tuple[str, str]], client_call_details) -> ClientCallDetails:
        metadata = []
        if client_call_details.metadata is not None:
            metadata = list(client_call_details.metadata)
        metadata.extend(new_metadata)

        return ClientCallDetails(
            client_call_details.method,
            client_call_details.timeout,
            metadata,
            client_call_details.credentials,
            False,
        )

    async def authenticate_if_needed(self):
        """
        Maybe authenticates depending on state of access + refresh tokens
        """
        if self.no_auth:
            return
        now = int(time.time())
        if self._access_token is None or self._refresh_token is None or now >= self._refresh_token.expiration:
            await self.full_authentication()
        elif now >= self._access_token.expiration:
            await self.refresh_authentication()

    async def refresh_authentication(self):
        """
        Performs an authentication refresh with the block engine, which involves using the refresh token to get a new
        access token.
        """
        credentials = ssl_channel_credentials()
        channel = secure_channel(self._url, credentials)
        auth_client = AuthServiceStub(channel)

        new_access_token: RefreshAccessTokenResponse = await auth_client.RefreshAccessToken(
            RefreshAccessTokenRequest(refresh_token=self._refresh_token.token)
        )
        self._access_token = JwtToken(
            token=new_access_token.access_token.value, expiration=new_access_token.access_token.expires_at_utc.seconds
        )

    async def full_authentication(self):
        """
        Performs full authentication with the block engine
        """
        credentials = ssl_channel_credentials()
        channel = secure_channel(self._url, credentials)
        auth_client = AuthServiceStub(channel)

        challenge = (
            await auth_client.GenerateAuthChallenge(
                GenerateAuthChallengeRequest(role=Role.SEARCHER, pubkey=bytes(self._kp.pubkey()))
            )
        ).challenge

        challenge_to_sign = f"{str(self._kp.pubkey())}-{challenge}"

        signed = self._kp.sign_message(bytes(challenge_to_sign, "utf8"))

        auth_tokens_response: GenerateAuthTokensResponse = await auth_client.GenerateAuthTokens(
            GenerateAuthTokensRequest(
                challenge=challenge_to_sign,
                client_pubkey=bytes(self._kp.pubkey()),
                signed_challenge=bytes(signed),
            )
        )

        self._access_token = JwtToken(
            token=auth_tokens_response.access_token.value,
            expiration=auth_tokens_response.access_token.expires_at_utc.seconds,
        )

        self._refresh_token = JwtToken(
            token=auth_tokens_response.refresh_token.value,
            expiration=auth_tokens_response.refresh_token.expires_at_utc.seconds,
        )


async def get_async_searcher_client(url: str, kp: Keypair) -> SearcherServiceStub:
    """
    Returns a Searcher Service client that intercepts requests and authenticates with the block engine.
    :param url: url of the block engine without http/https
    :param kp: keypair of the block engine
    :return: SearcherServiceStub which handles authentication on requests
    """
    no_auth = os.getenv('NO_AUTH', 'false').lower() == 'true'
    searcher_interceptor = AsyncSearcherInterceptor(url, kp) if not no_auth else None

    if no_auth:
        channel = insecure_channel(url)
    else:
        credentials = ssl_channel_credentials()
        channel = secure_channel(url, credentials, interceptors=[searcher_interceptor])
        if searcher_interceptor:
            channel._unary_stream_interceptors.append(searcher_interceptor)

    return SearcherServiceStub(channel)
