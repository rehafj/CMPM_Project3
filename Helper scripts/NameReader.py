###
### Outputs a list of pokemon names to file
###

import json

from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype

cards = Card.where(supertype='pokemon')
f = open("names.txt", "a", encoding="utf-8")
for card in cards:
    f.write(str(card.name))
    f.write("\n")
f.close()
