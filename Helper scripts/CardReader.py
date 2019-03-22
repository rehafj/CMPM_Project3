###
### Takes a list of cards and outputs their images to a local direectory
### naming the card the same as the pokemon's card ID
###

import requests
import shutil

from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype

cards = Card.where(supertype='pokemon')
for card in cards:
    card_url = card.image_url
    card_name = card.id + ".png"
    r = requests.get(card_url, stream=True)
    if r.status_code == 200:
        with open(card_name, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
