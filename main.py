# This is a creature personal project for the Computer Science Club by Allison LeBus
# Prompt:  Make four creature types, try to have at least one example of inheritance; have three different
# attributes for each creature, have the creatures be able to fight. Simple project, use your
# creativity to make it as simple or complex as you like! Finish by 7/10/2020, we can go over everyone's code
# next meeting.

# This game will have one of four classes battling together, each class if have a damage type, a speed or initiative,
# overall health, and weakness

# There will be two main classes, magic user and weapon user. This will determine damage type and health.

from game_func import *


def main():
    game_state = True
    round_count = 0
    heals = 3

    player = assign_characters(2)

    while game_state:
        for i in range(2):
            active = True
            while active:
                result = fight_menu(player[i])
                if result == "Attack":
                    try:
                        player[i + 1]
                    except IndexError:
                        defender = player[i - 1]
                    else:
                        defender = player[i + 1]
                    attack_result = attack_char(player[i], defender)
                    # returns [game_state, hit, crit, total damage]
                    if not attack_result[0]:
                        print(str(player[i].get_name()) + " attacks for " + str(attack_result[3]) + ", killing "
                              + str(defender.get_name()) + ".\nCongratulations, " + str(player[i].get_name())
                              + ", you have won in " + str(round_count + 1) + " rounds.")
                    else:
                        if attack_result[1] == "Dodge":
                            print(str(player[i].get_name()) + " attacks, but " + str(defender.get_name()) + " dodges.\n")
                        else:
                            if attack_result[2] == "Crit":
                                print("\nCritical hit.")
                            print(str(player[i].get_name()) + " attacks for " + str(attack_result[3]) +
                                  " damage, " + defender.get_name() + " has " + str(defender.get_health()) +
                                  " health.\n")
                    active = False
                    game_state = attack_result[0]
                elif result == "Heal":
                    if heals > 0:
                        if player[i].get_health() == player[i].get_max_health():
                            print("You are already at max health. Pick another action.")
                        else:
                            heals -= 1
                            pts = heal_char(player[i])
                            print(str(player[i].get_name()) + " heals for " + str(pts) + " health points and now has "
                                  + str(player[i].get_health()) + " health.")
                            print(str(player[i].get_name()) + " has " + str(heals) + " health potions left.")
                            active = False
                    else:
                        print(str(player[i].get_name()) + " has no more health potions left, pick another action.")
                elif result == "Defend":
                    print("Defensive stance.")
                else:
                    return sys.exit("Error occurred in picking action.")

            if not game_state:
                break

            round_count += 1


main()
