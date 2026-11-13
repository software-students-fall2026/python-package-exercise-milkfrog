# fridgelin

fridgelin is a playful Python package that turns leftover ingredients into an
imaginary restaurant experience. The team is building dish names, prices,
menus, reviews and drink pairings. This contribution implements dish reviews.

> Integration status: this documentation is based on the team skeleton at
> `69666f8a59c55ec8520c7c466913237a578c359e` and Spark's review contribution.
> The review implementation is included in this sequence. The complete menu,
> drink, CLI, two-version CI and official PyPI release still require team
> integration and verification. Intended outputs below are not release evidence.

## Install from the team source

```bash
git clone https://github.com/software-students-fall2026/python-package-exercise-milkfrog.git
cd python-package-exercise-milkfrog
python3 -m pip install pipenv
pipenv install --dev
```

Use Python 3.10 or newer. On Windows, replace `python3` with `python` when
installing pipenv. If the `pipenv` command is not on your PATH, run
`python3 -m pipenv` (or `python -m pipenv`) instead. If your Python installation
reports `externally-managed-environment`, install pipenv with `pipx` or the
platform's package manager.

The committed Pipfile requests an editable installation of this package and
the development tools. No environment variables, API keys or database setup
are required by the review feature.

The intended public package page is [fridgelin on PyPI](https://pypi.org/project/fridgelin/).
Publication has not been verified for this contribution. Use the source setup
above until the team has published and tested the package.

## Review a dish

```python
from fridgelin import review

print(review("Ketchup-Glazed Rice", 3, seed=7))
```

```text
Ketchup-Glazed Rice did exactly what it said it would do, no more, no less. I finished it, which proves nothing.
-- Percival Crumb, 3/5
```

The public signature is `review(dish, stars, critic="Percival Crumb", seed=None)`.

| Argument | Accepted values | Effect |
|---|---|---|
| `dish` | A non-empty string | Appears in the opening sentence |
| `stars` | An integer from 1 through 5 | Selects a critical, neutral or positive mood |
| `critic` | A non-empty string | Names the reviewer in the signature |
| `seed` | An integer or `None` | Makes selection repeatable when an integer is supplied |

Strings are stripped at their ends. Boolean values are not accepted as
integers. Wrong types raise `TypeError`; empty strings and out-of-range stars
raise `ValueError`. Internal punctuation and newlines in strings are preserved,
so callers should supply single-line names if they want a two-line result.

```python
print(review("Rice", 5, critic="Ada Spoon", seed=7))
```

The same arguments and seed produce the same result. Omitting the seed allows
random selection. Each call uses its own random generator.

## Test this contribution

```bash
pipenv run python -m pytest tests -k review
```

These tests exercise ratings, output, repeated seeds, trimming and invalid
arguments. Run the complete test suite as well before a pull request is merged:

```bash
pipenv run python -m pytest
```

## Build and collaboration

The project declares its build configuration in `pyproject.toml`.

```bash
pipenv run python -m build
pipenv run twine check dist/*
```

A successful local build is separate from publishing on PyPI. Team CI still
needs a build-and-test workflow on two recent Python versions for every pull
request to `main`. The existing event logger does not perform those tests.

Make changes in a feature branch, open a pull request against this team's
`main`, and ask another team member to review and run the tests before merging.

## Team

Team milkfrog:

- [Kevin Han](https://github.com/kevinhan923)
- [Tony Dong](https://github.com/tongdong016)
- [Spark Fan](https://github.com/SparkFan-ui)
- [Yutong Xiao](https://github.com/yx3295-star)

## License

GPL-3.0-or-later. See [LICENSE](LICENSE).
