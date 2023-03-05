import unittest
from adventure_game import *

class Testclasses(unittest.TestCase):

    def test_soldier(self):
        enemy_list = []
        test_soldier = soldier("test_soldier")
        self.assertEqual(test_soldier.power_attack(), (35,25))
        for i in range(1, 13):
            if i > 6:
                self.assertEqual(test_soldier.quick_attack(i), (80,0))
            else:
                self.assertEqual(test_soldier.quick_attack(i), (40,0))
        self.assertEqual(test_soldier.information(), "You have 100 health and 50 armour remaining")
        self.assertEqual(test_soldier.damage_taken(30, 0), (70,50))
        self.assertEqual(test_soldier.information(), "You have 70 health and 50 armour remaining")
        self.assertEqual(test_soldier.damage_taken(70, 0), "Game Over")
        test_soldier = soldier("test_soldier")
        self.assertEqual(test_soldier.damage_taken(0, 20), (100,30))
        self.assertEqual(test_soldier.damage_taken(0, 50), (80,0))
        self.assertEqual(test_soldier.information(), "You have 80 health and 0 armour remaining")
        self.assertEqual(test_soldier.damage_taken(0, 75), (5,0))
        self.assertEqual(test_soldier.attack_choice("1", enemy_list, 1), (test_soldier.quick_attack(1)))
        self.assertEqual(test_soldier.attack_choice("2", enemy_list, 1), (test_soldier.power_attack()))
        self.assertEqual(test_soldier.attack_choice("3", enemy_list, 1), (test_soldier.attack_information()))
        self.assertEqual(test_soldier.attack_information(), "Your quick attack does 40 health damage with a random chance of being activated again, whereas, the power attack does 35 health damage and 25 armour damage")
        test_soldier2 = soldier("test_soldier")
        self.assertEqual(test_soldier2.level_up(), "You are now rank 2 with 125 health and 75 armour")
        self.assertEqual(test_soldier2.level_up(), "You are now rank 3 with 150 health and 100 armour")
    
    def test_input(self):
        enemy_list = []
        orc_num = []
        test_soldier = soldier("test_soldier")
        test_mage = mage("test_mage")
        with self.assertRaises(ValueError):
            test_soldier.damage_taken(-10, 0)
        with self.assertRaises(ValueError):
            test_mage.damage_taken(-20, 0)
        with self.assertRaises(ValueError):
            test_mage.splash_damage_attack(enemy_list)
        with self.assertRaises(ValueError):
            test_mage.splash_damage_attack(enemy_list)
        test_goblin = goblin(enemy_list)
        test_troll = troll(enemy_list)
        with self.assertRaises(ValueError):
            test_goblin.damage_taken(-5, 0)
        with self.assertRaises(ValueError):
            test_goblin.damage_taken(50, -10)    
        with self.assertRaises(ValueError):
            test_goblin.damage_taken(0, -20)
        with self.assertRaises(ValueError):
            test_troll.damage_taken(0, -10)
        with self.assertRaises(ValueError):
            test_troll.damage_taken(-10, 0)
        with self.assertRaises(ValueError):
            test_troll.damage_taken(50, -20)
        test_orc = orc(enemy_list, orc_num)
        with self.assertRaises(ValueError):
            test_orc.damage_taken(-5, 0)
        with self.assertRaises(ValueError):
            test_orc.damage_taken(50, -5)
        with self.assertRaises(ValueError):
            test_orc.damage_taken(0, -43)
        # type errors/ input checks?
        # check value error through info method for orc killed by survival

    def test_mage(self):
        list_test = []
        orc_list = []
        test_mage = mage("test_mage")
        test_goblin = goblin(list_test)
        test_troll = troll(list_test)
        test_orc = orc(list_test, orc_list)
        test_orc2 = orc(list_test, orc_list)
        test_troll2 = troll(list_test)
        self.assertEqual(test_mage.information(), "You have 50 health and 20 armour remaining")
        self.assertEqual(test_mage.magic_attack(), (100,20))
        self.assertEqual(test_troll2.damage_taken(25,10), (50,40))
        self.assertEqual(test_mage.splash_damage_attack(list_test), (0,0))
        self.assertEqual(test_troll.information(list_test, orc_list), "The troll has 35 health and 40 armour remaining")
        self.assertEqual(test_goblin.information(list_test, orc_list), "The goblin is dead")
        self.assertEqual(test_orc.information(list_test, orc_list), "The orc has 10 health and 40 armour remaining")
        self.assertEqual(test_orc2.information(list_test, orc_list), "The orc has 10 health and 40 armour remaining")
        self.assertEqual(test_troll2.information(list_test, orc_list), "The troll has 10 health and 30 armour remaining")
        self.assertEqual(test_mage.information(), "You have 50 health and 20 armour remaining")
        self.assertEqual(test_mage.damage_taken(25,10), (18.75,10))
        self.assertEqual(test_mage.information(), "You have 18.75 health and 10 armour remaining")
        self.assertEqual(test_mage.damage_taken(5,15), (7.5,0))
        test_mage2 = mage("mage_two")
        self.assertEqual(test_mage2.damage_taken(0,15),(50,5))
        self.assertEqual(test_mage2.information(), "You have 50.0 health and 5 armour remaining")
        self.assertEqual(test_mage2.damage_taken(0,55), "Game Over")
        self.assertEqual(test_mage2.attack_choice("1", list_test), test_mage.magic_attack())
        self.assertEqual(test_mage2.attack_choice("2", list_test), test_mage.splash_damage_attack(list_test))
        self.assertEqual(test_mage2.attack_choice("3", list_test), test_mage.attack_information())

    def test_goblin(self): 
        enemy_list = []
        orc_list = []
        test_goblin = goblin(enemy_list)
        self.assertEqual(test_goblin.information(enemy_list, orc_list), 'The goblin has 25 health remaining')
        self.assertEqual(test_goblin.attack(), (25,0))
        self.assertEqual(test_goblin.damage_taken(30,0), 0)
        test_goblin = goblin(enemy_list)
        self.assertEqual(test_goblin.damage_taken(10,5), 10)
        self.assertEqual(test_goblin.information(enemy_list, orc_list), 'The goblin has 10 health remaining')
        self.assertEqual(test_goblin.damage_taken(10,0), 0) 
        test_goblin = goblin(enemy_list)
        self.assertEqual(test_goblin.damage_taken(0,25), 0) 
        
    def test_troll(self):  
        enemy_list = []
        orc_list = []
        test_troll = troll(enemy_list)
        self.assertEqual(test_troll.damage_taken(50, 10), (25, 40))
        for j in range(1,13):
            if test_troll.health < 30:
                if j < 7:
                    self.assertEqual(test_troll.attack_choice(j, orc_list, enemy_list), test_troll.main_attack())
                else:
                    self.assertEqual(test_troll.attack_choice(j, orc_list, enemy_list), test_troll.close_to_death())
        self.assertEqual(test_troll.main_attack(), (30, 25))
        self.assertEqual(test_troll.information(enemy_list, orc_list), 'The troll has 25 health and 40 armour remaining')
        self.assertEqual(test_troll.damage_taken(0, 50), (15, 0))
        self.assertEqual(test_troll.damage_taken(0, 15), 0)
        test_troll = troll(enemy_list)        
        self.assertEqual(test_troll.damage_taken(75,0), 0)
        test_troll = troll(enemy_list) 
        self.assertEqual(test_troll.damage_taken(30, 50), (45, 0))
        self.assertEqual(test_troll.damage_taken(25,0), (20, 0))
    
    def test_interactions(self):
        enemy_list = []
        list_of_orcs = []
        test_soldier = soldier("soldier")
        test_mage = mage("mage")
        test_goblin = goblin(enemy_list)
        test_troll = troll(enemy_list)
        test_orc = orc(enemy_list, list_of_orcs)
        self.assertEqual(test_soldier.damage_taken(test_goblin.attack()[0], test_goblin.attack()[1]), (75,50))
        self.assertEqual(test_troll.damage_taken(test_soldier.power_attack()[0], test_soldier.power_attack()[1]), (40,25))
        self.assertEqual(test_mage.damage_taken(test_orc.main_attack()[0],test_orc.main_attack()[1]), (6.25,5))
        test_mage = mage("mage_two")
        second_troll = troll(enemy_list)
        self.assertEqual(test_mage.splash_damage_attack(enemy_list), (0,0))
        self.assertEqual(test_orc.information(enemy_list, list_of_orcs), 'The orc has 10 health and 40 armour remaining')
        self.assertEqual(test_goblin.information(enemy_list, list_of_orcs), "The goblin is dead")
        self.assertEqual(second_troll.information(enemy_list, list_of_orcs), 'The troll has 35 health and 40 armour remaining')
        # more tests
    
    def test_orc(self):
        enemy_list = []
        orcs = []
        test_orc = orc(enemy_list, orcs)
        other_orc = orc(enemy_list, orcs)
        for k in range(1,13):
            if k > 9:
                with self.subTest():
                    self.assertEqual(test_orc.attack_choice(k, orcs, enemy_list), 'The orc is dead')
                    other_orc = orc(enemy_list, orcs)
                    # the above test prints a statement
            else:
                self.assertEqual(test_orc.attack_choice(k, orcs, enemy_list), test_orc.main_attack())
        self.assertEqual(test_orc.main_attack(), (35, 15))
        self.assertEqual(test_orc.survival_of_the_fittest(orcs, enemy_list), 'The orc is dead')
        # the above test prints a statement
        self.assertEqual(test_orc.information(enemy_list,orcs), 'The orc has 50 health and 50 armour remaining')
        self.assertEqual(test_orc.damage_taken(25, 25), (25, 25))
        self.assertEqual(test_orc.damage_taken(0, 25), (25, 0))
        self.assertEqual(test_orc.damage_taken(0, 25), 0)
        test_orc = orc(enemy_list, orcs)
        self.assertEqual(test_orc.damage_taken(50, 0), 0)
        test_orc = orc(enemy_list, orcs)
        self.assertEqual(test_orc.damage_taken(40, 20), (10,30))
        self.assertEqual(test_orc.damage_taken(30, 30), 0)

if __name__=='__main__':
	unittest.main()