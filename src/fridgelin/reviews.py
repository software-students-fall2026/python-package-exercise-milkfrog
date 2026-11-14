from fridgelin.helpers import whole, text, rng
from fridgelin.review_templates import FIRST, MORE


def review(dish, stars, critic="Percival Crumb", seed=None):
    dish = text("Dish", dish)
    whole("Stars", stars, 1, 5)
    critic = text("Critic", critic)

    randomizer = rng(seed)
    opening = randomizer.choice(FIRST[stars]).format(dish=dish)
    follow_up = randomizer.choice(MORE[stars])

    return f"{opening} {follow_up}\n-- {critic}, {stars}/5"
