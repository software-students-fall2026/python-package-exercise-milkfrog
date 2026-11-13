from fridgelin.helpers import clean, whole
from fridgelin.names import name


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


def menu(food, level=3, courses=3, width=72, seed=None):
    food = clean(food)
    whole("Level", level, 1, 5)
    whole("Courses", courses, 1, 6)
    whole("Width", width, 40, 120)

    # Keep this strict so True and False are not accepted as seeds.
    if seed is not None and type(seed) != int:
        raise TypeError("Seed must be a whole number or None")

    rows = ["Tonight's Tasting Menu"]
    total = 0

    for course in range(1, courses + 1):
        if course == courses:
            # The last course uses everything, not just the next ingredient.
            course_food = food
        else:
            course_food = food[:course]

        if seed is None:
            dish = name(course_food, level)
        else:
            course_seed = seed + course
            dish = name(course_food, level, course_seed)

        cost = price(course_food, level)
        total += cost

        row = line(dish, cost, width)
        rows.append(row)

    total_row = line("Total", total, width)
    rows.append(total_row)

    return "\n".join(rows)
