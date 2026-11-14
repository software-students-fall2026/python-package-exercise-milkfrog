import pytest

from fridgelin import review


def review_text(output):
    return output.split("\n", 1)[0]


def test_ending():
    output = review("Ketchup-Glazed Rice", 1, seed=7)
    assert output.endswith("\n-- Percival Crumb, 1/5")

    output = review("Ketchup-Glazed Rice", 4, "Ada Spoon", 7)
    assert output.endswith("\n-- Ada Spoon, 4/5")


def test_dish_first():
    for stars in range(1, 6):
        for seed in range(5):
            opening = review_text(
                review("Ketchup-Glazed Rice", stars, seed=seed)
            ).split(". ")[0]
            assert "Ketchup-Glazed Rice" in opening


def test_two_sentences():
    for stars in range(1, 6):
        assert review_text(review("Rice", stars, seed=3)).count(". ") == 1


def test_seed():
    assert review("Rice", 5, seed=7) == review("Rice", 5, seed=7)

    found = {review("Rice", 5, seed=seed) for seed in range(10)}
    assert len(found) > 1


def test_trim():
    output = review("  Rice  ", 3, seed=1)
    assert "  Rice" not in output
    assert "Rice" in output


def test_bad_stars():
    with pytest.raises(ValueError):
        review("Rice", 0)
    with pytest.raises(ValueError):
        review("Rice", 6)
    with pytest.raises(TypeError):
        review("Rice", True)
    with pytest.raises(TypeError):
        review("Rice", "1")


def test_bad_text():
    with pytest.raises(ValueError):
        review("", 3)
    with pytest.raises(TypeError):
        review(123, 3)
    with pytest.raises(ValueError):
        review("Rice", 3, "  ")


def test_bad_seed():
    with pytest.raises(TypeError):
        review("Rice", 3, seed="7")
