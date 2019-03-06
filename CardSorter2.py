import os
import glob
import shutil

from PIL import Image
from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype

for filename in glob.glob('cards/*.png'):
    name_ext = filename.split("\\")[1]
    # print(name_ext)
    name = name_ext.split(".")[0]
    name_dir = "./cards/" + name_ext
    card = Card.find(name)
    print(name_dir)
    card_type = card.types[0]
    if (card_type == "Colorless"):
        shutil.move(name_dir, "./cards/Colorless/" + name_ext)
    elif (card_type == "Darkness"):
        shutil.move(name_dir, "./cards/Darkness/" + name_ext)
    elif (card_type == "Dragon"):
        shutil.move(name_dir, "./cards/Dragon/" + name_ext)
    elif (card_type == "Fairy"):
        shutil.move(name_dir, "./cards/Fairy/" + name_ext)
    elif (card_type == "Fighting"):
        shutil.move(name_dir, "./cards/Fighting/" + name_ext)
    elif (card_type == "Fire"):
        shutil.move(name_dir, "./cards/Fire/" + name_ext)
    elif (card_type == "Grass"):
        shutil.move(name_dir, "./cards/Grass/" + name_ext)
    elif (card_type == "Lightning"):
        shutil.move(name_dir, "./cards/Lightning/" + name_ext)
    elif (card_type == "Metal"):
        shutil.move(name_dir, "./cards/Metal/" + name_ext)
    elif (card_type == "Psychic"):
        shutil.move(name_dir, "./cards/Psychic/" + name_ext)
    else:
        shutil.move(name_dir, "./cards/Water/" + name_ext)
