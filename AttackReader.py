# Calls the Pokemon TCG API to create a CSV list of each attack and its type
# for later use to train a text classifier

import json

from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype

# Reduces the number of card types for better training
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

# writes the attacks to file
def writeCard(card, card_type):
    for attack in card.attacks:
        # f.write(card_type + ",\"")
        if "cost" in attack:
            f.write(json.dumps(attack["cost"]).replace('\"', '\'') + ',')
        if "name" in attack:
            f.write(json.dumps(attack["name"]).replace('\"', '') +  ',')
        if "text" in attack:
            f.write(json.dumps(attack["text"]).replace('\"', '\'') +  ',')
        if "damage" in attack:
            f.write(json.dumps(attack["damage"]).replace('\"', ''))
        f.write("\"\n")

# Calls the API for each card, sees if they have an attack, and if so call other functions
if __name__ == "__main__":
    cards = Card.where(supertype='pokemon') # for each card that is a pokemon
    f = open("attacks.txt", "a")
    for card in cards:
        card_type = card.types[0] # take only the primary type
        if card.attacks is not None: # Check to make sure card has attacks
            card_type = setCardType(card_type)
            writeCard(card, card_type)
    f.close()
