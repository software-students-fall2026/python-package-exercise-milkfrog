import pytest

from fridgelin.names import glue
from fridgelin.names import name


EIGHT=["rice","ketchup","egg","lime","hot sauce","butter","cheese","bread"]



def test_glue():
    assert glue(["Egg"])=="Egg"

    assert glue(["Egg", "Lime"])=="Egg and Lime"

    assert glue(["Egg","Lime","Bread"])=="Egg, Lime and Bread"



def test_same_seed():

    assert name(["rice", "egg"], 3, 7)==name(["rice", "egg"],3,7)

    assert name(["rice"], 5, 1)==name(["rice"],5,1)




def test_seed_matters():
    found=set()

    for s in range(10):
        found.add(name(["rice", "egg"],3,s))

    assert len(found)>1




def test_no_seed():
    out=name(["rice","egg"])

    assert "Rice" in out

    assert "Egg" in out




def test_all_in():

    for level in range(1, 6):
        out=name(["rice"],level,3)

        assert "Rice" in out



        out=name(["rice", "ketchup", "egg"],level,3)
        assert "Rice" in out
        assert "Ketchup" in out
        assert "Egg" in out

        out=name(EIGHT,level,3)

        for item in EIGHT:
            assert item.title() in out




def test_bad_food():

    with pytest.raises(TypeError):
        name("rice")

    with pytest.raises(ValueError):
        name([])

    with pytest.raises(ValueError):
        name([""])

    with pytest.raises(TypeError):
        name(["rice",3])




def test_bad_level():

    with pytest.raises(TypeError):
        name(["rice"],True)

    with pytest.raises(ValueError):
        name(["rice"],0)

    with pytest.raises(ValueError):
        name(["rice"],6)




def test_bad_seed():

    with pytest.raises(TypeError):
        name(["rice"],3,"7")

    with pytest.raises(TypeError):
        name(["rice"],3,1.5)
