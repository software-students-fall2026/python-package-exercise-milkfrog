import pytest

from fridgelin import name
from fridgelin import swap

from fridgelin.swaps import FANCY

from fridgelin.swaps import PREFIX



def test_known():

    for s in range(10):
        out=swap(["ketchup"],s)
        assert len(out)==1
        assert out[0] in FANCY["Ketchup"]


    assert swap(["hot sauce"],7)[0] in FANCY["Hot Sauce"]




def test_unknown():

    for s in range(10):
        out=swap(["mystery jar"],s)[0]

        assert out.endswith(" Mystery Jar")
        assert out.replace(" Mystery Jar","") in PREFIX



def test_order():
    out=swap(["rice","mystery jar","egg"],7)

    assert len(out)==3
    assert out[0] in FANCY["Rice"]
    assert out[1].endswith(" Mystery Jar")
    assert out[2] in FANCY["Egg"]




def test_messy_input():

    assert swap(["  KETCHUP "],7)[0] in FANCY["Ketchup"]
    assert swap(["Hot sauce"],7)[0] in FANCY["Hot Sauce"]

    assert swap(["egg"],7)==swap([" Egg "],7)



def test_same_seed():

    assert swap(["rice","egg"],7)==swap(["rice","egg"],7)

    assert swap(["mystery jar"],1)==swap(["mystery jar"],1)




def test_seed_matters():
    found=set()

    for s in range(10):
        found.add(tuple(swap(["rice", "egg"],s)))
    assert len(found)>1




def test_no_seed():
    out=swap(["rice","egg"])

    assert len(out)==2
    assert out[0] in FANCY["Rice"]
    assert out[1] in FANCY["Egg"]



def test_food_untouched():

    food=["rice","egg"]

    swap(food,7)

    assert food==["rice","egg"]




def test_with_name():

    for level in range(1, 6):
        fancy=swap(["rice","ketchup","egg"],level)
        out=name(fancy,level,7)

        for item in fancy:
            assert item in out




def test_table():

    for key in FANCY:
        assert key==key.title()
        assert len(FANCY[key])>=2

        for word in FANCY[key]:
            assert word==word.title()


    for word in PREFIX:
        assert word==word.title()




def test_bad_food():

    with pytest.raises(TypeError):
        swap("rice")

    with pytest.raises(TypeError):
        swap(["rice",3])
    with pytest.raises(ValueError):
        swap([])
    with pytest.raises(ValueError):
        swap(["rice",""])

    with pytest.raises(ValueError):
        swap(["a","b","c","d","e","f","g","h","i"])




def test_bad_seed():
    with pytest.raises(TypeError):
        swap(["rice"],"7")
    with pytest.raises(TypeError):
        swap(["rice"],1.5)
    with pytest.raises(TypeError):
        swap(["rice"],True)
