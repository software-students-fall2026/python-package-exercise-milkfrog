import pytest

from fridgelin import review


def review_text(output):
    return output.split("\n", 1)[0]


@pytest.mark.parametrize("stars", range(1, 6))
def test_default_signature(stars):
    output = review("Ketchup-Glazed Rice", stars, seed=7)
    assert output.endswith(f"\n-- Percival Crumb, {stars}/5")


def test_custom_signature():
    output = review("Ketchup-Glazed Rice", 4, "Ada Spoon", 7)
    assert output.endswith("\n-- Ada Spoon, 4/5")


@pytest.mark.parametrize("stars", range(1, 6))
@pytest.mark.parametrize("seed", range(5))
def test_dish_first(stars, seed):
    opening = review_text(
        review("Ketchup-Glazed Rice", stars, seed=seed)
    ).split(". ")[0]
    assert "Ketchup-Glazed Rice" in opening


@pytest.mark.parametrize("stars", range(1, 6))
def test_two_sentences(stars):
    assert review_text(review("Rice", stars, seed=3)).count(". ") == 1


def test_dish_and_critic_are_trimmed():
    output = review("  Rice  ", 3, "  Ada Spoon  ", seed=1)
    assert output == review("Rice", 3, "Ada Spoon", seed=1)
    assert "  Rice" not in output
    assert "Rice" in output
    assert output.endswith("\n-- Ada Spoon, 3/5")
