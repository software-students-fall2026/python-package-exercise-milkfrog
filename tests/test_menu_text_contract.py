"""Check the public text contract from header through the final total."""

import pytest

from fridgelin import menu, name


@pytest.mark.parametrize("width", [40, 60, 72, 120])
def test_changing_width_only_changes_dot_leaders(width):
    food = ["rice", "egg"]
    rows = menu(food, level=2, courses=2, width=width, seed=7).split("\n")
    first = name(["rice"], 2, 8)
    second = name(food, 2, 9)
    expected = [(first, "$30.99"), (second, "$44.99"), ("Total", "$75.98")]
    assert rows[0] == "Tonight's Tasting Menu"
    assert len(rows[1:]) == len(expected)
    for row, (label, dollars) in zip(rows[1:], expected):
        dots = max(0, width - len(label) - len(dollars) - 2)
        assert row == f"{label} {'.' * dots} {dollars}"


def test_default_format_has_a_single_header_and_no_blank_lines():
    text = menu(["rice"], seed=3)
    assert text.count("Tonight's Tasting Menu") == 1
    assert text.count("\n") == 4
    assert not text.startswith("\n")
    assert not text.endswith("\n")
    assert all(row.strip() for row in text.split("\n"))


@pytest.mark.parametrize("food", [["rice"], ["rice", "eggs"], ["hot sauce", "lime", "豆腐"]])
def test_wide_menu_has_one_total_after_all_dishes(food):
    rows = menu(food, level=1, courses=6, width=120, seed=2).splitlines()
    assert len(rows) == 8
    assert all(not row.startswith("Total ") for row in rows[1:-1])
    assert rows[-1].startswith("Total ")
    assert all(len(row) == 120 for row in rows[1:])


def test_long_name_overflows_without_hiding_the_price_or_total():
    ingredient = "longingredient" * 8
    dish = name([ingredient], 2, 5)
    rows = menu([ingredient], level=2, courses=1, width=40, seed=4).splitlines()
    assert len(dish) > 40
    assert rows[1] == dish + "  $30.99"
    assert len(rows[-1]) == 40
    assert rows[-1].endswith("$30.99")


def test_normalized_unicode_stays_in_the_dish():
    food = ["  豆腐 ", " CAfé "]
    rows = menu(food, level=1, courses=1, width=72, seed=4).splitlines()
    assert "豆腐" in rows[1]
    assert "Café" in rows[1]
    assert rows[1].endswith(" $11.99")
