# Benjamin's Kata

# Python version
`.python-version` holds the recommended version of python that the repo was developed in.

It is recommended to us `pyenv` when developing on this repo.

# Development
It is recommended to use `pyenv` and `vitualenv` when setting up a development environment for this repo.

As such:
- [Install `pyenv`](https://github.com/pyenv/pyenv#installation)
- run `python -m venv .venv` to create your environment.
- run `source .venv/bin/activate` to activate your environment.
- install `pip-tools`: `pip install pip-compile`
- install the requirements as stated below

## Requirements
Install the development and non development requirements:
- `pip install -r dev-requirements.txt`
- `pip install -r requirements.txt`

`pip-tools` are being used to pin requirements: [See more](https://github.com/jazzband/pip-tools)

# Makefile
A Make file has been added to aid the development process:

Use `make help` see the list of commands:
