import pytest

from fridgelin.helpers import clean
from fridgelin.helpers import whole
from fridgelin.helpers import text
from fridgelin.helpers import rng



def test_clean():

    assert clean([" rice ", "hot sauce", "half-lime"])==["Rice", "Hot Sauce", "Half-Lime"]
    assert clean(["egg"])==["Egg"]
    assert clean(["RICE", "egg"])==["Rice", "Egg"]

    assert len(clean(["a", "b", "c", "d", "e", "f", "g", "h"]))==8


def test_clean_not_list():
    with pytest.raises(TypeError):
        clean("rice")
    with pytest.raises(TypeError):
        clean(("rice", "egg"))
    with pytest.raises(TypeError):
        clean(["rice", 3])


def test_clean_count():

    with pytest.raises(ValueError):
        clean([])

    with pytest.raises(ValueError):
        clean(["a","b","c","d","e","f","g","h","i"])



def test_clean_empty_item():

    with pytest.raises(ValueError):
        clean([""])

    with pytest.raises(ValueError):
        clean(["   "])

    with pytest.raises(ValueError):
        clean(["rice", ""])





def test_whole():
    whole("x",1,1,5)


    whole("x",5,1,5)
    whole("x",-2,-3,3)




def test_whole_type():

    with pytest.raises(TypeError):

        whole("x", True, 1, 5)


    with pytest.raises(TypeError):
        whole("x", "3", 1, 5)


    with pytest.raises(TypeError):
        whole("x", 3.0, 1, 5)


def test_whole_range():

    with pytest.raises(ValueError):
        whole("x", 0, 1, 5)

    with pytest.raises(ValueError):
        whole("x", 6, 1, 5)




def test_text():
    assert text("dish","  Rice  ")=="Rice"

    assert text("dish","Rice")=="Rice"

    with pytest.raises(TypeError):
        text("dish",5)

    with pytest.raises(ValueError):
        text("dish","   ")



def test_rng():
    assert rng(7).random()==rng(7).random()
    assert rng(1).random()!=rng(2).random()
    assert rng(0).random()<1
    assert rng(None).random()<1



def test_rng_bad_seed():

    with pytest.raises(TypeError):
        rng("7")

    with pytest.raises(TypeError):
        rng(True)
        
    with pytest.raises(TypeError):
        rng(1.5)
