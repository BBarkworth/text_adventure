import random
import time

class soldier:
    def __init__(self):
        self.health = 100
        self.armour = 50
    
    def __repr__(self):
        return 'soldier'
    
    def quick_attack(self, num):
        health_damage = 40
        armour_damage = 0
        if num > 6:
            return health_damage * 2, armour_damage
        return health_damage, armour_damage

    def power_attack(self):
        health_damage = 35
        armour_damage = 25
        return health_damage, armour_damage

    def damage_taken(self, num, armour_num=0):
        if num < 0 or armour_num < 0:
            raise ValueError
        self.health = self.health - num
        if armour_num > 0:
            if armour_num > self.armour:
                self.armour -= armour_num
                remaining_damage = self.armour * -1
                if self.armour < 0:
                    self.armour = 0
                self.health -= remaining_damage
                if self.health <= 0:
                    return "Game Over"
            else:
                self.armour = self.armour - armour_num
        if self.health <= 0:
            return "Game Over"
        return self.health, self.armour

    def information(self):
        if self.health <= 0:
            return "Dead"
        return "You have {} health and {} armour remaining".format(self.health, self.armour)

    def attack_information(self):
        print("Your quick attack does 40 health damage with a random chance of being activated again, whereas, the power attack does 25 health damage and 25 armour damage")

    def attack_choice(self):
        choice = input("Choose which attack to use. Press 1 for quick attack, 2 for power attack or 3 for more information: ")
        if choice == "1":
            num = random.randint(1,12)
            outcome = self.quick_attack(num)
        elif choice == "2":
            outcome = self.power_attack()
        elif choice == "3":
            outcome = self.attack_information()
            self.attack_choice()
        else:
            self.attack_choice()
        print(outcome)
        return outcome

class mage:
    def __init__(self):
        self.health = 50
        self.armour = 20

    def __repr__(self):
        return 'mage'
    
    def magic_attack(self):
        health_damage = 100
        armour_damage = 20
        return health_damage, armour_damage
    
    def splash_damage_attack(self, opponent_num):
        if opponent_num <= 0:
            raise ValueError
        health_damage = 40 * opponent_num
        armour_damage = 10 * opponent_num
        return health_damage, armour_damage
        # this needs to be applied to all enemies, could use enemy list(?)
        # take out opponent num argument and apply enemy num elsewhere?

    def damage_taken(self, num, armour_num=0):
        if num < 0 or armour_num < 0:
            raise ValueError
        self.health = self.health - (num * 1.5)
        if armour_num > 0:
            if armour_num > self.armour:
                self.armour -= armour_num
                remaining_damage = self.armour * -1
                if self.armour < 0:
                    self.armour = 0
                self.health -= remaining_damage
                if self.health <= 0:
                    return "Game Over"
            else:
                self.armour = self.armour - armour_num
        if self.health <= 0:
            return "Game Over"
        return self.health, self.armour
    
    def information(self):
        if self.health <= 0:
            return "Dead"
        return "You have {} health and {} armour remaining".format(self.health, self.armour)

    def attack_information(self):
        print("Your quick attack does 40 health damage with a random chance of being activated again, whereas, the power attack does 25 health damage and 25 armour damage")

    def attack_choice(self):
        choice = input("Choose which attack to use. Press 1 for magic attack, 2 for splash damage attack or 3 for more information: ")
        if choice == "1":
            outcome = self.magic_attack()
        elif choice == "2":
            outcome = self.splash_damage_attack()
        elif choice == "3":
            outcome = self.attack_information()
            self.attack_choice()
        else:
            print("Please input a number between 1 and 3")
            self.attack_choice()
        print(outcome)
        return outcome

class goblin:
    def __init__(self):
        self.health = 25
    
    def attack(self):
        health_damage = 25
        return health_damage

    def damage_taken(self, num, armour_num=0):
        if num < 0 or armour_num < 0:
            raise ValueError
        self.health = self.health - num
        if armour_num > 0:
            self.health -= armour_num
        if self.health <= 0:
            time.sleep(1)
            return "The goblin has been vanquished"
        return self.health

    def information(self):
        if self.health <= 0:
            return "Dead"
        return self.health
        # needs altering - include goblin name(?) and above info

class troll:
    def __init__(self):
        self.health = 75
        self.armour = 50
    
    def main_attack(self):
        health_damage = 30
        armour_damage = 25
        return health_damage, armour_damage

    def close_to_death(self):
        health_damage = 50
        armour_damage = 10
        return health_damage, armour_damage

    def damage_taken(self, num, armour_num):
        if num < 0 or armour_num < 0:
            raise ValueError
        self.health = self.health - num
        if armour_num > 0:
            if armour_num > self.armour:
                self.armour -= armour_num
                remaining_damage = self.armour * -1
                if self.armour < 0:
                    self.armour = 0
                self.health -= remaining_damage
                if self.health <= 0:
                    return "The troll has been conquered"
            else:
                self.armour = self.armour - armour_num
        if self.health <= 0:
            return "The troll has been conquered"
        return self.health, self.armour

    def information(self):
        if self.health <= 0:
            return "Dead"
        return self.health, self.armour
        # needs altering - include troll name(?) and above info

    def attack_choice(self):
        if self.health < 30:
            num = random.randint(1,12)
            if num > 6: 
                outcome = self.close_to_death()
                return outcome
            else:
                outcome = self.main_attack()
                return outcome
        outcome = self.main_attack()
        return outcome

    # make health private?
    # include orc class? include method to kill other orc if number over 9 rolled?
    # include level up ability after kills = more health/armour?
    # include ability to leave before fighing more enemies??