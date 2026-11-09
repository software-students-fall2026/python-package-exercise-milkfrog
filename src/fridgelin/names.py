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
        "Honest {head}",
        "{head}, Lightly Considered",
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
        "Charred {head}, Finished Tableside",
        "{head}, Pressed and Rested",
        "Slow-Cooked {head} with Its Own Essence",
        "A Plate of {head}, Carefully Arranged",
        "{head} with Smoked Air"
    ),


    5: 
    (
        "{head}, Three Ways, All of Them Cold",
        "A Meditation on {head}",
        "{head}, Reimagined",
        "The Essence of {head}",
        "An Ode to {head}",
        "{head}, Interrupted"
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
        "Honest {head} with {rest}",
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
        "Charred {head} over a Silken {rest} Emulsion, Finished Tableside",
        "Sous-Vide {head} with a Velvet {rest} Foam",
        "{head}, Pressed, with {rest} Soil",
        "{head} with {rest} Gel and Torched Edges",
        "Roasted {head}, {rest} Dust, Micro Herbs",
        "{head} Rested on Warm {rest}, Finished with Smoke",
        "Aged {head} Under a Veil of {rest}",
        "Hand-Cut {head} over {rest} Puree, Plated Warm",
        "Slow {head}, Quick {rest}"
    ),


    5: 
    (
        "Deconstructed {rest}, Three Ways, on a Bed of {head}",
        "A Study of {head} and {rest}",
        "{head}, Reimagined, with a Whisper of {rest}",
        "Textures of {head}, Memory of {rest}",
        "{head} in Conversation with {rest}",
        "An Ode to {head}, Interrupted by {rest}",
        "The Idea of {head}, Served with {rest} Air",
        "{head}, Forgotten and Found, over {rest} Snow",
        "A Quiet Argument Between {head} and {rest}"
    )

}





def glue(rest):

    if len(rest)==1:
        return rest[0]

    return ", ".join(rest[:-1]) +" and "+ rest[-1]



def name(food, level=3, seed=None):

    food=clean(food)
    whole("Level",level,1,5)

    r =rng(seed)
    
    head=food[0]

    if len(food)==1:
        pick=r.choice(SOLO[level])
        return pick.format(head=head)

    pick=r.choice(MULTI[level])

    return pick.format(head=head, rest=glue(food[1:]))
