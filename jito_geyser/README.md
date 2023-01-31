# About
This library contains python code to interact with [Jito's Geyser Plugin](https://github.com/jito-foundation/geyser-grpc-plugin).

# Downloading
```bash
$ pip install jito_geyser
```

# Access Token
Please request access to geyser by emailing support@jito.wtf

# Examples

### Printing slot updates
```python
from grpc import ssl_channel_credentials, secure_channel

from jito_geyser.generated.geyser_pb2 import SubscribeSlotUpdateRequest
from jito_geyser.generated.geyser_pb2_grpc import GeyserStub

GEYSER_URL = "mainnet.rpc.jito.wtf"
ACCESS_TOKEN = "ACCESS_TOKEN_HERE"

channel = secure_channel(GEYSER_URL, ssl_channel_credentials())
client = GeyserStub(channel)
for msg in client.SubscribeSlotUpdates(SubscribeSlotUpdateRequest(), metadata=[("access-token", ACCESS_TOKEN)]):
    print(msg)
```

### Listening to program account updates
This example listens to pyth-owned accounts
```python
from grpc import ssl_channel_credentials, secure_channel
from solders.pubkey import Pubkey # note: probably need to install solders for this import

from jito_geyser.generated.geyser_pb2 import SubscribeProgramsUpdatesRequest
from jito_geyser.generated.geyser_pb2_grpc import GeyserStub

GEYSER_URL = "mainnet.rpc.jito.wtf"
ACCESS_TOKEN = "ACCESS_TOKEN_HERE"
ACCOUNTS = [bytes(Pubkey.from_string("FsJ3A3u2vn5cTVofAjvy6y5kwABJAqYWpe4975bi2epH"))]

channel = secure_channel(GEYSER_URL, ssl_channel_credentials())
client = GeyserStub(channel)
for msg in client.SubscribeProgramUpdates(SubscribeProgramsUpdatesRequest(programs=ACCOUNTS), metadata=[("access-token", ACCESS_TOKEN)]):
    print(msg)
```

### Functions available
- There are many functions available including:
  - GetHeartbeatInterval
  - SubscribeAccountUpdates
  - SubscribeProgramUpdates
  - SubscribePartialAccountUpdates
  - SubscribeSlotUpdates
  - SubscribeTransactionUpdates
  - SubscribeBlockUpdates

# Development

Install pip
```bash
$ curl -sSL https://bootstrap.pypa.io/get-pip.py | python 3 -
```

Install poetry
```bash
$ curl -sSL https://install.python-poetry.org | python3 -
```

Setup environment and build protobufs
```bash
$ poetry install
$ poetry shell
$ poetry protoc
```

Linting
```bash
$ poetry run black .
$ poetry run isort .
```

Publishing package
```bash
$ poetry protoc && poetry build && poetry publish
```
