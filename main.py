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
        player = soldier()
    elif choice.lower() == "mage":
        player = mage()
    else:
        player = soldier()
        print("You're playing as a soldier because you didn't pick one of the class options")
    return player

if __name__=='__main__':
    player = player_choice()
    enemy_list = []

    while player.information() != "Dead":
        goblin_one = goblin("Goblin soldier", enemy_list)
        print("Look out, a goblin has appeared")
        time.sleep(1.5)
        while goblin_one.health > 0:
            player_attack = player.attack_choice()
            goblin_one.damage_taken(player_attack[0],player_attack[1])
            goblin_attack = goblin_one.attack()
            player.damage_taken(goblin_attack)
            if player.health <= 0:
                break
            player.information()
        print(goblin_one.information())
        troll_one = troll("Cave troll", enemy_list)
        print("A cave troll has awoken from its slumber")
        time.sleep(1.5)
        while troll_one.health > 0:
            player_attack = player.attack_choice()
            troll_one.damage_taken(player_attack[0],player_attack[1])
            troll_attack = troll_one.attack_choice()
            player.damage_taken(troll_attack[0], troll_attack[1])
            if player.health <= 0:
                break
            player.information()
        print(troll_one.information())
    if player.health > 0:
        print("You were victorious, but this was only the tutorial")
        time.sleep(1.5)
        print("Get ready for the next set of enemies")
        player.level_up()
    else:
        print("You were slain")

# add multiple players option
# put main script in try/except statement to loop back for multi playthroughs?
# random option for spawning enemies?