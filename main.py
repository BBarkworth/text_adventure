from adventure_game import *
import time
import random

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

def enemy_spawn(level_enemy_number):
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
    # move functions to separate file

def dice_roll():
    num = random.randint(1,12)
    return num

if __name__=='__main__':
    player = player_choice()
    enemy_list = []
    orc_list = []

    time.sleep(1)
    goblin_one = goblin(enemy_list)
    print("A goblin has appeared")
    time.sleep(1.5)
    while goblin_one.health > 0:
        while True:
            print(player.attack_information())
            choice = input("Choose which attack to use. Press 1 for your primary attack or 2 for your secondary attack: ")
            choice = str(choice)
            if choice == "1" or choice == "2":
                break
        roll = dice_roll()
        player_attack = player.attack_choice(choice, enemy_list, roll)
        goblin_one.damage_taken(player_attack[0], player_attack[1])
        time.sleep(1.5)
        print(goblin_one.information(enemy_list, orc_list))
        if goblin_one.health <= 0:
            time.sleep(1)
            print(player.information())
            break
        goblin_attack = goblin_one.attack()
        player.damage_taken(goblin_attack[0], goblin_attack[1])
        if player.health <= 0:
            break
        print(player.information())
    troll_one = troll(enemy_list)
    print("A cave troll has awoken from its slumber")
    time.sleep(1.5)
    while troll_one.health > 0:
        while True:
            print(player.attack_information())
            choice = input("Choose which attack to use. Press 1 for your primary attack or 2 for your secondary attack: ")
            choice = str(choice)
            if choice == "1" or choice == "2":
                break
        time.sleep(1.5)
        roll = dice_roll()
        player_attack = player.attack_choice(choice, enemy_list, roll)
        troll_one.damage_taken(player_attack[0], player_attack[1])
        time.sleep(1.5)
        print(troll_one.information(enemy_list, orc_list))
        if troll_one.health <= 0:
            time.sleep(1)
            break
        enemy_roll = dice_roll()
        troll_attack = troll_one.attack_choice(enemy_roll)
        player.damage_taken(troll_attack[0], troll_attack[1])
        if player.health <= 0:
            time.sleep(1)
            print(player.information())
            break
        time.sleep(1.5)
        print(player.information())
    if player.health > 0:
        print("You were victorious but this was only the tutorial")
        time.sleep(1.5)
        print("Get ready for the next set of enemies")
        time.sleep(1.5)
        player.level_up()
    else:
        print("You were slain")
        time.sleep(1)
        print("Game Over")

    counter = 0
    level_enemies = 5
    new_level = enemy_spawn(level_enemies)
    print("More enemies have appeared")
    while player.health > 0:
        if len(enemy_list) == 0:
            print("More enemies have appeared")
            player.level_up()
            new_level = enemy_spawn(level_enemies)
            time.sleep(1.5)
        copy_list = enemy_list.copy()
        while True:
            print(player.attack_information())
            choice = input("Choose which attack to use. Press 1 for your primary attack or 2 for your secondary attack: ")
            choice = str(choice)
            if choice == "1" or choice == "2":
                break
        time.sleep(1.5)
        roll = dice_roll()
        player_attack = player.attack_choice(choice, enemy_list, roll)
        for j in enemy_list:
            print(j)
        if player_attack == (0, 0):
            for k in copy_list:
                print(k.information(enemy_list, orc_list))
                # copy list used to avoid mutation issues with loop
                time.sleep(1)
        else:
            while True:
                enemy_choice = input("Choose which enemy to attack by inputting their name: ")
                enemy_choice = str(enemy_choice)
                if enemy_choice.lower() == "goblin" or enemy_choice.lower() == "orc" or enemy_choice.lower() == "troll":
                    break
            for k in copy_list:
                if enemy_choice == str(k):
                    k.damage_taken(player_attack[0], player_attack[1])
                    print(k.information(enemy_list, orc_list))
                    # move information to be above attack input?
                    break
                counter += 1
        time.sleep(2.5)
        if len(enemy_list) == 0:
            continue
        else:
            num = random.randint(0,len(enemy_list) - 1)
            enemy = enemy_list[num]
            enemy_roll = dice_roll()
            enemy_attack = enemy.attack_choice(enemy_roll, orc_list, enemy_list)
            if str(enemy) != "orc":
                player.damage_taken(enemy_attack[0], enemy_attack[1])
            else:
                if enemy_attack == enemy.main_attack():
                    player.damage_taken(enemy_attack[0], enemy_attack[1])
                else:
                    print(enemy_attack)
            if player.health <= 0:
                break
            print(player.information())
    print("You were slain")
    time.sleep(1.5)
    print("You reached level {}".format(player.current_level))

# add multiple players option - player list and loop?
# fancy writing libraries/wrappers?

# change health damage - increase it or force armour to be 0 as well for death? - maybe just trolls die from health damage?

# method results can be accessed individually rather than used as a variable - fix main code?

# comment code thoroughly