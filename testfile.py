import unittest
from adventure_game import *

class Testclasses(unittest.TestCase):
    def test_soldier_attack_range(self):
        test_soldier = soldier("test_soldier")
        for i in range(1,13):
            with self.subTest(i=i):
                if i > 6:
                    self.assertEqual(test_soldier.quick_attack(i), (80,0))
                else:
                    self.assertEqual(test_soldier.quick_attack(i), (40,0))

    def test_soldier(self):
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
    
    def test_input(self):
        enemy_list = []
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
            test_goblin.damage_taken(enemy_list, -5, 0)
        with self.assertRaises(ValueError):
            test_goblin.damage_taken(enemy_list, 50, -10)    
        with self.assertRaises(ValueError):
            test_goblin.damage_taken(enemy_list, 0, -20)
        with self.assertRaises(ValueError):
            test_troll.damage_taken(enemy_list, 0, -10)
        with self.assertRaises(ValueError):
            test_troll.damage_taken(enemy_list, -10, 0)
        with self.assertRaises(ValueError):
            test_troll.damage_taken(enemy_list, 50, -20)
        test_orc = orc("orc_one", enemy_list)
        with self.assertRaises(ValueError):
            test_orc.damage_taken(enemy_list, -5, 0)
        with self.assertRaises(ValueError):
            test_orc.damage_taken(enemy_list, 50, -5)
        with self.assertRaises(ValueError):
            test_orc.damage_taken(enemy_list, 0, -43)
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

    def test_goblin(self): 
        enemy_list = []
        test_goblin = goblin("test_goblin", enemy_list)
        self.assertEqual(test_goblin.information(), 25)
        self.assertEqual(test_goblin.attack(), 25)
        self.assertEqual(test_goblin.damage_taken(enemy_list,30,0), 0)
        test_goblin = goblin("goblin_two", enemy_list)
        self.assertEqual(test_goblin.damage_taken(enemy_list,10,5), 10)
        self.assertEqual(test_goblin.information(), 10)
        self.assertEqual(test_goblin.damage_taken(enemy_list,10,0), 0) 
        test_goblin = goblin("goblin_three", enemy_list)
        self.assertEqual(test_goblin.damage_taken(enemy_list,0,25), 0) 
        
    def test_troll(self):  
        enemy_list = []
        test_troll = troll("test_troll", enemy_list)
        self.assertEqual(test_troll.main_attack(), (30, 25))
        self.assertEqual(test_troll.information(), (75,50))
        self.assertEqual(test_troll.damage_taken(enemy_list,50, 10), (25, 40))
        self.assertEqual(test_troll.damage_taken(enemy_list,0, 50), (15, 0))
        self.assertEqual(test_troll.damage_taken(enemy_list,0, 15), 0)
        test_troll = troll("troll_one", enemy_list)        
        self.assertEqual(test_troll.damage_taken(enemy_list,75,0), 0)
        test_troll = troll("troll_two", enemy_list) 
        self.assertEqual(test_troll.damage_taken(enemy_list,30, 50), (45, 0))
        self.assertEqual(test_troll.damage_taken(enemy_list,25,0), (20, 0))
    
    def test_interactions(self):
        enemy_list = []
        test_soldier = soldier("soldier")
        test_mage = mage("mage")
        test_goblin = goblin("goblin", enemy_list)
        test_troll = troll("troll", enemy_list)
        attack = test_goblin.attack()
        self.assertEqual(test_soldier.damage_taken(attack), (75,50))
        # add more
    
    def test_orc(self):
        enemy_list = []
        test_orc = orc("test_orc", enemy_list)
        other_orc = orc("other_orc", enemy_list)
        self.assertEqual(test_orc.main_attack(), (35, 15))
        self.assertEqual(test_orc.survival_of_the_fittest(other_orc, enemy_list), "Infighting has broken out between the orcs and {} has killed his brother".format(test_orc.name))
        self.assertEqual(test_orc.information(), (50,50))
        self.assertEqual(test_orc.damage_taken(enemy_list, 25, 25), (25, 25))
        self.assertEqual(test_orc.damage_taken(enemy_list, 0, 25), (25, 0))
        self.assertEqual(test_orc.damage_taken(enemy_list, 0, 25), 0)
        test_orc = orc("orc_two", enemy_list)
        self.assertEqual(test_orc.damage_taken(enemy_list, 50, 0), 0)
        test_orc = orc("orc_three", enemy_list)
        self.assertEqual(test_orc.damage_taken(enemy_list, 40, 20), (10,30))
        self.assertEqual(test_orc.damage_taken(enemy_list, 30, 30), 0)

if __name__=='__main__':
	unittest.main()