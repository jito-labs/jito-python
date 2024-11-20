# About
This library contains tooling to interact with Jito Lab's Block Engine as a searcher.

# Downloading
```bash
$ pip install jito_searcher_client
```

# Keypair Authentication
Basic access(5 req/second per region) no longer requires approval. Please visit our [Discord](https://discord.gg/jito) dev channel, if you have other questions.
If your application requires higher rate limits, please complete this [form](https://forms.gle/8jZmKX1KZA71jXp38)

# Examples

## Sync Client

```python
from jito_searcher_client import get_searcher_client
from jito_searcher_client.generated.searcher_pb2 import ConnectedLeadersRequest

from solders.keypair import Keypair

KEYPAIR_PATH = "/path/to/authenticated/keypair.json"
BLOCK_ENGINE_URL = "frankfurt.mainnet.block-engine.jito.wtf"

with open(KEYPAIR_PATH) as kp_path:
    kp = Keypair.from_json(kp_path.read())

client = get_searcher_client(BLOCK_ENGINE_URL, kp)
# This call is not needed since jito-sol is on the majority of validators
# It is useful if jito-sol is on less than 50% of the validators
leaders = client.GetConnectedLeaders(ConnectedLeadersRequest())
print(f"{leaders=}")
```

## Async Client

```python
import asyncio

from jito_searcher_client import get_async_searcher_client
from jito_searcher_client.generated.searcher_pb2 import ConnectedLeadersRequest

from solders.keypair import Keypair

KEYPAIR_PATH = "/path/to/authenticated/keypair.json"
BLOCK_ENGINE_URL = "frankfurt.mainnet.block-engine.jito.wtf"

async def main():
    with open(KEYPAIR_PATH) as kp_path:
        kp = Keypair.from_json(kp_path.read())
    client = await get_async_searcher_client(BLOCK_ENGINE_URL, kp)
    # This call is not needed since jito-sol is on the majority of validators
    # It is useful if jito-sol is on less than 50% of the validators
    leaders = await client.GetConnectedLeaders(ConnectedLeadersRequest())
    print(f"{leaders=}")

asyncio.run(main())
```

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

Linting:
```bash
poetry run isort .
poetry run black .
```

Publishing package
```bash
$ poetry protoc && poetry build && poetry publish
```
