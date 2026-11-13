import pytest

from fridgelin import name, price, menu
from fridgelin.menus import line


EIGHT = ["rice", "ketchup", "egg", "lime", "hot sauce", "butter", "cheese", "bread"]


def cost(row):
    price_text = row.split("$")[-1]
    return float(price_text)


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


def test_menu_example():
    out = menu(["rice", "ketchup"], 2, 2, 40, 7)
    rows = out.splitlines()

    assert rows[0] == "Tonight's Tasting Menu"
    assert len(rows) == 4
    assert not out.endswith("\n")

    for row in rows[1:]:
        assert len(row) == 40

    assert rows[1].endswith(" $30.99")
    assert rows[2].endswith(" $44.99")
    assert rows[3].startswith("Total ")
    assert rows[3].endswith(" $75.98")


def test_menu_prices():
    food = ["rice", "ketchup", "egg"]
    out = menu(food, 4, 3, 60, 2)
    rows = out.splitlines()

    first_price = price(food[:1], 4)
    second_price = price(food[:2], 4)
    last_price = price(food, 4)
    assert cost(rows[1]) == first_price
    assert cost(rows[2]) == second_price
    assert cost(rows[3]) == last_price

    total = first_price + second_price + last_price
    assert rows[4].endswith(f"${total:.2f}")


def test_prices_never_drop():
    rows = menu(EIGHT, 3, 6, 72, 5).splitlines()
    previous_price = 0

    for row in rows[1:-1]:
        current_price = cost(row)
        assert current_price >= previous_price
        previous_price = current_price


def test_last_course():
    rows = menu(EIGHT, 2, 3, 72, 9).splitlines()
    last_dish = name(EIGHT, 2, 9 + 3)

    for item in EIGHT:
        assert item.title() in last_dish
    assert rows[3].startswith(last_dish)


def test_short_menu():
    out = menu(["rice", "egg", "lime"], 1, 3, 120, 4)
    assert "Rice" in out
    assert "Egg" in out
    assert "Lime" in out


def test_more_courses_than_food():
    rows = menu(["rice"], 3, 3, 72, 1).splitlines()
    assert len(rows) == 5
    assert cost(rows[1]) == cost(rows[2]) == cost(rows[3]) == 68.49
    assert rows[4].endswith("$205.47")


def test_same_seed():
    food = ["rice", "egg"]
    first_menu = menu(food, 3, 3, 72, 7)
    second_menu = menu(food, 3, 3, 72, 7)

    assert first_menu == second_menu


def test_no_seed():
    rows = menu(["rice"]).splitlines()
    assert len(rows) == 5

    for row in rows[1:]:
        assert len(row) == 72


def test_widths():
    rows = menu(["rice"], 1, 2, 40, 1).splitlines()
    for row in rows[1:]:
        assert len(row) == 40

    rows = menu(EIGHT, 5, 6, 120, 1).splitlines()
    for row in rows[1:]:
        assert len(row) == 120
    assert rows[-1].endswith("$2618.44")


def test_menu_bad():
    with pytest.raises(ValueError):
        menu([], 3)
    with pytest.raises(ValueError):
        menu(["rice"], 9)
    with pytest.raises(TypeError):
        menu(["rice"], "3")

    with pytest.raises(ValueError):
        menu(["rice"], 3, 0)
    with pytest.raises(ValueError):
        menu(["rice"], 3, 7)
    with pytest.raises(TypeError):
        menu(["rice"], 3, True)

    with pytest.raises(ValueError):
        menu(["rice"], 3, 3, 39)
    with pytest.raises(ValueError):
        menu(["rice"], 3, 3, 121)
    with pytest.raises(TypeError):
        menu(["rice"], 3, 3, 72, "7")


def test_one_course_uses_all_food():
    food = ["rice", "egg", "lime"]
    rows = menu(food, level=2, courses=1, width=120, seed=4).splitlines()
    expected_dish = name(food, 2, 5)
    expected_price = price(food, 2)

    assert len(rows) == 3
    assert rows[1].startswith(expected_dish)
    assert cost(rows[1]) == expected_price
    assert rows[2].startswith("Total ")
    assert cost(rows[2]) == expected_price


def test_boolean_seed():
    with pytest.raises(TypeError):
        menu(["rice"], seed=True)
    with pytest.raises(TypeError):
        menu(["rice"], seed=False)
