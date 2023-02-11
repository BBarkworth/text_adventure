import random

class soldier:
    def __init__(self, name):
        self.health = 100
        self.armour = 50
        self.name = name
        self.current_level = 1
        self.original_health = self.health
        self.original_armour = self.armour
    
    def __repr__(self):
        return 'soldier'
    
    def quick_attack(self):
        health_damage = 40
        armour_damage = 0
        num = random.randint(1,12)
        if num > 6:
            return health_damage * 2, armour_damage
        return health_damage, armour_damage

    def power_attack(self):
        health_damage = 35
        armour_damage = 25
        return (health_damage, armour_damage)

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
        return "Your quick attack does 40 health damage with a random chance of being activated again, whereas, the power attack does 25 health damage and 25 armour damage"

    def attack_choice(self, choice, enemy_list):
        if choice == "1":
            outcome = self.quick_attack()
        elif choice == "2":
            outcome = self.power_attack()
        else:
            return self.attack_information()
        return outcome
    
    def level_up(self):
        self.original_health = self.original_health + 25
        self.original_armour = self.original_armour + 25
        self.health = self.original_health
        self.armour = self.original_armour
        self.current_level = self.current_level + 1
        print("You are now rank {} with {} health and {} armour".format(self.current_level, self.health, self.armour))

class mage:
    def __init__(self, name):
        self.health = 50
        self.armour = 20
        self.name = name
        self.current_level = 1
        self.original_health = self.health
        self.original_armour = self.armour

    def __repr__(self):
        return 'mage'
    
    def magic_attack(self):
        health_damage = 100
        armour_damage = 20
        return health_damage, armour_damage
    
    def splash_damage_attack(self, enemy_list):
        if len(enemy_list) <= 0:
            raise ValueError
        health_damage = 40
        armour_damage = 10
        for i in enemy_list:
            i.damage_taken(health_damage, armour_damage)
        return 0,0
        # - returning any value above 0 causes issues as that is applied on top of looping damage

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
        return "Your magic attack does 100 health damage and 20 armour damage, whereas, the splash damage attack does 40 health damage and 10 armour damage for each enemy"

    def attack_choice(self, choice, enemy_list):
        if choice == "1":
            outcome = self.magic_attack()
        elif choice == "2":
            outcome = self.splash_damage_attack(enemy_list)
        else:
            return self.attack_information()
        return outcome

    def level_up(self):
        self.original_health = self.original_health + 25
        self.original_armour = self.original_armour + 25
        self.health = self.original_health
        self.armour = self.original_armour
        self.current_level = self.current_level + 1
        print("You are now rank {} with {} health and {} armour".format(self.current_level, self.health, self.armour))

class goblin:
    def __init__(self, enemies_list):
        self.health = 25
        enemies_list.append(self)
        print("A goblin has appeared")

    def __repr__(self):
        return 'goblin'
    
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
            return 0
        return self.health

    def information(self, enemy_list):
        if self.health <= 0:
            enemy_list.remove(self)
            return "The goblin is dead"
        return "The goblin has {} health remaining".format(self.health)

class troll:
    def __init__(self, enemies_list):
        self.health = 75
        self.armour = 50
        enemies_list.append(self)
        print("A troll has appeared")

    def __repr__(self):
        return 'troll'
    
    def main_attack(self):
        health_damage = 30
        armour_damage = 25
        return health_damage, armour_damage

    def close_to_death(self):
        health_damage = 50
        armour_damage = 10
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
                    return 0
            else:
                self.armour = self.armour - armour_num
        if self.health <= 0:
            return 0
        return self.health, self.armour

    def information(self, enemy_list):
        if self.health <= 0:
            enemy_list.remove(self)
            return "The troll is dead"
        return "The troll has {} health and {} remaining".format(self.health, self.armour)

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

class orc:
    def __init__(self, enemies_list, orc_list):
        self.health = 50
        self.armour = 50
        enemies_list.append(self)
        orc_list.append(self)
        print("An orc has appeared")

    def __repr__(self):
        return 'orc'

    def main_attack(self):
        health_damage = 35
        armour_damage = 15
        return health_damage, armour_damage
    
    def damage_taken(self, health_num, armour_num=0):
        if health_num < 0 or armour_num < 0:
            raise ValueError
        self.health = self.health - health_num
        if armour_num > 0:
            if armour_num > self.armour:
                self.armour -= armour_num
                remaining_damage = self.armour * -1
                if self.armour < 0:
                    self.armour = 0
                self.health -= remaining_damage
                if self.health <= 0:
                    return 0
            else:
                self.armour = self.armour - armour_num
        if self.health <= 0:
            return 0
        return self.health, self.armour
    
    def survival_of_the_fittest(self, orc_list, enemy_list):
        health_damage = 50
        armour_damage = 50
        for i in orc_list:
            if i == self:
                continue
            else:
                i.damage_taken(health_damage, armour_damage)
        print("Infighting has broken out between the orcs")
        return i.information(enemy_list, orc_list)

    def information(self, enemy_list, orc_list):
        if self.health <= 0:
            enemy_list.remove(self)
            orc_list.remove(self)
            return "The orc is dead"
        return "The orc has {} health and {} remaining".format(self.health, self.armour)

    def attack_choice(self, orc_list, enemy_list):
        num = random.randint(1,12)
        if num > 9 and len(orc_list) > 1:
            outcome = self.survival_of_the_fittest(orc_list, enemy_list)
            return outcome
        else:
            outcome = self.main_attack()
            return outcome