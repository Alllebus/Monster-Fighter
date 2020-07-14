from character_class import *
import re
import sys


def create_character(player_num):
    fighter = True
    while fighter:
        player_char = input("Player " + str(player_num) + ", choose your fighter class: "
                                                          "\nMystic, Elementalist, Assassin, Knight \n")
        if re.match('[Mm]ystic', player_char):
            fighter = False
            char = Mystic()
        elif re.match('[Ee]lementalist', player_char):
            fighter = False
            char = Elementalist()
        elif re.match('[Aa]ssassin', player_char):
            fighter = False
            char = Assassin()
        elif re.match('[Kk]night', player_char):
            fighter = False
            char = Knight()
        else:
            print("Please pick a fighter class.")
    char_name = input("Player " + str(player_num) + ", name your character: ")
    return [char_name, char]


def assign_characters(num_of_char):
    while not type(num_of_char) == int:
        num_of_char = input("Enter an integer")
    player = [GenClass()] * num_of_char
    for i in range(num_of_char):
        char = create_character(i+1)
        player[i] = char[1]
        player[i].set_name(char[0])
        print("\n")
    return player


def heal_char(char):
    pts = 15 + random.randint(0, 30)
    char.heal(pts)
    return pts


def defend_char(char):
    return True


def attack_char(attacker, defender):
    crit = ""
    dodge_chance = defender.dodge()
    if dodge_chance == "Dodge":
        hit = "Dodge"
        game_state = True
        crit = ""
        total_dmg = 0
        return [game_state, hit, crit, total_dmg]
    hit = "Hit"
    dmg = attacker.attack()
    if dmg[1] == "Crit":
        crit = "Crit"
    dmg_taken = defender.take_damage(dmg, attacker.get_dmg_type())
    if dmg_taken[0] == "Alive":
        game_state = True
        return [game_state, hit, crit, dmg_taken[1]]
    elif dmg_taken[0] == "Dead":
        game_state = False
        return [game_state, hit, crit, dmg_taken[1]]
    else:
        return sys.exit("Error occurred in attack_char.")


def fight_menu(active):
    choosing = True
    while choosing:
        action = input("\n" + str(active.get_name()) + ", pick an action: \nAttack, Heal, Defend \n")
        if re.match("[Aa]ttack", action):
            result = "Attack"
            return result
        elif re.match("[Hh]eal", action):
            result = "Heal"
            return result
        elif re.match("[Dd]efend", action):
            result = "Defend"
            return result
        else:
            print("Pick again.")
            choosing = True
