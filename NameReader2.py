###
### Outputs a list of pokemon names to CSV [type, name]
###

import json

from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype

def setCardType(type):
    if (type == "Darkness"):
        return "Psychic"
    elif (type == "Dragon"):
        return "Water"
    elif (type == "Fairy"):
        return "Colorless"
    elif (type == "Metal"):
        return "Fighting"
    else:
        return type

cards = Card.where(supertype='pokemon')
f = open("names.txt", "a", encoding="utf-8")
for card in cards:
    type = setCardType(card.types[0])
    f.write(str(type) + ", ")
    f.write(str(card.name))
    f.write("\n")
f.close()
