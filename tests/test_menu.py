import pytest

from fridgelin import price


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
