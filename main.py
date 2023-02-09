from adventure_game import *
import time

def player_choice():
    name = input("What is your name? ")
    if name == "":
        name = "the nameless one"
    time.sleep(0.5)
    print("Welcome", name)
    time.sleep(1.5)
    choice = input("Choose whether you would like to be a soldier or a mage: ")
    if choice.lower() == "soldier":
        player = soldier(name)
    elif choice.lower() == "mage":
        player = mage(name)
    else:
        player = soldier(name)
        print("You're playing as a soldier because you didn't pick one of the class options")
    return player

def enemy_spawn():
    pass
    # add random percentages for enemy spawns - goblin most, then orc and troll

if __name__=='__main__':
    player = player_choice()
    enemy_list = []
    orc_list = []

    goblin_one = goblin("Goblin soldier", enemy_list)
    print("Look out, a goblin soldier has appeared")
    time.sleep(1.5)
    while goblin_one.health > 0:
        try:
            print(player.attack_information())
            choice = input("Choose which attack to use. Press 1 for your primary attack or 2 for your secondary attack: ")
        except:
            choice == "1" or choice == "2"
        player_attack = player.attack_choice(choice, enemy_list)
        goblin_one.damage_taken(player_attack[0], player_attack[1])
        print(goblin_one.information(enemy_list))
        if goblin_one.health <= 0:
            print(player.information())
            break
        goblin_attack = goblin_one.attack()
        player.damage_taken(goblin_attack)
        if player.health <= 0:
            break
        print(player.information())
    troll_one = troll("Cave troll", enemy_list)
    print("A cave troll has awoken from its slumber")
    time.sleep(1.5)
    while troll_one.health > 0:
        try:
            print(player.attack_information())
            choice = input("Choose which attack to use. Press 1 for your primary attack or 2 for your secondary attack: ")
        except:
            choice == "1" or choice == "2"
        player_attack = player.attack_choice(choice, enemy_list)
        troll_one.damage_taken(player_attack[0], player_attack[1])
        print(troll_one.information(enemy_list))
        if troll_one.health <= 0:
            break
        troll_attack = troll_one.attack_choice()
        player.damage_taken(troll_attack[0], troll_attack[1])
        if player.health <= 0:
            print(player.information())
            break
        print(player.information())
    if player.health > 0:
        print("You were victorious, but this was only the tutorial")
        time.sleep(1.5)
        print("Get ready for the next set of enemies")
        player.level_up()
    else:
        print("You were slain")
        time.sleep(1)
        print("Game Over")

# include total enemies at one time + num of enemies to finish level + 2 spawn at 1st
# generic text to indicate what has spawned in?
# add multiple players option - player list and loop?
# put main script in try/except statement to loop back for multi playthroughs?
# fancy writing libraries/wrappers?
# create generic enemy interaction function - ??
# rework enemy class info methods so they display health/armour in readable format
# add time delays

# splash damage - returning any value above 0 causes issues as that is applied on top of looping damage
# change health damage - increase it or force armour to be 0 as well for death? - maybe just trolls die from health damage?
# fix orc remove from list issue
# could keep the dice roll separate as a function as then it could be passed in as a parameter - should stop test fails

# method results can be accessed individually rather than used as a variable - fix main code?