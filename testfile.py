import unittest
from adventure_game import *

class Testclasses(unittest.TestCase):

    def test_soldier(self):
        enemy_list = []
        test_soldier = soldier("test_soldier")
        self.assertEqual(test_soldier.power_attack(), (35,25))
        self.assertEqual(test_soldier.information(), "You have 100 health and 50 armour remaining")
        self.assertEqual(test_soldier.damage_taken(30, 0), (70,50))
        self.assertEqual(test_soldier.information(), "You have 70 health and 50 armour remaining")
        self.assertEqual(test_soldier.damage_taken(70, 0), "Game Over")
        test_soldier = soldier("test_soldier")
        self.assertEqual(test_soldier.damage_taken(0, 20), (100,30))
        self.assertEqual(test_soldier.damage_taken(0, 50), (80,0))
        self.assertEqual(test_soldier.information(), "You have 80 health and 0 armour remaining")
        self.assertEqual(test_soldier.damage_taken(0, 80), "Game Over")
        self.assertEqual(test_soldier.attack_choice("2", enemy_list), (test_soldier.power_attack()))
        self.assertEqual(test_soldier.attack_choice("3", enemy_list), (test_soldier.attack_information()))

    '''
    def test_quick_attack(self):
        test_soldier = soldier("test_player")
        with self.subTest():
            self.assertEqual(test_soldier.quick_attack(), (40,0))
        with self.subTest():
            self.assertEqual(test_soldier.quick_attack(), (80,0))
    '''
    
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
        test_goblin = goblin("test_goblin", enemy_list)
        test_troll = troll("test_troll", enemy_list)
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
        test_orc = orc("orc_one", enemy_list, orc_num)
        with self.assertRaises(ValueError):
            test_orc.damage_taken(-5, 0)
        with self.assertRaises(ValueError):
            test_orc.damage_taken(50, -5)
        with self.assertRaises(ValueError):
            test_orc.damage_taken(0, -43)
        # type errors/ input checks?

    def test_mage(self):
        list_test = []
        test_mage = mage("test_mage")
        test_goblin = goblin("goblin", list_test)
        test_troll = troll("troll", list_test)
        self.assertEqual(test_mage.information(), "You have 50 health and 20 armour remaining")
        self.assertEqual(test_mage.magic_attack(), (100,20))
        self.assertEqual(test_mage.splash_damage_attack(list_test), (0,0))
        self.assertEqual(test_mage.information(), "You have 50 health and 20 armour remaining")
        self.assertEqual(test_mage.damage_taken(25,10), (12.5,10))
        self.assertEqual(test_mage.information(), "You have 12.5 health and 10 armour remaining")
        self.assertEqual(test_mage.damage_taken(5,15), "Game Over")
        test_mage = mage("mage_two")
        self.assertEqual(test_mage.damage_taken(0,15),(50,5))
        self.assertEqual(test_mage.information(), "You have 50.0 health and 5 armour remaining")
        self.assertEqual(test_mage.damage_taken(0,55), "Game Over")
        self.assertEqual(test_mage.attack_choice("1", list_test), test_mage.magic_attack())
        self.assertEqual(test_mage.attack_choice("2", list_test), test_mage.splash_damage_attack(list_test))
        self.assertEqual(test_mage.attack_choice("3", list_test), test_mage.attack_information())

    def test_goblin(self): 
        enemy_list = []
        test_goblin = goblin("test_goblin", enemy_list)
        self.assertEqual(test_goblin.information(enemy_list), 25)
        self.assertEqual(test_goblin.attack(), 25)
        self.assertEqual(test_goblin.damage_taken(30,0), 0)
        test_goblin = goblin("goblin_two", enemy_list)
        self.assertEqual(test_goblin.damage_taken(10,5), 10)
        self.assertEqual(test_goblin.information(enemy_list), 10)
        self.assertEqual(test_goblin.damage_taken(10,0), 0) 
        test_goblin = goblin("goblin_three", enemy_list)
        self.assertEqual(test_goblin.damage_taken(0,25), 0) 
        
    def test_troll(self):  
        enemy_list = []
        test_troll = troll("test_troll", enemy_list)
        self.assertEqual(test_troll.main_attack(), (30, 25))
        self.assertEqual(test_troll.information(enemy_list), (75,50))
        self.assertEqual(test_troll.damage_taken(50, 10), (25, 40))
        self.assertEqual(test_troll.damage_taken(0, 50), (15, 0))
        self.assertEqual(test_troll.damage_taken(0, 15), 0)
        test_troll = troll("troll_one", enemy_list)        
        self.assertEqual(test_troll.damage_taken(75,0), 0)
        test_troll = troll("troll_two", enemy_list) 
        self.assertEqual(test_troll.attack_choice(), test_troll.main_attack())
        self.assertEqual(test_troll.damage_taken(30, 50), (45, 0))
        self.assertEqual(test_troll.damage_taken(25,0), (20, 0))
    
    '''
    def test_multiple_outcomes(self):
        enemy_list = []
        test_troll = troll("test_troll", enemy_list)
        self.assertEqual(test_troll.damage_taken(50, 50), (25, 0))
        with self.subTest():
            self.assertEqual(test_troll.attack_choice(), test_troll.close_to_death())
        with self.subTest():
            self.assertEqual(test_troll.attack_choice(), test_troll.main_attack())
    '''
    
    def test_interactions(self):
        enemy_list = []
        list_of_orcs = []
        test_soldier = soldier("soldier")
        test_mage = mage("mage")
        test_goblin = goblin("goblin", enemy_list)
        test_troll = troll("troll", enemy_list)
        test_orc = orc("orc", enemy_list, list_of_orcs)
        self.assertEqual(test_soldier.damage_taken(test_goblin.attack()), (75,50))
        self.assertEqual(test_troll.damage_taken(test_soldier.power_attack()[0], test_soldier.power_attack()[1]), (40,25))
        self.assertEqual(test_mage.damage_taken(test_orc.main_attack()[0],test_orc.main_attack()[1]), 'Game Over')
        test_mage = mage("mage_two")
        second_troll = troll("troll", enemy_list)
        self.assertEqual(test_mage.splash_damage_attack(enemy_list), (0,0))
        self.assertEqual(test_orc.information(enemy_list, list_of_orcs), (10,40))
        self.assertEqual(test_goblin.information(enemy_list), "{} is dead".format(test_goblin.name))
        self.assertEqual(second_troll.information(enemy_list), (35,40))
        # more tests
    
    def test_orc(self):
        enemy_list = []
        orcs = []
        test_orc = orc("test_orc", enemy_list, orcs)
        other_orc = orc("other_orc", enemy_list, orcs)
        self.assertEqual(test_orc.main_attack(), (35, 15))
        self.assertEqual(test_orc.survival_of_the_fittest(orcs, enemy_list), "{} is dead".format(other_orc.name))
        # the above test prints a statement
        self.assertEqual(test_orc.information(enemy_list,orcs), (50,50))
        self.assertEqual(test_orc.damage_taken(25, 25), (25, 25))
        self.assertEqual(test_orc.damage_taken(0, 25), (25, 0))
        self.assertEqual(test_orc.damage_taken(0, 25), 0)
        test_orc = orc("orc_two", enemy_list, orcs)
        self.assertEqual(test_orc.damage_taken(50, 0), 0)
        test_orc = orc("orc_three", enemy_list, orcs)
        self.assertEqual(test_orc.damage_taken(40, 20), (10,30))
        self.assertEqual(test_orc.damage_taken(30, 30), 0)
    
    '''
    def test_multiple_outcomes(self):
        enemy_list = []
        orc_num = []
        test_orc = orc("test_orc", enemy_list, orc_num)
        second_orc = orc("second_orc", enemy_list, orc_num)
        with self.subTest():
            self.assertEqual(test_orc.attack_choice(orc_num, enemy_list), test_orc.main_attack())
        with self.subTest():
            self.assertEqual(test_orc.attack_choice(orc_num, enemy_list), test_orc.survival_of_the_fittest(orc_num, enemy_list))
    '''

if __name__=='__main__':
	unittest.main()