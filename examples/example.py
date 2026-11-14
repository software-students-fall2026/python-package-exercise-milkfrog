from fridgelin import name, price, menu, review, drink, swap


food=["rice", "ketchup", "egg"]



print("Dish names, from plain to pretentious")

for level in range(1, 6):
    print(" ", level, name(food, level, seed=7))

print()

print("Price at level 3:", price(food, 3))
print("Price at level 5:", price(food, 5))

print()

print(menu(food, 3, 3, 60, seed=7))
dish=name(food, 5, seed=7)

print()

print(review(dish, 1, seed=7))

print()

print(review(dish, 5, "Ada Spoon", seed=7))

print()

print(drink(dish, "student", seed=7))
print(drink(dish, "date", seed=7))
print(drink(dish, "investor", seed=7))

print()

fancy=swap(food, seed=7)
print("Fancy ingredients:", ", ".join(fancy))
print(name(fancy, 5, seed=7))


