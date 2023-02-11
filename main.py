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

def enemy_spawn(level_enemy_number):
    enemies_list = ["goblin", "troll", "orc"]
    for i in range(len(level_enemy_number)):
        enemy = random.choices(enemies_list, weights=(40,25,35), k = 1)
        if enemy[i] == "goblin":
            goblin(enemy_list)
        elif enemy[i] == "troll":
            troll(enemy_list)
        else:
            orc(enemy_list, orc_list)
        time.sleep(1.5)

if __name__=='__main__':
    player = player_choice()
    enemy_list = []
    orc_list = []

    time.sleep(1)
    goblin_one = goblin(enemy_list)
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
        time.sleep(1.5)
        print(goblin_one.information(enemy_list))
        if goblin_one.health <= 0:
            time.sleep(1)
            print(player.information())
            break
        goblin_attack = goblin_one.attack()
        player.damage_taken(goblin_attack)
        if player.health <= 0:
            break
        print(player.information())
    troll_one = troll(enemy_list)
    print("A cave troll has awoken from its slumber")
    time.sleep(1.5)
    while troll_one.health > 0:
        try:
            print(player.attack_information())
            choice = input("Choose which attack to use. Press 1 for your primary attack or 2 for your secondary attack: ")
        except:
            choice == "1" or choice == "2"
        time.sleep(1.5)
        player_attack = player.attack_choice(choice, enemy_list)
        troll_one.damage_taken(player_attack[0], player_attack[1])
        time.sleep(1.5)
        print(troll_one.information(enemy_list))
        if troll_one.health <= 0:
            time.sleep(1)
            break
        troll_attack = troll_one.attack_choice()
        player.damage_taken(troll_attack[0], troll_attack[1])
        if player.health <= 0:
            time.sleep(1)
            print(player.information())
            break
        time.sleep(1.5)
        print(player.information())
    if player.health > 0:
        print("You were victorious, but this was only the tutorial")
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
    while len(enemy_list) > 0:
        new_level = enemy_spawn(level_enemies)

        # moves variable - 1 move for each side or 1 move for player + enemy? - each move could just be the actions in a loop iteration?
        # fight with enemy_list item i.e. individual enemy and vice_versa?
        # how to end level? - death indicator? - add to enemy information method and compare variable/method output with level_enemy_number to indicate level end?

# change spawn so everything spawns in at once and then move check can be if any enemies are left - combine with player choosing what enemy to attack?
# add death method for enemies to make all attacks 0 if health is 0?

# add multiple players option - player list and loop?
# fancy writing libraries/wrappers?

# change health damage - increase it or force armour to be 0 as well for death? - maybe just trolls die from health damage?
# could keep the dice roll separate as a function as then it could be passed in as a parameter - should stop test fails, 'dice' would have to be rolled/called every turn before choice option so it can be passed in if necessary

# method results can be accessed individually rather than used as a variable - fix main code?