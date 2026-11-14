"""Verify the seeded public API against the real dish-name generator."""

from concurrent.futures import ThreadPoolExecutor
import random

import pytest

from fridgelin import menu, name


FOOD = ["rice", "egg", "lime"]


@pytest.mark.parametrize("seed", [-(2**80), -1, 0, 1, 2**80])
def test_each_seed_offset_is_applied_before_naming(seed):
    rows = menu(FOOD, 3, 3, 120, seed).splitlines()
    expected = [
        name(FOOD[:1], 3, seed + 1),
        name(FOOD[:2], 3, seed + 2),
        name(FOOD, 3, seed + 3),
    ]
    assert [row.split(" ...", 1)[0] for row in rows[1:-1]] == expected


@pytest.mark.parametrize("level", [1, 3, 5])
def test_a_known_seed_can_be_replayed_after_unseeded_menus(level):
    before = random.getstate()
    first = menu(FOOD, level=level, seed=0)
    try:
        for _ in range(3):
            menu(["hot sauce", "bread"], level=5, courses=6)
        assert random.getstate() == before
        assert menu(FOOD, level=level, seed=0) == first
    finally:
        random.setstate(before)


def test_concurrent_seeded_requests_match_sequential_results():
    seeds = [0, 2, -5, 2, 0, 111, -5, 111]
    sequential = [menu(FOOD, 2, 3, 120, seed) for seed in seeds]

    def request(seed):
        return menu(FOOD, 2, 3, 120, seed)

    with ThreadPoolExecutor(max_workers=3) as pool:
        concurrent = list(pool.map(request, seeds))
    assert concurrent == sequential


def test_seed_changes_names_without_changing_money():
    menus = [menu(FOOD, level=4, courses=3, seed=seed).splitlines() for seed in range(12)]
    totals = {rows[-1] for rows in menus}
    amounts = {tuple(row.rsplit("$", 1)[1] for row in rows[1:-1]) for rows in menus}
    assert len(totals) == 1
    assert amounts == {("120.99", "176.99", "232.99")}
    assert len({rows[1] for rows in menus}) > 1
