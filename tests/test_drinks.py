import pytest
from fridgelin import drink
from fridgelin.drinks import DRINKS




def test_shape():

    out =drink("Ketchup-Glazed Rice", "student", 7)

    assert out.startswith("Pair Ketchup-Glazed Rice with ")
    assert out.endswith(".")
    assert not out.endswith("..")
    assert ": "  in out




def test_right_table():
    for budget in ["student", "date", "investor"]:
        for s in range(6):
            out = drink("Rice", budget, s)
            hit = False
            for what, why in DRINKS[budget]:
                if what in out and why in out:
                    hit = True
            assert hit




def test_seed():
    assert drink("Rice", "investor", 7)==drink("Rice", "investor", 7)

    found=set()
    for s in range(10):
        found.add(drink("Rice", "date", s))
    assert len(found)>1



def test_default():
    assert drink("Rice", seed=2)==drink("Rice", "student", 2)




def test_bad_budget():
    with pytest.raises(ValueError):
        drink("Rice", "rich")
    with pytest.raises(ValueError):
        drink("Rice", "Student")
    with pytest.raises(ValueError):
        drink("Rice", "")
    with pytest.raises(TypeError):
        drink("Rice", 3)



def test_bad_dish():
    with pytest.raises(ValueError):
        drink("")
    with pytest.raises(TypeError):
        drink(None)
    with pytest.raises(ValueError):
        drink("   ")



def test_bad_seed():
    with pytest.raises(TypeError):
        drink("Rice", "student", 1.5)



