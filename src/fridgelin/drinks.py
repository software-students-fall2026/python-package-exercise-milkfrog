from fridgelin.helpers import text, rng



DRINKS ={

    "student": (
        ("tap water with a lemon slice", "the lemon is doing all the work"),
        ("instant coffee, black", "it is technically a beverage"),
        ("half a can of flat soda", "found in the door of the fridge, lightly chilled"),
        ("the last of the orange juice", "shake the carton, that counts as mixing"),
        ("a glass of milk", "someone has to finish it before Friday"),
        ("ice water, extra ice", "it stretches the water"),
        ("free refill lemonade", "the second cup is the real pairing"),
        ("tea from a bag that was already used once", "the second steep is subtle"),
        ("a sports drink of an uncertain flavor", "blue is a flavor")
    ),

    "date": (
        ("the house red", "nobody will ask what it is"),
        ("a glass of the cheapest sparkling wine", "bubbles make everything look planned"),
        ("one cocktail with a name you can pronounce", "confidence is the real garnish"),
        ("a shared bottle of something white", "sharing is cheaper than two glasses"),
        ("a beer that comes in a tall glass", "the glass does the talking"),
        ("sangria from a pitcher", "fruit makes it a food group"),
        ("pink wine, because it is pink", "the color matches the candle"),
        ("a lemonade with a sprig of something", "the sprig is for the photo"),
        ("a small glass of port", "it says you have plans for dessert")
    ),

    "investor":(
        ("a 1998 Bordeaux you cannot pronounce", "the tannins will distract from everything else"),
        ("a single-malt whisky with a name longer than the menu", "the name alone is a conversation"),
        ("a vintage champagne from a year nobody remembers", "the bubbles are smaller, which costs more"),
        ("a dessert wine aged longer than the sommelier", "patience is the main ingredient"),
        ("a sake served in a cup smaller than a thimble", "the cup is the point"),
        ("a 2005 Burgundy opened an hour early", "it needs time, like most investments"),
        ("a tequila poured by someone wearing gloves", "the gloves add a zero to the price"),
        ("a cognac older than the building", "it has seen things"),
        ("mineral water imported from a glacier", "the glacier is very exclusive")
    )


}







def drink(dish, budget = "student", seed  = None):

    dish = text("Dish", dish)


    if type(budget) != str:
        raise TypeError("Budget must be a string")
    if budget not in DRINKS:
        raise ValueError("Budget must be one of student, date or investor")


    r = rng(seed)
    pick =r.choice(DRINKS[budget])


    return "Pair " + dish + " with " + pick[0] + ": " + pick[1] + "."




