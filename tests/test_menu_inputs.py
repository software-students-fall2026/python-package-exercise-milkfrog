import pytest

from fridgelin import menu, price


def test_price_normalizes_ingredients():
    messy = ["  RICE ", "eGG", " hot sauce  "]
    clean = ["rice", "egg", "hot sauce"]

    assert price(messy, 1) == price(clean, 1)
    assert price(messy, 3) == price(clean, 3)
    assert price(messy, 5) == price(clean, 5)


def test_menu_normalizes_ingredients():
    messy = ["  RICE ", "eGG", " hot sauce  "]
    clean = ["Rice", "Egg", "Hot Sauce"]

    first = menu(messy, level=2, courses=3, width=120, seed=7)
    second = menu(clean, level=2, courses=3, width=120, seed=7)
    assert first == second


def test_price_leaves_original_food_unchanged():
    food = ["  RICE ", "eGG", " hot sauce  "]
    before = food.copy()

    price(food, 4)

    assert food == before
    assert food[0] == "  RICE "
    assert food[1] == "eGG"


def test_menu_leaves_original_food_unchanged():
    food = ["  RICE ", "eGG", " hot sauce  "]
    before = food.copy()

    menu(food, level=3, courses=3, width=120, seed=9)
    assert food == before

    menu(food, level=1, courses=1, width=120)
    assert food == before


def test_too_many_ingredients():
    food = ["rice", "egg", "lime", "bread", "cheese", "butter", "peas", "tofu", "corn"]

    with pytest.raises(ValueError):
        price(food)
    with pytest.raises(ValueError):
        menu(food, seed=7)


def test_blank_ingredients():
    with pytest.raises(ValueError):
        price(["rice", "   "])
    with pytest.raises(ValueError):
        menu(["rice", "   "], seed=7)
    with pytest.raises(ValueError):
        price([""])
    with pytest.raises(ValueError):
        menu([""], seed=7)


def test_non_string_ingredients():
    with pytest.raises(TypeError):
        price(["rice", 3])
    with pytest.raises(TypeError):
        menu(["rice", 3], seed=7)
    with pytest.raises(TypeError):
        price([None])
    with pytest.raises(TypeError):
        menu([None], seed=7)
