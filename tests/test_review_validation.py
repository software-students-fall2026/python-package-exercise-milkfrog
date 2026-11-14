import pytest

from fridgelin import review


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
