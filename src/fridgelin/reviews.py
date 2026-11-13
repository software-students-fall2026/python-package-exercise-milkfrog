from fridgelin.helpers import whole, text, rng


FIRST = {
    1: (
        "{dish} arrived with the confidence of a dish that had never been tasted.",
        "{dish} is less a meal than a rumor of one.",
        "I have had worse than {dish}, but I had to think about it.",
        "{dish} answered a question nobody at the table had asked.",
        "Somewhere, a chef is very proud of {dish}, and that is the saddest part.",
        "{dish} was served warm, which is the nicest thing I can say about it."
    ),
    2: (
        "{dish} is fine, in the way a waiting room is fine.",
        "{dish} showed up, did its job, and left without making eye contact.",
        "There is a good dish hiding inside {dish}, and it would like to be rescued.",
        "{dish} tastes like a reasonable decision made in a hurry.",
        "{dish} did not offend me, which is not the same as pleasing me."
    ),
    3: (
        "{dish} was food.",
        "I ate {dish} and I am still here.",
        "{dish} did exactly what it said it would do, no more, no less.",
        "{dish} is a dish, served on a plate, at a temperature.",
        "I can confirm that {dish} exists and that I consumed it.",
        "{dish} was placed in front of me and later it was gone."
    ),
    4: (
        "{dish} is better than it has any right to be.",
        "Somebody in that kitchen cares about {dish}, and it shows.",
        "{dish} made me put my phone down, which is the highest honor I give.",
        "I did not expect to think about {dish} on the way home, and yet.",
        "{dish} is the kind of plate you quietly order twice."
    ),
    5: (
        "{dish} changed the way I think about dinner.",
        "I would cross a city on foot for {dish}.",
        "{dish} is the reason forks were invented.",
        "If {dish} were a person I would write it letters.",
        "{dish} made the table go silent, then loud, then silent again.",
        "There is dinner, and then there is {dish}."
    )
}


MORE = {
    1: (
        "The kitchen, we assume, was also surprised.",
        "We sent it back, and it returned unchanged, like a grudge.",
        "The plate was clean, which I now believe was a warning.",
        "Our table went quiet in a way that was not respect.",
        "The garnish looked like it wanted to leave.",
        "I asked for the bill and the bill was the best course.",
        "Between the first bite and the second, hope left the building."
    ),
    2: (
        "The seasoning arrived about ten minutes after the food.",
        "It was hot, mostly, in places.",
        "I would order it again if the other options were closed.",
        "The sauce had opinions but kept them to itself.",
        "A second bite confirmed the first, which is something.",
        "The portion was generous, which felt like an apology."
    ),
    3: (
        "The bread was bread.",
        "I finished it, which proves nothing.",
        "It had a flavor, and the flavor was consistent.",
        "The fork worked.",
        "Nothing happened, and I mean that neutrally.",
        "The plate was round.",
        "I would describe the experience as an experience."
    ),
    4: (
        "The sauce knew when to stop, which is rarer than it sounds.",
        "Every bite tasted like the first one, on purpose.",
        "My dining companion stopped talking, which never happens.",
        "The portion was right, and the price was wrong in the good direction.",
        "I considered licking the plate and I considered it seriously.",
        "Only a stubborn crust kept it from a perfect score."
    ),
    5: (
        "The first bite was a sentence and the second was a paragraph.",
        "I have not stopped thinking about it and I do not plan to.",
        "The kitchen should be studied by scientists.",
        "I asked for the recipe and was politely refused, as I deserved.",
        "Everyone at the table ordered another one and nobody shared.",
        "My only complaint is that it ended.",
        "Pay whatever they ask."
    )
}


def review(dish, stars, critic="Percival Crumb", seed=None):
    dish = text("Dish", dish)
    whole("Stars", stars, 1, 5)
    critic = text("Critic", critic)

    randomizer = rng(seed)
    opening = randomizer.choice(FIRST[stars]).format(dish=dish)
    follow_up = randomizer.choice(MORE[stars])

    return f"{opening} {follow_up}\n-- {critic}, {stars}/5"
