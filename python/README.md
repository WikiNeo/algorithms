# Algorithms Python

## Setup

```shell
uv init
uv add --dev pre-commit
pre-commit install
# Auto-update pre-commit config to the latest repos' versions.
pre-commit autoupdate
pre-commit run --all-files
```

## Development

```shell
source .venv/bin/activate
uv sync
```

## Test

```shell
./test.sh
```

## Reference

- [https://github.com/keon/algorithms](https://github.com/keon/algorithms)
