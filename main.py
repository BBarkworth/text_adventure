from adventure_game import *
from helpers import player_choice, enemy_spawn, dice_roll
from art import *
import time
import random
import sys

if __name__=='__main__':
    player = player_choice()
    # player object
    enemy_list = []
    orc_list = []
    # enemy lists for different methods

    time.sleep(1)
    goblin_one = goblin(enemy_list)
    # goblin object
    print("A goblin has appeared")
    time.sleep(1.5)

    # goblin encounter loop
    while goblin_one.health > 0:
        # attack choice loop for user input
        while True:
            print(player.attack_information())
            choice = input("Choose which attack to use. Press 1 for your primary attack or 2 for your secondary attack: ")
            choice = str(choice)
            if choice == "1" or choice == "2":
                break
        # player attack
        roll = dice_roll()
        player_attack = player.attack_choice(choice, enemy_list, roll)
        goblin_one.damage_taken(player_attack[0], player_attack[1])
        time.sleep(1.5)
        print(goblin_one.information(enemy_list, orc_list))
        # conditional check to end loop
        if goblin_one.health <= 0:
            time.sleep(1)
            print(player.information())
            break
        # goblin attack
        goblin_attack = goblin_one.attack()
        player.damage_taken(goblin_attack[0], goblin_attack[1])
        # conditional check to end loop
        if player.health <= 0:
            break
        print(player.information())
    
    # troll object
    troll_one = troll(enemy_list)
    print("A cave troll has awoken from its slumber")
    time.sleep(1.5)
    # troll encounter loop
    while troll_one.health > 0:
        # attack choice loop for user input
        while True:
            print(player.attack_information())
            choice = input("Choose which attack to use. Press 1 for your primary attack or 2 for your secondary attack: ")
            choice = str(choice)
            if choice == "1" or choice == "2":
                break
        # player attack
        roll = dice_roll()
        player_attack = player.attack_choice(choice, enemy_list, roll)
        troll_one.damage_taken(player_attack[0], player_attack[1])
        time.sleep(1.5)
        print(troll_one.information(enemy_list, orc_list))
         # conditional check to end loop
        if troll_one.health <= 0:
            time.sleep(1)
            break
         # troll attack
        enemy_roll = dice_roll()
        troll_attack = troll_one.attack_choice(enemy_roll)
        player.damage_taken(troll_attack[0], troll_attack[1])
        time.sleep(1.5)
        # conditional check to end loop
        if player.health <= 0:
            break
        time.sleep(1.5)
        print(player.information())
    # end of loop conditionals
    if player.health > 0:
        print("You were victorious but this was only the tutorial")
        time.sleep(1.5)
        print("Get ready for the next set of enemies")
        time.sleep(1.5)
        print(player.level_up())
    else:
        tprint("You were slain", font="slant")
        time.sleep(1)
        tprint("Game over", font="slant")
        sys.exit()

    # num of level enemies set at 5
    level_enemies = 5
    # spawn enemies
    new_level = enemy_spawn(level_enemies, enemy_list, orc_list)
    print("More enemies have appeared")
    # level encounter loop
    while player.health > 0:
        # conditional check to start new level and level up character
        if len(enemy_list) == 0:
            print("More enemies have appeared")
            print(player.level_up())
            new_level = enemy_spawn(level_enemies, enemy_list, orc_list)
            time.sleep(1.5)
        # copy list used to avoid mutation issues with loop for splash damage attack
        copy_list = enemy_list.copy()
        # attack choice inout loop
        while True:
            print(player.attack_information())
            choice = input("Choose which attack to use. Press 1 for your primary attack or 2 for your secondary attack: ")
            choice = str(choice)
            if choice == "1" or choice == "2":
                break
        time.sleep(1.5)
        roll = dice_roll()
        player_attack = player.attack_choice(choice, enemy_list, roll)
        # list enemies 
        for j in enemy_list:
            print(j)
        # splash damage attack conditional
        if player_attack == (0, 0):
            for k in copy_list:
                print(k.information(enemy_list, orc_list))
                time.sleep(1)
        else:
            # choosing enemy to attack input loop
            while True:
                enemy_choice = input("Choose which enemy to attack by inputting their name: ")
                enemy_choice = str(enemy_choice)
                if enemy_choice.lower() == "goblin" or enemy_choice.lower() == "orc" or enemy_choice.lower() == "troll":
                    break
            # applying player damage to enemy
            for k in copy_list:
                if enemy_choice == str(k):
                    k.damage_taken(player_attack[0], player_attack[1])
                    print(k.information(enemy_list, orc_list))
                    break
        time.sleep(2.5)
        # end of level conditional check
        if len(enemy_list) == 0:
            continue
        # # random enemy chosen to attack player
        else:
            num = random.randint(0,len(enemy_list) - 1)
            enemy = enemy_list[num]
            enemy_roll = dice_roll()
            # enemy attack chosen with dice roll passed in as parameter
            enemy_attack = enemy.attack_choice(enemy_roll, orc_list, enemy_list)
            # conditional check for orc as survival_of_the_fittest needs to be applied differently
            if str(enemy) != "orc":
                player.damage_taken(enemy_attack[0], enemy_attack[1])
            else:
                if enemy_attack == enemy.main_attack():
                    player.damage_taken(enemy_attack[0], enemy_attack[1])
                else:
                    print(enemy_attack)
            # player health check to end level
            if player.health <= 0:
                break
            # health and armour information for plaer
            print(player.information())
    # print statements for the end of the game
    tprint("You were slain", font="slant")
    time.sleep(1.5)
    tprint("Game over", font="slant")
    time.sleep(1.5)
    tprint("You reached level {}".format(player.current_level), font="slant")

    # finish tests