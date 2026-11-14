import random

from fridgelin import menu, name


def test_seeded_menu_preserves_global_random_state():
    original_state = random.getstate()
    try:
        random.seed(31)
        before = random.getstate()

        menu(["rice", "egg"], level=3, courses=3, seed=7)

        assert random.getstate() == before
    finally:
        random.setstate(original_state)


def test_unseeded_menu_preserves_global_random_state():
    original_state = random.getstate()
    try:
        random.seed(19)
        before = random.getstate()

        menu(["rice", "egg"], courses=2)

        assert random.getstate() == before
    finally:
        random.setstate(original_state)


def test_seeded_menu_ignores_unrelated_random_calls():
    food = ["rice", "egg", "lime"]
    original_state = random.getstate()
    try:
        first = menu(food, level=4, courses=3, width=120, seed=11)

        random.seed(2026)
        for _ in range(20):
            random.random()
        menu(["bread", "butter"], seed=99)

        second = menu(food, level=4, courses=3, width=120, seed=11)
        assert second == first
    finally:
        random.setstate(original_state)


def test_course_names_use_incrementing_seeds():
    food = ["rice", "egg", "lime", "cheese"]
    seed = 20
    rows = menu(food, level=3, courses=3, width=120, seed=seed).splitlines()

    first_dish = name(food[:1], 3, seed + 1)
    second_dish = name(food[:2], 3, seed + 2)
    last_dish = name(food, 3, seed + 3)

    assert rows[1].startswith(first_dish + " ")
    assert rows[2].startswith(second_dish + " ")
    assert rows[3].startswith(last_dish + " ")
    assert rows[-1].startswith("Total ")


def test_seed_changes_do_not_change_prices():
    food = ["rice", "egg", "lime"]
    first = menu(food, level=4, courses=3, width=120, seed=0).splitlines()
    second = menu(food, level=4, courses=3, width=120, seed=-7).splitlines()

    assert len(first) == len(second) == 5
    for index in range(1, len(first)):
        first_price = first[index].rsplit("$", 1)[1]
        second_price = second[index].rsplit("$", 1)[1]
        assert first_price == second_price
