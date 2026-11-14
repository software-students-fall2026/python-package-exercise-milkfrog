# Development and release procedure

[Back to the project overview](../README.md) · [Usage and API reference](usage.md)

> Integration status: this documentation is based on the team skeleton at
> `69666f8a59c55ec8520c7c466913237a578c359e` and Spark's review contribution.
> The review implementation is included in this sequence. The complete menu,
> drink, CLI, two-version CI and official PyPI release still require team
> integration and verification. Intended outputs below are not release evidence.

## For contributors

### Set up

```bash
git clone https://github.com/software-students-fall2026/python-package-exercise-milkfrog.git
cd python-package-exercise-milkfrog
python3 -m pip install pipenv
pipenv install --dev
```

On Windows use `python -m pip install pipenv` for the third line; the rest is the same. If `pipenv` is not found afterwards, use `python3 -m pipenv` (or `python -m pipenv`) instead of `pipenv`. If pip refuses with `externally-managed-environment`, install pipenv with `pipx install pipenv` instead (or `brew install pipenv` on macOS).

`pipenv install --dev` creates the virtual environment, installs the package in editable mode and installs the development tools (`pytest`, `coverage`, `pytest-cov`, `build`, `twine`). There is no `.env` file and nothing to configure.

### Run the tests

```bash
pipenv run python -m pytest
```

The review tests cover valid and invalid input. Run the current review tests
with `pipenv run python -m pytest tests -k review`. The team still needs to
confirm coverage for every other public function and add CLI tests; the checked
baseline does not contain `tests/test_cli.py`.

### Build the package

```bash
pipenv run python -m build
pipenv run twine check dist/*
```

This writes the source archive and the wheel into `dist/`.

### Publish a version after integration

The following steps are a release procedure, not a record of a completed
upload. First finish every public function, its tests and the example program.

1. Bump `version` in `pyproject.toml`. PyPI never accepts the same version twice.
2. Merge to `main`.
3. Delete the old `dist` folder, build and upload with twine. Twine asks for a PyPI API token from your account (older twine versions ask for a username first: type `__token__`). The token never goes into the repository.

```bash
pipenv run python -m build
pipenv run twine check dist/*
pipenv run twine upload dist/*
```

### Continuous integration

Planned workflow: `.github/workflows/build.yaml` should build and test the
package on Python 3.12 and 3.14 for every pull request to `main`; push runs are
also planned. This file is absent from the checked baseline. Enable Actions
for the fork if necessary, then verify both version jobs before merging.

After the workflow exists, add its live status badge at the top of this README:

```markdown
![build and test](https://github.com/software-students-fall2026/python-package-exercise-milkfrog/actions/workflows/build.yaml/badge.svg)
```

A successful `log github events` run is not a successful build/test run.

### How we work

All changes go through a feature branch and a pull request against this repository's `main`, reviewed and merged by another team member.
