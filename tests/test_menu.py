import pytest

from fridgelin import price
from fridgelin.menus import line


EIGHT = ["rice", "ketchup", "egg", "lime", "hot sauce", "butter", "cheese", "bread"]


def test_price():
    assert price(["rice"], 1) == 8.49
    assert price(["rice", "egg"], 3) == 99.99
    assert price(["rice", "egg", "lime"], 5) == 363.49
    assert price(EIGHT, 5) == 800.99


def test_price_goes_up():
    assert price(["rice"], 1) < price(["rice"], 2)
    assert price(["rice"], 2) < price(["rice"], 5)
    assert price(["rice"], 3) < price(["rice", "egg"], 3)
    assert price(["rice", "egg"], 3) < price(EIGHT, 3)


def test_price_bad():
    with pytest.raises(TypeError):
        price("rice")
    with pytest.raises(TypeError):
        price(["rice"], True)

    with pytest.raises(ValueError):
        price(["rice"], 0)
    with pytest.raises(ValueError):
        price(["rice"], 6)
    with pytest.raises(ValueError):
        price([], 3)


def test_line():
    row = line("Rice", 8.49, 40)
    assert len(row) == 40
    assert row.endswith(" $8.49")
    assert row.startswith("Rice ....")

    total_row = line("Total", 2618.44, 120)
    assert len(total_row) == 120
    assert total_row.endswith(" $2618.44")

    long_name = "A" * 50
    row = line(long_name, 1.0, 40)
    assert row.startswith(long_name)
    assert row.endswith(" $1.00")
    assert row == long_name + "  $1.00"
