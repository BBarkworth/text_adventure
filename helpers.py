from adventure_game import *
import time
import random

# function for choosing player class
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

# function for enemy spawns for each level
def enemy_spawn(level_enemy_number, enemy_list, orc_list):
    enemies_list = ["goblin", "troll", "orc"]
    for i in range(level_enemy_number):
        enemy = random.choices(enemies_list, weights=(40,25,35), k = 1)
        if enemy[0] == "goblin":
            goblin(enemy_list)
        elif enemy[0] == "troll":
            troll(enemy_list)
        else:
            orc(enemy_list, orc_list)
        time.sleep(1.5)

# dice roll to pass in as num for various methods
def dice_roll():
    num = random.randint(1,12)
    return num