"""Independent cent arithmetic for the ingredient pricing API."""

from decimal import Decimal

import pytest

from fridgelin import price


PANTRY = ["rice", "egg", "lime", "bread", "butter", "tofu", "bean", "corn"]


def expected_cents(count, level):
    """Price before the 99-cent surcharge is scaled by the square of the level."""
    return (400 + 350 * count) * level * level + 99


@pytest.mark.parametrize("level", range(1, 6))
@pytest.mark.parametrize("count", range(1, 9))
def test_every_supported_combination_has_the_expected_dollar_price(count, level):
    amount = price(PANTRY[:count], level)
    assert isinstance(amount, float)
    assert Decimal(str(amount)) * 100 == expected_cents(count, level)


@pytest.mark.parametrize("level", [1, 2, 3, 4, 5])
def test_one_more_ingredient_has_a_fixed_marginal_price(level):
    amounts = [
        Decimal(str(price(PANTRY[:count], level)))
        for count in range(1, len(PANTRY) + 1)
    ]
    changes = [right - left for left, right in zip(amounts, amounts[1:])]
    assert changes == [Decimal("3.50") * level**2] * 7


def test_surcharge_is_added_after_difficulty_scaling():
    base = Decimal(str(price(["egg"], level=1))) - Decimal("0.99")
    for level in range(2, 6):
        dollars = Decimal(str(price(["egg"], level=level)))
        assert dollars - Decimal("0.99") == base * level**2


def test_one_price_per_list_entry_including_duplicates():
    single = price(["Rice"], level=2)
    pair = price(["Rice", " rice "], level=2)
    distinct_pair = price(["Egg", "Lime"], level=2)
    assert single == 30.99
    assert pair == distinct_pair == 44.99


def test_price_is_invariant_under_reordering_and_spelling():
    named = ["saffron", "lime", "tortilla"]
    reordered = list(reversed(named))
    other_names = ["beans", "tomato", "curry leaf"]
    for level in (1, 3, 5):
        assert price(named, level) == price(reordered, level)
        assert price(named, level) == price(other_names, level)


def test_default_level_matches_explicit_level_three():
    assert price(PANTRY) == price(PANTRY, 3) == 288.99
