# multi_poetry
Test out multiple poetry projects in one repo

## Notes

we can add non-subpath local dependencies to pyproject.toml, i.e.:

```
[tool.poetry.dependencies]
python = "^3.10"
toolbox = { path = "../toolbox/", develop = false }
cowsay = "^5.0"
```

This works for development but not when building. We can not add non-sub-path packages like:

```
[tool.poetry]
packages = [
    { include = "../toolbox" },
]
```

This will give an error when building the sdist.

## Solution Attempt

This has been tracked at: https://github.com/python-poetry/poetry-core/pull/273

That ticket has been closed since someone has made a poetry [plugin](https://pypi.org/project/poetry-multiproject-plugin/) to allow this:

### Setup

Install (globally to Poetry) via: `poetry self add poetry-multiproject-plugin`

See the docs there for more information.

To build:

`poetry build-project`

> Note that once you use packages, you must now also specify the default package:
> "Using packages disables the package auto-detection feature meaning you have to explicitly specify the “default” package."

### Remaining Questions

How to handle shared dependencies between top level module and toolbox. For example, currently they both need
to specify cowsay in the `pyproject.toml`

Is the `poetry check-project` we get with the multi-project plugin useful?
