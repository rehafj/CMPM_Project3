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
    name_dir = "./" + name_ext
    card = Card.find(name)
    print(name_dir)
    card_type = card.types[0]
    if (card_type == "Colorless"):
        shutil.move(name_dir, "./Colorless/" + name_ext)
    elif (card_type == "Darkness"):
        shutil.move(name_dir, "./Darkness/" + name_ext)
    elif (card_type == "Dragon"):
        shutil.move(name_dir, "./Dragon/" + name_ext)
    elif (card_type == "Fairy"):
        shutil.move(name_dir, "./Fairy/" + name_ext)
    elif (card_type == "Fighting"):
        shutil.move(name_dir, "./Fighting/" + name_ext)
    elif (card_type == "Fire"):
        shutil.move(name_dir, "./Fire/" + name_ext)
    elif (card_type == "Grass"):
        shutil.move(name_dir, "./Grass/" + name_ext)
    elif (card_type == "Lightning"):
        shutil.move(name_dir, "./Lightning/" + name_ext)
    elif (card_type == "Metal"):
        shutil.move(name_dir, "./Metal/" + name_ext)
    elif (card_type == "Psychic"):
        shutil.move(name_dir, "./Psychic/" + name_ext)
    else:
        shutil.move(name_dir, "./Water/" + name_ext)
