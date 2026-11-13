"""Lock down how the original text formatter measures and joins a row."""

import pytest

from fridgelin.menus import line


@pytest.mark.parametrize("width", [40, 41, 71, 72, 119, 120])
@pytest.mark.parametrize(("dish", "amount", "tag"), [
    ("Rice", 0, "$0.00"),
    ("Bean broth", 8.49, "$8.49"),
    ("Total", 2618.44, "$2618.44"),
    ("Two  spaces", 0.5, "$0.50"),
])
def test_padding_depends_on_price_length_as_well_as_dish_length(width, dish, amount, tag):
    row = line(dish, amount, width)
    left = len(dish) + 1
    right = width - len(tag) - 1
    assert len(row) == width
    assert row[:left] == dish + " "
    assert row[left:right] == "." * (right - left)
    assert row[right:] == " " + tag


@pytest.mark.parametrize(("dish_length", "dots"), [(32, 1), (33, 0), (34, 0), (80, 0)])
def test_exact_fit_and_overflow_keep_both_separators(dish_length, dots):
    dish = "r" * dish_length
    assert line(dish, 8.49, 40) == dish + " " + "." * dots + " $8.49"


@pytest.mark.parametrize(("dish", "length"), [
    ("豆腐", 2),
    ("Café", 4),
    ("Cafe\u0301", 5),
    ("Riz 🍚", 5),
])
def test_original_width_uses_python_string_length(dish, length):
    dots = 40 - length - len("$1.00") - 2
    row = line(dish, 1, 40)
    assert row == dish + " " + "." * dots + " $1.00"
    assert len(row) == 40


@pytest.mark.parametrize("dish", ["A.B.", "50% off", "a $9 dish", "{pepper}", "rice\tbean"])
def test_punctuation_and_embedded_spaces_are_literal(dish):
    row = line(dish, 9.0, 40)
    assert row[:len(dish)] == dish
    assert row.endswith(" $9.00")
    assert len(row) == 40
