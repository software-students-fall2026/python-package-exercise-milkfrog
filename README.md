![build and test](https://github.com/software-students-fall2026/python-package-exercise-milkfrog/actions/workflows/build.yaml/badge.svg)

# fridgelin

fridgelin turns whatever is left in your fridge into a pretentious tasting menu. Give it a few ingredients and it names the dish, prices it, writes the menu, reviews the dish and picks a drink. Everything is pure Python with no dependencies, and every function that uses randomness takes a `seed`, so the same seed always gives the same nonsense.

The package is on PyPI: https://pypi.org/project/fridgelin/

## Install

```bash
pip install fridgelin
```

Python 3.10 or newer. No API keys, no environment variables, no files on disk. On macOS and Linux the command may be `pip3` or `python3 -m pip`.

## Try it from the command line

```bash
fridgelin "instant noodles" lime "hot sauce" --seed 1111
```

```
Braised Instant Noodles with Lime and Hot Sauce

Tonight's Tasting Menu
Charred Instant Noodles, Herb Oil ............................... $68.49
Pan-Seared Instant Noodles, Lime Reduction ...................... $99.99
Smoked Instant Noodles, Lime and Hot Sauce Drizzle ............. $131.49
Total .......................................................... $299.97

I ate Braised Instant Noodles with Lime and Hot Sauce and I am still here. I finished it, which proves nothing.
-- Percival Crumb, 3/5

Pair Braised Instant Noodles with Lime and Hot Sauce with the last of the orange juice: shake the carton, that counts as mixing.
```

`python -m fridgelin ...` does the same thing. Ingredients with spaces go in quotes. The review and the drink are about the dish named at the top.

| Option | Default | What it does |
|---|---|---|
| `--level` | 3 | how fancy the names are, 1 to 5 |
| `--courses` | 3 | courses on the menu, 1 to 6 |
| `--width` | 72 | menu width in columns, 40 to 120 |
| `--stars` | 3 | stars for the review, 1 to 5 |
| `--critic` | `Percival Crumb` | who signs the review |
| `--budget` | `student` | `student`, `date` or `investor` |
| `--seed` | none | same seed, same output |
| `--only` | `all` | print just one part: `name`, `menu`, `review` or `drink` |

Bad input prints an error message and exits with code 2. Options for parts that are not printed are ignored, except `--level`, which the dish name always needs.

## Use it in your own code

```python
from fridgelin import name, price, menu, review, drink
```

Every example below that takes a `seed` uses `seed=7`, so you get exactly the same output. Leave the seed out and the output is random. `price` has no seed because it is not random.

### name(food, level=3, seed=None)

Names a dish. `food` is a list of ingredients and `level` goes from 1 (plain) to 5 (ridiculous). Every ingredient ends up in the name, in title case, with the first one as the star.

```python
name(["rice", "ketchup", "egg"], 1, seed=7)
```
```
'Rice, Ketchup and Egg'
```
```python
name(["rice", "ketchup", "egg"], 3, seed=7)
```
```
'Seared Rice over Warm Ketchup and Egg'
```
```python
name(["rice", "ketchup", "egg"], 5, seed=7)
```
```
'An Ode to Rice, Interrupted by Ketchup and Egg'
```
```python
name(["rice"], 5, seed=7)
```
```
'Rice, Reimagined'
```

### price(food, level=3)

Prices a dish. No randomness: `price = (4 + 3.5 * n) * level ** 2 + 0.99`, rounded to cents, where `n` is the number of ingredients.

```python
price(["rice", "ketchup", "egg"], 3)
```
```
131.49
```
```python
price(["rice", "ketchup", "egg"], 5)
```
```
363.49
```

### menu(food, level=3, courses=3, width=72, seed=None)

Writes a tasting menu. Course 1 uses the first ingredient, course 2 the first two, and so on, and the last course always uses everything, so the prices climb until every ingredient is on the plate. The dots pad each line out to `width` columns; a name too long for that is not cut, so the line just runs over.

```python
print(menu(["rice", "ketchup", "egg"], 3, 3, 60, seed=7))
```
```
Tonight's Tasting Menu
Slow-Roasted Rice ................................... $68.49
Rice with Ketchup Glaze ............................. $99.99
Pan-Seared Rice, Ketchup and Egg Reduction ......... $131.49
Total .............................................. $299.97
```

### review(dish, stars, critic="Percival Crumb", seed=None)

A review of the dish: one sentence about the dish, one more sentence about the meal, and a signature on its own line. `stars` picks the mood, from 1 (cruel) to 5 (in love).

```python
print(review("Ketchup-Glazed Rice", 3, seed=7))
```
```
Ketchup-Glazed Rice did exactly what it said it would do, no more, no less. I finished it, which proves nothing.
-- Percival Crumb, 3/5
```
```python
dish = name(["rice", "ketchup", "egg"], 5, seed=7)
print(review(dish, 1, seed=7))
```
```
I have had worse than An Ode to Rice, Interrupted by Ketchup and Egg, but I had to think about it. We sent it back, and it returned unchanged, like a grudge.
-- Percival Crumb, 1/5
```
```python
print(review(dish, 5, "Ada Spoon", seed=7))
```
```
An Ode to Rice, Interrupted by Ketchup and Egg is the reason forks were invented. I have not stopped thinking about it and I do not plan to.
-- Ada Spoon, 5/5
```

### drink(dish, budget="student", seed=None)

Picks a drink for the dish. `budget` is `student`, `date` or `investor`.

```python
drink("Ketchup-Glazed Rice", "date", seed=7)
```
```
'Pair Ketchup-Glazed Rice with sangria from a pitcher: fruit makes it a food group.'
```
```python
drink(dish, "investor", seed=7)
```
```
'Pair An Ode to Rice, Interrupted by Ketchup and Egg with a 2005 Burgundy opened an hour early: it needs time, like most investments.'
```

### What counts as valid input

- `food` is a list of 1 to 8 non-empty strings. Spaces around each one are trimmed and the words are title-cased, so `"hot sauce"` becomes `Hot Sauce`.
- `level`, `stars`, `courses` and `width` must be whole numbers in their range. `True` and `False` are rejected.
- `dish` and `critic` must be non-empty strings. Spaces around them are trimmed.
- `budget` must be exactly `student`, `date` or `investor`, in lowercase.
- `seed` is a whole number or `None`.

Wrong types raise `TypeError` and wrong values raise `ValueError`, with a message that says which argument is wrong.

### Example program

[examples/example.py](https://github.com/software-students-fall2026/python-package-exercise-milkfrog/blob/main/examples/example.py) calls every function and prints the results. After the contributor setup below, run it with:

```bash
pipenv run python examples/example.py
```

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

The tests in `tests/` cover every public function with valid and invalid input, and `tests/test_cli.py` runs the command line in a subprocess.

### Build the package

```bash
pipenv run python -m build
pipenv run twine check dist/*
```

This writes the source archive and the wheel into `dist/`.

### Publish a version

1. Bump `version` in `pyproject.toml`. PyPI never accepts the same version twice.
2. Merge to `main`.
3. Delete the old `dist` folder, build and upload with twine. Twine asks for a PyPI API token from your account (older twine versions ask for a username first: type `__token__`). The token never goes into the repository.

```bash
pipenv run python -m build
pipenv run twine check dist/*
pipenv run twine upload dist/*
```

### Continuous integration

Every push and pull request to `main` builds the package and runs the tests on Python 3.12 and 3.14. See [.github/workflows/build.yaml](https://github.com/software-students-fall2026/python-package-exercise-milkfrog/blob/main/.github/workflows/build.yaml). GitHub turns workflows off in a forked repository until someone opens the Actions tab and enables them once.

### How we work

All changes go through a feature branch and a pull request against this repository's `main`, reviewed and merged by another team member.

## Team

Team milkfrog:

- [Kevin Han](https://github.com/kevinhan923)
- [Tony Dong](https://github.com/tongdong016)
- [Spark Fan](https://github.com/SparkFan-ui)
- [Yutong Xiao](https://github.com/yx3295-star)

## License

GPL-3.0-or-later. See [LICENSE](https://github.com/software-students-fall2026/python-package-exercise-milkfrog/blob/main/LICENSE).
