# Python Dependency Management

Since `pyenv` only manages different Python versions, it doesn't manage their dependencies at the same time. So as long as we're only using one version of Python, it provides no benefits.

For now, we're just using the Homebrew version of `python` (which seems to install `python` and `python3`?). And then installing `pip` dependencies with `pip install --usr`. This at least provides some separation between user installed dependencies.
