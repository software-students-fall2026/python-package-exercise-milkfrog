from fridgelin.helpers import clean
from fridgelin.helpers import rng



FANCY={
    "Rice": ("Ancient Grain Pilaf","Jasmine Pearls", "Heritage Rice"),
    "Bread": ("Rustic Sourdough", "Hand-Torn Country Loaf", "Artisan Loaf"),
    "Toast": ("Twice-Baked Brioche", "Charred Sourdough", "Golden Crisp Bread"),
    "Instant Noodles": ("Hand-Pulled Ramen", "Silk Noodles", "Hand-Cut Wheat Noodles"),
    "Pasta": ("Fresh Tagliatelle", "Bronze-Cut Pasta", "Hand-Rolled Pappardelle"),
    "Tortilla": ("Stone-Ground Masa","Heirloom Corn Tortilla", "Hand-Pressed Flatbread"),
    "Cereal": ("Toasted Grain Clusters", "Puffed Heritage Grains", "Morning Crunch"),
    "Crackers": ("Seeded Crisps", "Stone-Baked Wafers", "Rye Lavash"),
    "Potato": ("Fondant Potato", "Pommes Puree", "Heirloom Fingerling"),
    "Fries": ("Triple-Cooked Frites", "Duck Fat Chips","Pommes Allumettes"),
    "Pizza": ("Day-Old Neapolitan Flatbread", "Wood-Fired Galette", "Twice-Served Focaccia"),
    "Egg": ("Pasture-Raised Egg", "Golden Yolk", "Slow-Poached Egg"),
    "Chicken": ("Free-Range Poussin", "Heritage Hen", "Roasted Bird"),
    "Ham": ("Jambon Blanc", "Cured Heritage Pork", "Slow-Smoked Ham"),
    "Bacon": ("Cured Pork Belly", "Smoked Lardons", "Applewood Rashers"),
    "Hot Dog": ("Heritage Frankfurter", "Smoked Pork Sausage", "Stadium Charcuterie"),
    "Spam": ("Pressed Pork Terrine", "Canned Charcuterie", "Tinned Luncheon Meat"),
    "Tuna": ("Line-Caught Tuna", "Tuna Rillettes", "Canned Ocean Tuna"),
    "Tofu": ("Silken Bean Curd", "Hand-Pressed Tofu", "Soy Custard"),
    "Beans": ("Heirloom Legumes", "Slow-Cooked Cassoulet", "Braised Pulses"),
    "Peanut Butter": ("Stone-Ground Peanut Butter", "Roasted Groundnut Paste", "Peanut Praline"),
    "Cheese": ("Aged Fromage", "Cave-Ripened Cheese", "Artisan Curd"),
    "Butter": ("Cultured Butter", "Hand-Churned Butter", "Beurre Noisette"),
    "Milk": ("Grass-Fed Milk", "Farmstead Cream","Cold Whole Milk"),
    "Yogurt": ("Strained Labneh", "Cultured Cream","Greek-Style Curd"),
    "Cream Cheese": ("Whipped Fromage Frais","Fresh Cream Curd", "Soft Farmhouse Cheese"),
    "Ice Cream": ("Hand-Churned Gelato","Frozen Custard","Vanilla Bean Semifreddo"),
    "Ketchup": ("Heirloom Tomato Reduction","Tomato Gastrique", "Slow-Cooked Tomato Glaze"),
    "Mustard": ("Whole-Grain Dijon", "Mustard Seed Caviar", "Stone-Ground Mustard"),
    "Mayo": ("Hand-Whisked Aioli", "Whipped Egg Yolk", "House Mayo"),
    "Hot Sauce": ("Fermented Chili Sauce", "Smoked Pepper Sauce", "Chili Gastrique"),
    "Soy Sauce": ("Aged Tamari", "Fermented Soy Glaze", "Soy Reduction"),
    "Sriracha": ("Fermented Red Chili Paste", "Chili Garlic Sauce", "Smoked Chili Oil"),
    "Ranch": ("Buttermilk Herb Dressing", "Garden Herb Cream", "Cultured Dill Dressing"),
    "Salsa": ("Fire-Roasted Tomato Relish", "Salsa Fresca", "Charred Pepper Relish"),
    "Honey": ("Wildflower Honey", "Raw Comb Honey", "Local Honey"),
    "Jam": ("Fruit Preserve", "Seasonal Compote", "Small-Batch Confiture"),
    "Olive Oil": ("Cold-Pressed Olive Oil", "Extra Virgin Olive Oil", "Estate Olive Oil"),
    "Lime": ("Key Lime Zest", "Lime Wedge", "Charred Lime"),
    "Lemon": ("Meyer Lemon Zest", "Preserved Lemon","Squeezed Lemon"),
    "Onion": ("Caramelized Shallot","Sweet Onion Confit","Charred Allium"),
    "Garlic": ("Roasted Garlic Confit","Black Garlic","Garlic Chips"),
    "Tomato": ("Heirloom Tomato", "Vine-Ripened Tomato", "Tomato Concasse"),
    "Lettuce": ("Baby Gem Leaves","Microgreens", "Garden Leaves"),
    "Carrot": ("Heirloom Carrot","Rainbow Baby Carrots", "Roasted Root"),
    "Broccoli": ("Charred Broccolini","Long-Stem Broccoli", "Green Florets"),
    "Spinach": ("Baby Spinach Leaves", "Wilted Garden Greens", "Spinach Chiffonade"),
    "Mushroom": ("Wild Forest Mushrooms", "Foraged Chanterelles", "Cremini Duxelles"),
    "Frozen Peas": ("Garden Peas", "Sweet English Peas", "Pea Puree"),
    "Pickles": ("Lacto-Fermented Cucumbers", "House Pickles", "Brined Gherkins"),
    "Avocado": ("Avocado Mousse", "Smashed Avocado", "Avocado Crema"),
    "Banana": ("Caramelized Plantain", "Bruleed Banana", "Banana Puree"),
    "Apple": ("Orchard Apple","Honeycrisp Compote", "Apple Tarte Fine"),
    "Chips": ("Kettle-Cooked Crisps","Potato Wafers","Sea Salt Chips"),
    "Chocolate": ("Single-Origin Cacao","Dark Chocolate Ganache", "Cocoa Nibs"),
    "Soda": ("Flat Soda Reduction", "Sparkling Syrup", "Fizzy Sugar Water")
}



PREFIX=(
    "Artisanal",
    "Small-Batch",
    "Hand-Picked",
    "Farm-Fresh",
    "Heritage",
    "Locally Sourced",
    "Single-Origin",
    "Hand-Foraged",
    "Slow-Aged",
    "House-Made"
)





def swap(food, seed=None):

    food=clean(food)
    r=rng(seed)


    out=[]
    for item in food:

        if item in FANCY:
            out.append(r.choice(FANCY[item]))

        else:
            out.append(r.choice(PREFIX)+" "+item)


    return out
