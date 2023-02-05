from adventure_game import *
import time

if __name__=='__main__':
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
goblin_one = goblin()
print("Look out, a goblin has appeared")
time.sleep(1.5)

while goblin_one.information() != "Dead":
    if repr(player) == "soldier":
        attack_choice = input("Choose which attack to use. Press 1 for quick attack, 2 for power attack or 3 for more information: ")
        if attack_choice == "1":
            quick_attack = player.quick_attack()
            goblin_one.damage_taken(quick_attack)
        elif attack_choice == "2":
            power_attack = player.power_attack()
            goblin_one.damage_taken(power_attack)
        else:
            attack_choice = "3"
    # incorrect input check needed
    if repr(player) == "mage":    
        attack_choice = input("Choose which attack to use. Press 1 for magic attack, 2 for splash damage attack or 3 for more information: ")
        if attack_choice == "1":
            magic_attack = player.magic_attack()
            goblin_one.damage_taken(magic_attack)
        elif attack_choice == "2":
            splash_attack = player.splash_damage_attack()
            goblin_one.damage_taken(splash_attack)
        else:
            attack_choice = "3"
    goblin_attack = goblin_one.attack()
    player.damage_taken(goblin_attack)
    # incorrect input check needed
    if player.damage_taken() == "Game Over":
        break
player.information()

troll_one = troll()
print("A cave troll has awoken from its slumber")
time.sleep(1.5)
'''
if move_counter > 2:
    goblin_two = goblin()
    print("You've attracted the attention of another goblin")
move_counter += 1
'''

# present input options for player
# create attack information method for battle or when character created
# convert attack choices into functions?
# add multiple players option