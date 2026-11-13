from fridgelin.helpers import clean
from fridgelin.helpers import whole
from fridgelin.helpers import rng



SOLO={
    1: 
    (
        "Just {head}",
        "{head}, Plain",
        "A Bowl of {head}",

        "Some {head}",
        "{head}, Nothing Else",
        "Leftover {head}"
    ),


    2:
    (
        "Classic {head}",
        "Mom's {head}",
        "Home-Style {head}",
        "Rustic {head}",
        "{head}, Made with Care"
    ),


    3: 
    (
        "Pan-Seared {head}, {head} Jus",
        "Slow-Roasted {head}",
        "Charred {head}, Herb Oil",
        "{head} Two Ways",
        "Braised {head}, Pan Juices"
    ),

    4: 
    (
        "Barely Cooked {head}, Brown Butter",
        "{head} Cuit Sous Vide, Pomme Fondante",
        "Crudo of {head}, Olive Oil and Sea Salt",

        "Salt-Baked {head}, Black Truffle",
        "Dry-Aged {head}, Sauce Bordelaise"
    ),
    5: 
    (
        "{head}, Three Ways, All of Them Cold",
        "Hot {head}, Cold {head}",
        "{head}, Reimagined",
        "{head} in Textures",
        "An Ode to {head}",
        "Variations of {head}"
    )

}



MULTI={
    1: 
    (
        "{head} with {rest}",
        "{head} and {rest}",
        "Plate of {head} with {rest}",
        "Bowl of {head} and {rest}",
        "Leftover {head} with {rest}",
        "{head}, {rest}",
        "{head} Next to {rest}",
        "Some {head} and Some {rest}",
        "{head} with a Side of {rest}"
    ),
    2: 
    (
        "Rustic {head} with {rest}",
        "Grandma's {head} with {rest}",
        "{head} Glazed with {rest}",
        "Homemade {head} with {rest}",
        "{head} Tossed with {rest}",
        "Weeknight {head} with {rest}",
        "{head} Skillet with {rest}",
        "{head} with {rest}, Family Style",
        "Simple {head} over {rest}"
    ),
    3: 
    (
        "Pan-Seared {head}, {rest} Reduction",
        "Slow-Roasted {head} in {rest} Jus",
        "Charred {head}, {rest} Butter",
        "Braised {head} with {rest}",
        "{head} Confit, {rest} Crumble",
        "Seared {head} over Warm {rest}",
        "Roasted {head}, {rest} Salsa",
        "{head} with {rest} Glaze",
        "Smoked {head}, {rest} Drizzle"
    ),
    4: 
    (
        "Barely Cooked {head}, {rest} Beurre Blanc",
        "Butter-Poached {head} with {rest} Sabayon",
        "Tartare of {head} with {rest}, Toasted Brioche",
        "Salad of {head} with {rest} Vinaigrette", 

        "{head} Cuit Sous Vide, Pomme Fondante, {rest} Jus",
        "Dry-Aged {head}, {rest}, Sauce Bordelaise",
        "Coal-Roasted {head}, {rest}, Black Truffle",
        
        "Glazed {head} with {rest} Gastrique",
        "{head} Ragout with {rest} Foam"
    ),


    5: 
    (
        "Deconstructed {rest}, Three Ways, on a Bed of {head}",
        "{head} in Textures, {rest} Snow",
        "Hot {head}, Cold {rest}",
        "Variations of {head}, {rest} Consomme",
        "{head} Almost Raw, {rest} Barely Touched",
        "An Ode to {head}, Interrupted by {rest}",
        "{head} Under a Cloche of {rest} Smoke",
        "Garden of {head} with {rest} Soil",
        "{head} and Pearls, {rest} Sabayon"
    )

}





def glue(rest):

    if len(rest)==1:
        return rest[0]

    return ", ".join(rest[:-1]) +" and "+ rest[-1]



def name(food,level=3,seed=None):

    food=clean(food)
    whole("Level",level,1,5)

    r=rng(seed)
    
    head=food[0]

    if len(food)==1:

        pick=r.choice(SOLO[level])

        return pick.format(head=head)

    pick=r.choice(MULTI[level])
    return pick.format(head=head, rest=glue(food[1:]))
