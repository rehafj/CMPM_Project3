import json

from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype

cards = Card.where(supertype='pokemon')
for card in cards:
    card_type = card.types[0]
    #print(card.attacks)
    if card.attacks is not None:
        if (card_type == "Colorless"):
            for attack in card.attacks:
                f = open("colorless_attack.txt", "a")
                f.write(card_type + ",")
                f.write('\"' + json.dumps(attack["cost"]) + '\",')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]) +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]))
                f.write("\n\n")
                f.close()
        elif (card_type == "Darkness"):
            for attack in card.attacks:
                f = open("psychic_attack.txt", "a")
                f.write("Psychic,")
                if "cost" in attack:
                    f.write('\"' + json.dumps(attack["cost"]) + '\",')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]) +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]))
                f.write("\n\n")
                f.close()
        elif (card_type == "Dragon"):
            for attack in card.attacks:
                f = open("water_attack.txt", "a")
                f.write("Water,")
                if "cost" in attack:
                    f.write('\"' + json.dumps(attack["cost"]) + '\",')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]) +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]))
                f.write("\n\n")
                f.close()
        elif (card_type == "Fairy"):
            for attack in card.attacks:
                f = open("colorless_attack.txt", "a")
                f.write("Colorless,")
                if "cost" in attack:
                    f.write('\"' + json.dumps(attack["cost"]) + '\",')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]) +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]))
                f.write("\n\n")
                f.close()
        elif (card_type == "Fighting"):
            for attack in card.attacks:
                f = open("fighting_attack.txt", "a")
                f.write(card_type + ",")
                if "cost" in attack:
                    f.write('\"' + json.dumps(attack["cost"]) + '\",')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]) +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]))
                f.write("\n\n")
                f.close()
        elif (card_type == "Fire"):
            for attack in card.attacks:
                f = open("fire_attack.txt", "a")
                f.write(card_type + ",")
                if "cost" in attack:
                    f.write('\"' + json.dumps(attack["cost"]) + '\",')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]) +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]))
                f.write("\n\n")
                f.close()
        elif (card_type == "Grass"):
            for attack in card.attacks:
                f = open("grass_attack.txt", "a")
                f.write(card_type + ",")
                if "cost" in attack:
                    f.write('\"' + json.dumps(attack["cost"]) + '\",')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]) +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]))
                f.write("\n\n")
                f.close()
        elif (card_type == "Lightning"):
            for attack in card.attacks:
                f = open("lightning_attack.txt", "a")
                f.write(card_type + ",")
                if "cost" in attack:
                    f.write('\"' + json.dumps(attack["cost"]) + '\",')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]) +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]))
                f.write("\n\n")
                f.close()
        elif (card_type == "Metal"):
            for attack in card.attacks:
                f = open("fighting_attack.txt", "a")
                f.write("Fighting,")
                if "cost" in attack:
                    f.write('\"' + json.dumps(attack["cost"]) + '\",')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]) +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]))
                f.write("\n\n")
                f.close()
        elif (card_type == "Psychic"):
            for attack in card.attacks:
                f = open("psychic_attack.txt", "a")
                f.write(card_type + ",")
                if "cost" in attack:
                    f.write('\"' + json.dumps(attack["cost"]) + '\",')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]) +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]))
                f.write("\n\n")
                f.close()
        else: # water
            for attack in card.attacks:
                f = open("water_attack.txt", "a")
                if "cost" in attack:
                    f.write('\"' + json.dumps(attack["cost"]) + '\",')
                if "text" in attack:
                    f.write(json.dumps(attack["text"]) +  ',')
                if "damage" in attack:
                    f.write(json.dumps(attack["damage"]))
                f.write("\n\n")
                f.close()
