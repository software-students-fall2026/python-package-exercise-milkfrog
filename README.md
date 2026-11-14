![build and test](https://github.com/software-students-fall2026/python-package-exercise-milkfrog/actions/workflows/build.yaml/badge.svg)

# fridgelin

fridgelin is a package turns whatever is left in your fridge into a pretentious restaurant menu. Input the ingredients and it will name the dish, price it, write up a menu, and have a critic review it.

Plain Python, no dependencies, each function take a seed so the same seed always generate same nonsense

PyPI: https://pypi.org/project/fridgelin/

## Install

```bash
pip install fridgelin
```

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

If an ingredient has a space, put it in quotes. The review and the drink are both about the dish named on the first line.

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


## Use it in your own code

```python
from fridgelin import name, price, menu, review, drink, swap
```

Leave the seed out and you will get something random each time. 
`price` has no seed because nothing about it is random.

### name(food, level=3, seed=None)

Comes up with a name for the dish. `food` is a list of ingredients and `level` is how fancy you want it (1-5).

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


### price(food, level=3)

no randomness, `price = (4 + 3.5 * n) * level ** 2 + 0.99` rounded to cents (`n` is the number of ingredients).

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

Writes a tasting menu. Course 1 uses the first ingredient, course 2 uses the first two, and so on. The last course always uses all of them, so the prices keep going up until everything is on the plate. 

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

Writes a review of the dish: one sentence about the dish, one about the meal overall, and the critic's signature on its own line. `stars` sets the mood (1-5).

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


### drink(dish, budget="student", seed=None)

Picks a drink to go with the dish. `budget` is `student`, `date` or `investor`.

```python
drink("Ketchup-Glazed Rice", "date", seed=7)
```
```
'Pair Ketchup-Glazed Rice with sangria from a pitcher: fruit makes it a food group.'
```


### swap(food, seed=None)

Renames plain ingredients to what a fancy restaurant would call them.

```python
swap(["rice", "ketchup", "egg"], seed=7)
```
```
['Jasmine Pearls', 'Heirloom Tomato Reduction', 'Golden Yolk']
```
```python
swap(["rice", "mystery jar"], seed=7)
```
```
['Jasmine Pearls', 'Hand-Picked Mystery Jar']
```


### Valid input

- `food` is a list of 1 to 8 strings, no empty str. Spaces around each get trimmed and capitalized.
- `level`, `stars`, `courses` and `width` have to be whole numbers within range.
- `dish` and `critic` is nonempty str.
- `budget` has to be `student`, `date` or `investor`
- `seed` is whole number or `None`.

### Example program

[examples/example.py](https://github.com/software-students-fall2026/python-package-exercise-milkfrog/blob/main/examples/example.py) uses every function.

```bash
pipenv run python examples/example.py
```


## For contributors

Set up virtual environment and install dependencies:

```bash
git clone https://github.com/software-students-fall2026/python-package-exercise-milkfrog.git
cd python-package-exercise-milkfrog
python3 -m pip install pipenv
pipenv install --dev
```

On Windows, use `py -m pip install pipenv`.

Run the tests:

```bash
pipenv run python -m pytest
```

Build the package:

```bash
pipenv run python -m build
```


## Team

Team milkfrog:

- [Kevin Han](https://github.com/kevinhan923)
- [Tony Dong](https://github.com/tongdong016)
- [Spark Fan](https://github.com/SparkFan-ui)
- [Yutong Xiao](https://github.com/yx3295-star)

