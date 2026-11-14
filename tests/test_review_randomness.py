import random

import pytest

from fridgelin import review


@pytest.mark.parametrize("seed", [0, -7, 7])
def test_seed_is_repeatable(seed):
    assert review("Rice", 5, seed=seed) == review("Rice", 5, seed=seed)


def test_seeds_can_produce_different_reviews():
    found = {review("Rice", 5, seed=seed) for seed in range(10)}
    assert len(found) > 1


@pytest.mark.parametrize("seed", [None, 7])
def test_review_preserves_global_random_state(seed):
    previous_state = random.getstate()
    review("Rice", 3, seed=seed)
    assert random.getstate() == previous_state
