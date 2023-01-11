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

