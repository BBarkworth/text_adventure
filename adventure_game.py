import random

class soldier:
    def __init__(self):
        self.health = 100
        self.armour = 50
    
    def __repr__(self):
        return 'soldier'
    
    def quick_attack(self):
        health_damage = 40
        return health_damage
    # link in with random chance of doing another quick attack if
    # fake dice roll is above 6

    def power_attack(self):
        health_damage = 25
        # make health damage higher?
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
            return 0
        print("You have {} health and {} armour remaining".format(self.health, self.armour))

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

    def damage_taken(self, num, armour_num):
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
            return "The player has died"
        print("You have {self.health} remaining and {self.armour} armour remaining")

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
            print("The goblin has been vanquished")
        return self.health

    def information(self):
        if self.health <= 0:
            return "Dead"
        return self.health
        # expand information out

class troll:
    def __init__(self):
        self.health = 75
        self.armour = 50
    
    def main_attack(self):
        health_damage = 30
        armour_damage = 25
        return health_damage, armour_damage

    # add attack based on health below a certain point e.g. desperation attack

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
        # expand information out

    # make health private?
    # include orc class? include method to kill other orc if number over 9 rolled?
    # include level up ability after kills = more health/armour?
    # include ability to leave before fighing more enemies??
    # create repo?