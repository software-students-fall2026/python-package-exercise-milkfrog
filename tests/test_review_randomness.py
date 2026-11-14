from fridgelin import review


def test_seed():
    assert review("Rice", 5, seed=7) == review("Rice", 5, seed=7)

    found = {review("Rice", 5, seed=seed) for seed in range(10)}
    assert len(found) > 1
