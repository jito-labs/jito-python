from dataclasses import dataclass


@dataclass
class JwtToken:
    # jwt token string
    token: str
    # time in seconds since epoch when the token expires
    expiration: int
