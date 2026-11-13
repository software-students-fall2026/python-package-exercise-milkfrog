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


def line(dish, cost, width):
    tag = "$%.2f" % cost
    dot_count = width - len(dish) - len(tag) - 2

    # A long dish name stays intact, even if there is no room for dots.
    dots = "." * dot_count
    row = dish + " " + dots + " " + tag
    return row


def menu(food,level=3,courses=3,width=72, seed=None):
    raise NotImplementedError("not yet")
