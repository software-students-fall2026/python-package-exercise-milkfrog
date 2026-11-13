"""Exercise public error categories and precedence for invalid arguments."""

import pytest

from fridgelin import menu, price


class NumberLike:
    def __int__(self):
        return 3


class IntChild(int):
    pass


@pytest.mark.parametrize("operation", [price, menu])
@pytest.mark.parametrize("food", [None, "rice", ("rice",), {"rice"}, {"rice": 1}, 1])
def test_ingredient_container_requires_a_list(operation, food):
    with pytest.raises(TypeError, match="Ingredients must be a list"):
        operation(food)


@pytest.mark.parametrize("operation", [price, menu])
@pytest.mark.parametrize("food", [[], ["rice"] * 9])
def test_empty_and_oversized_pantries_fail_before_pricing(operation, food):
    with pytest.raises(ValueError, match="1 to 8"):
        operation(food)


@pytest.mark.parametrize("keyword", ["level", "courses", "width", "seed"])
@pytest.mark.parametrize("invalid", [True, False, 2.0, "2", IntChild(2), NumberLike()])
def test_integer_fields_use_strict_python_integer_types(keyword, invalid):
    with pytest.raises(TypeError, match=keyword.title()):
        menu(["rice"], **{keyword: invalid})


@pytest.mark.parametrize(("keyword", "invalid"), [
    ("level", 0), ("level", 6), ("courses", 0), ("courses", 7),
    ("width", 39), ("width", 121),
])
def test_integer_bounds_report_which_field_was_invalid(keyword, invalid):
    with pytest.raises(ValueError, match=keyword.title()):
        menu(["rice"], **{keyword: invalid})


@pytest.mark.parametrize(("args", "error", "message"), [
    (([], 0, 0, 30, True), ValueError, "Ingredients"),
    (([1], 0, 0, 30, True), TypeError, "Ingredient"),
    ((["rice"], 0, 0, 30, True), ValueError, "Level"),
    ((["rice"], 1, 0, 30, True), ValueError, "Courses"),
    ((["rice"], 1, 1, 30, True), ValueError, "Width"),
    ((["rice"], 1, 1, 40, True), TypeError, "Seed"),
])
def test_first_invalid_argument_matches_original_validation_order(args, error, message):
    with pytest.raises(error, match=message):
        menu(*args)


@pytest.mark.parametrize("operation", [price, menu])
def test_invalid_last_entry_leaves_the_original_list_untouched(operation):
    food = ["  Rice ", "eGG", "\t"]
    before = food.copy()
    with pytest.raises(ValueError, match="Ingredient"):
        operation(food)
    assert food == before


def test_failed_call_does_not_affect_the_next_valid_menu():
    args = dict(level=1, courses=1, width=40, seed=7)
    before = menu(["rice"], **args)
    with pytest.raises(TypeError):
        menu(["rice"], seed=7.0)
    assert menu(["rice"], **args) == before
