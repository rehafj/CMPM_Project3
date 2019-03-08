import json

from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype

cards = Card.where(supertype='pokemon')
f = open("attacks.txt", "a")
for card in cards:
    card_type = card.types[0]
    #print(card.attacks)
    if card.attacks is not None:
        if (card_type == "Colorless"):
            for attack in card.attacks:
                f = open("attacks.txt", "a")
                f.write(card_type + ",\"")
                if "cost" in attack:
                    f.write(json.dumps(attack["cost"]).replace('\"', '\'') + ',')
                if "name" in attack:
                    f.write(json.dumps(attack["name"]).replace('\"', '') +  ',')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]).replace('\"', '\'') +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]).replace('\"', ''))
                f.write("\"\n")
        elif (card_type == "Darkness"):
            for attack in card.attacks:
                f = open("attacks.txt", "a")
                f.write("Psychic,\"")
                if "cost" in attack:
                    f.write(json.dumps(attack["cost"]).replace('\"', '\'') + ',')
                if "name" in attack:
                    f.write(json.dumps(attack["name"]).replace('\"', '') +  ',')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]).replace('\"', '\'') +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]).replace('\"', ''))
                f.write("\"\n")
        elif (card_type == "Dragon"):
            for attack in card.attacks:
                f = open("attacks.txt", "a")
                f.write("Water,\"")
                if "cost" in attack:
                    f.write(json.dumps(attack["cost"]).replace('\"', '\'') + ',')
                if "name" in attack:
                    f.write(json.dumps(attack["name"]).replace('\"', '') +  ',')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]).replace('\"', '\'') +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]).replace('\"', ''))
                f.write("\"\n")
        elif (card_type == "Fairy"):
            for attack in card.attacks:
                f = open("attacks.txt", "a")
                f.write("Colorless,\"")
                if "cost" in attack:
                    f.write(json.dumps(attack["cost"]).replace('\"', '\'') + ',')
                if "name" in attack:
                    f.write(json.dumps(attack["name"]).replace('\"', '') +  ',')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]).replace('\"', '\'') +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]).replace('\"', ''))
                f.write("\"\n")
        elif (card_type == "Fighting"):
            for attack in card.attacks:
                f = open("attacks.txt", "a")
                f.write(card_type + ",\"")
                if "cost" in attack:
                    f.write(json.dumps(attack["cost"]).replace('\"', '\'') + ',')
                if "name" in attack:
                    f.write(json.dumps(attack["name"]).replace('\"', '') +  ',')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]).replace('\"', '\'') +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]).replace('\"', ''))
                f.write("\"\n")
        elif (card_type == "Fire"):
            for attack in card.attacks:
                f = open("attacks.txt", "a")
                f.write(card_type + ",\"")
                if "cost" in attack:
                    f.write(json.dumps(attack["cost"]).replace('\"', '\'') + ',')
                if "name" in attack:
                    f.write(json.dumps(attack["name"]).replace('\"', '') +  ',')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]).replace('\"', '\'') +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]).replace('\"', ''))
                f.write("\"\n")
        elif (card_type == "Grass"):
            for attack in card.attacks:
                f = open("attacks.txt", "a")
                f.write(card_type + ",\"")
                if "cost" in attack:
                    f.write(json.dumps(attack["cost"]).replace('\"', '\'') + ',')
                if "name" in attack:
                    f.write(json.dumps(attack["name"]).replace('\"', '') +  ',')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]).replace('\"', '\'') +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]).replace('\"', ''))
                f.write("\"\n")
        elif (card_type == "Lightning"):
            for attack in card.attacks:
                f = open("attacks.txt", "a")
                f.write(card_type + ",\"")
                if "cost" in attack:
                    f.write(json.dumps(attack["cost"]).replace('\"', '\'') + ',')
                if "name" in attack:
                    f.write(json.dumps(attack["name"]).replace('\"', '') +  ',')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]).replace('\"', '\'') +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]).replace('\"', ''))
                f.write("\"\n")
        elif (card_type == "Metal"):
            for attack in card.attacks:
                f = open("attacks.txt", "a")
                f.write("Fighting,\"")
                if "cost" in attack:
                    f.write(json.dumps(attack["cost"]).replace('\"', '\'') + ',')
                if "name" in attack:
                    f.write(json.dumps(attack["name"]).replace('\"', '') +  ',')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]).replace('\"', '\'') +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]).replace('\"', ''))
                f.write("\"\n")
        elif (card_type == "Psychic"):
            for attack in card.attacks:
                f = open("attacks.txt", "a")
                f.write(card_type + ",\"")
                if "cost" in attack:
                    f.write(json.dumps(attack["cost"]).replace('\"', '\'') + ',')
                if "name" in attack:
                    f.write(json.dumps(attack["name"]).replace('\"', '') +  ',')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]).replace('\"', '\'') +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]).replace('\"', ''))
                f.write("\"\n")
        if (card_type == "Water"):
            for attack in card.attacks:
                f = open("attacks.txt", "a")
                f.write(card_type + ",\"")
                if "cost" in attack:
                    f.write(json.dumps(attack["cost"]).replace('\"', '\'') + ',')
                if "name" in attack:
                    f.write(json.dumps(attack["name"]).replace('\"', '') +  ',')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]).replace('\"', '\'') +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]).replace('\"', ''))
                f.write("\"\n")
f.close()
