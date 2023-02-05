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

    while player.information() != "Dead":
        goblin_one = goblin()
        print("Look out, a goblin has appeared")
        time.sleep(1.5)
        while goblin_one.information() != "Dead":
            player_attack = player.attack_choice()
            goblin_one.damage_taken(player_attack[0],player_attack[1])
            goblin_attack = goblin_one.attack()
            player.damage_taken(goblin_attack)
            if player.health == 0:
                break
            player.information()
        troll_one = troll()
        print("A cave troll has awoken from its slumber")
        time.sleep(1.5)
        while troll_one.information() != "Dead":
            player_attack = player.attack_choice()
            troll_one.damage_taken(player_attack[0],player_attack[1])
            troll_attack = troll_one.attack_choice()
            player.damage_taken(troll_attack[0], troll_attack[1])
            if player.health == 0:
                break
            player.information()
    if player.health > 0:
        print("You were victorious")
    else:
        print("You were slain")

    '''
    if move_counter > 2:
        goblin_two = goblin()
        print("You've attracted the attention of another goblin")
    move_counter += 1
    '''

# add multiple players option
# put main script in try/except statement to loop back through?