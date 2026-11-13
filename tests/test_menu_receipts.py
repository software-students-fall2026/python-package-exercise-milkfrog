"""Reconcile actual printed receipts without using the production price helper."""

from decimal import Decimal
import re

import pytest

from fridgelin import menu


FOOD = ["rice", "egg", "lime", "bread", "butter", "tofu", "bean", "corn"]
MONEY = re.compile(r" \$(\d+\.\d{2})$")


def receipt(food, level, courses, seed):
    header, *items, total = menu(food, level, courses, 120, seed).splitlines()
    assert header == "Tonight's Tasting Menu"
    assert total.startswith("Total ")
    assert len(items) == courses
    amounts = []
    for row in [*items, total]:
        match = MONEY.search(row)
        assert match is not None, row
        amounts.append(Decimal(match.group(1)))
    return amounts[:-1], amounts[-1]


@pytest.mark.parametrize("level", range(1, 6))
@pytest.mark.parametrize("courses", range(1, 7))
@pytest.mark.parametrize("count", range(1, 9))
def test_every_receipt_charges_the_planned_portions(count, courses, level):
    items, total = receipt(FOOD[:count], level, courses, seed=17)
    portions = [min(course, count) for course in range(1, courses)] + [count]
    expected = [
        (Decimal("4") + Decimal("3.50") * size) * level**2 + Decimal("0.99")
        for size in portions
    ]
    assert items == expected
    assert total == sum(expected)


@pytest.mark.parametrize("courses", range(1, 6))
def test_an_extra_course_changes_the_total_by_its_own_price(courses):
    old_items, old_total = receipt(FOOD, 2, courses, seed=0)
    new_items, new_total = receipt(FOOD, 2, courses + 1, seed=0)
    assert old_items[:-1] == new_items[:-2]
    assert old_items[-1] == new_items[-1]
    assert new_total - old_total == new_items[-2]


def test_receipt_reader_uses_trailing_price_for_a_dollar_in_a_name():
    items, total = receipt(["$5 rice", "egg"], 1, 2, seed=-1)
    assert items == [Decimal("8.49"), Decimal("11.99")]
    assert total == Decimal("20.48")


def test_a_small_pantry_can_supply_six_identically_priced_courses():
    items, total = receipt(["egg"], 5, 6, seed=3)
    assert items == [Decimal("188.49")] * 6
    assert total == Decimal("1130.94")


def test_maximum_receipt_prints_two_decimal_places_even_at_four_digits():
    items, total = receipt(FOOD, 5, 6, seed=0)
    assert items[-1] == Decimal("800.99")
    assert total == Decimal("2618.44")
    assert total.as_tuple().exponent == -2
