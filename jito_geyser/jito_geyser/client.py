from grpc import ssl_channel_credentials, secure_channel

from jito_geyser.generated.geyser_pb2 import SubscribeSlotUpdateRequest
from jito_geyser.generated.geyser_pb2_grpc import GeyserStub


def get_geyser_client(url: str, access_token: str) -> GeyserStub:
    credentials = ssl_channel_credentials()
    channel = secure_channel(url, credentials)
    return GeyserStub(channel)


def main():
    client = get_geyser_client("frankfurt.mainnet.rpc.jito.wtf", "foo")
    for msg in client.SubscribeSlotUpdates(SubscribeSlotUpdateRequest()):
        print(msg)


if __name__ == "__main__":
    main()
