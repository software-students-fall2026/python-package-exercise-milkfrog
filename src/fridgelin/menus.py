from fridgelin.helpers import clean, whole


def price(food, level=3):
    food = clean(food)
    whole("Level", level, 1, 5)

    ingredient_count = len(food)
    base_price = 4 + 3.5 * ingredient_count
    level_multiplier = level**2
    scaled_price = base_price * level_multiplier
    final_price = round(scaled_price + 0.99, 2)

    return final_price


def menu(food,level=3,courses=3,width=72, seed=None):
    raise NotImplementedError("not yet")
