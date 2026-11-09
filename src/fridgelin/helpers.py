import random



def text(name,value):

    if type(value)!=str:
        raise TypeError(name+" must be a string")

    value=value.strip()


    if value=="":
        raise ValueError(name+" cannot be empty")


    return value




def whole(name, value,lo,hi):

    if type(value)!=int:
        raise TypeError(name+" must be a whole number")

    if value<lo or value>hi:
        raise ValueError(name+" must be from "+ str(lo) +" to " +str(hi))



def clean(food):

    if type(food)!=list:
        raise TypeError("Ingredients must be a list")


    if len(food)<1 or len(food)>8:
        raise ValueError("Ingredients must be 1 to 8 items")


    out=[]
    for item in food:
        out.append(text("Ingredient", item).title())


    return out




def rng(seed):

    if seed is not None and type(seed)!=int:
        raise TypeError("Seed must be a whole number or None")

    return random.Random(seed)
