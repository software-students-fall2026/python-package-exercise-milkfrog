"""Trace the existing menu-to-naming contract without changing dish pricing."""

import pytest

from fridgelin import menus


def trace_names(monkeypatch):
    calls = []

    def label(parts, level, *seed):
        calls.append((tuple(parts), level, seed))
        return f"Course {len(calls)}"

    monkeypatch.setattr(menus, "name", label)
    return calls


@pytest.mark.parametrize(("courses", "portions"), [
    (1, [("Rice", "Egg", "Lime")]),
    (2, [("Rice",), ("Rice", "Egg", "Lime")]),
    (3, [("Rice",), ("Rice", "Egg"), ("Rice", "Egg", "Lime")]),
    (4, [("Rice",), ("Rice", "Egg"), ("Rice", "Egg", "Lime"), ("Rice", "Egg", "Lime")]),
])
def test_last_course_uses_everything_and_earlier_courses_grow(monkeypatch, courses, portions):
    calls = trace_names(monkeypatch)
    dish = menus.menu([" rice ", "eGG", "lime"], level=2, courses=courses, seed=-2)
    assert calls == [
        (items, 2, (-2 + index,))
        for index, items in enumerate(portions, start=1)
    ]
    rows = dish.splitlines()
    for index in range(1, courses + 1):
        assert rows[index].startswith(f"Course {index} ")


def test_unseeded_menu_uses_the_naming_helpers_default_randomness(monkeypatch):
    calls = trace_names(monkeypatch)
    menus.menu(["rice"], level=4, courses=3)
    assert calls == [(("Rice",), 4, ())] * 3


def test_cleaning_keeps_repeated_ingredients_in_original_order(monkeypatch):
    calls = trace_names(monkeypatch)
    food = ["  bean ", "RICE", " Bean "]
    original = food.copy()
    menus.menu(food, level=1, courses=2, seed=0)
    assert food == original
    assert calls[0] == (("Bean",), 1, (1,))
    assert calls[1] == (("Bean", "Rice", "Bean"), 1, (2,))


def test_menu_completes_validation_before_naming_any_course(monkeypatch):
    calls = trace_names(monkeypatch)
    with pytest.raises(TypeError, match="Seed"):
        menus.menu(["rice"], courses=6, seed=True)
    with pytest.raises(ValueError, match="Width"):
        menus.menu(["rice"], courses=6, width=39)
    assert calls == []


def test_naming_failure_does_not_mutate_input_or_return_a_partial_menu(monkeypatch):
    calls = []

    def reject_second_course(parts, level, seed):
        calls.append(list(parts))
        if len(calls) == 2:
            raise ValueError("missing course name")
        return "First course"

    monkeypatch.setattr(menus, "name", reject_second_course)
    food = [" rice", "EGG "]
    with pytest.raises(ValueError, match="missing course name"):
        menus.menu(food, courses=3, seed=4)
    assert calls == [["Rice"], ["Rice", "Egg"]]
    assert food == [" rice", "EGG "]
