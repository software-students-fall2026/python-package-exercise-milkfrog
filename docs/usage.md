# Usage and API reference

[Back to the project overview](../README.md)

> Integration status: this documentation is based on the team skeleton at
> `69666f8a59c55ec8520c7c466913237a578c359e` and Spark's review contribution.
> The review implementation is included in this sequence. The complete menu,
> drink, CLI, two-version CI and official PyPI release still require team
> integration and verification. Intended outputs below are not release evidence.

## Planned command-line interface

This section records the intended CLI behavior. The baseline CLI is a
placeholder; confirm the implementation and output after the team merges it.

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

## Public API and integration targets

The `review` examples were checked against the supplied review implementation.
The remaining examples are the team design from the original README and must
be rerun against the integrated package before being described as verified.

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

Integration pending: the baseline contains a placeholder for this function.

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

Integration pending: the baseline contains a placeholder for this function.

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

Integration pending: the baseline contains a placeholder for this function.

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
  Internal punctuation and newlines are preserved by the current review
  implementation; use single-line strings for a two-line review.
- `budget` must be exactly `student`, `date` or `investor`, in lowercase.
- `seed` is a whole number or `None`.

Wrong types raise `TypeError` and wrong values raise `ValueError`, with a message that says which argument is wrong.

### Example program

The team must add and verify `examples/example.py` calling every public
function before release. It is absent from the checked baseline. The intended
command after that file is implemented is:

```bash
pipenv run python examples/example.py
```
