from adventure_game import *
import time

if __name__=='__main__':
    # change this into function with a loop so player can start again or leave?
    name = input("What is your name? ")
    if name == "":
        name = "The nameless one"
    choice = input("Choose whether you would like to be a soldier or a mage: ")
    if choice.lower() != "soldier" or choice.lower() != "mage":
        player = soldier()
        print("You're playing as the soldier because you didn't specify a class")
    elif choice.lower() == "soldier":
        player = soldier()
    else:
        player = mage()

    while player.information() != "Dead":
        goblin_one = goblin()
        print("Look out, a goblin has appeared")
        time.sleep(1.5)
        while goblin_one.information() != "Dead":
            attack_choice = input("Choose which attack to use. Press 1 for quick attack, 2 for power attack or 3 for more information: ")
            player_attack = player.attack_choice(attack_choice)
            goblin_one.damage_taken(player_attack)
            goblin_attack = goblin_one.attack()
            player.damage_taken(goblin_attack)
            # incorrect input check needed
            if player.information() == 0:
                break
        troll_one = troll()
        print("A cave troll has awoken from its slumber")
        time.sleep(1.5)
    print("You were slain")

    '''
    if move_counter > 2:
        goblin_two = goblin()
        print("You've attracted the attention of another goblin")
    move_counter += 1
    '''

# add multiple players option