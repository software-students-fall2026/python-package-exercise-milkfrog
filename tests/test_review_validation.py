import pytest

from fridgelin import review


@pytest.mark.parametrize("stars", [0, 6])
def test_stars_outside_range(stars):
    with pytest.raises(ValueError, match="Stars"):
        review("Rice", stars)


@pytest.mark.parametrize("stars", [True, False, 1.0, "1", None])
def test_stars_must_be_integer(stars):
    with pytest.raises(TypeError, match="Stars"):
        review("Rice", stars)


@pytest.mark.parametrize("field", ["dish", "critic"])
@pytest.mark.parametrize("value", ["", "  "])
def test_empty_text(field, value):
    arguments = {"dish": "Rice", "stars": 3, "critic": "Ada Spoon"}
    arguments[field] = value
    with pytest.raises(ValueError, match=field.capitalize()):
        review(**arguments)


@pytest.mark.parametrize("field", ["dish", "critic"])
@pytest.mark.parametrize("value", [123, None])
def test_text_must_be_string(field, value):
    arguments = {"dish": "Rice", "stars": 3, "critic": "Ada Spoon"}
    arguments[field] = value
    with pytest.raises(TypeError, match=field.capitalize()):
        review(**arguments)


@pytest.mark.parametrize("seed", ["7", True, False, 1.5])
def test_invalid_seed_type(seed):
    with pytest.raises(TypeError, match="Seed"):
        review("Rice", 3, seed=seed)
