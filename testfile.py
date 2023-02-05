import unittest
from adventure_game import *

class Testclasses(unittest.TestCase):
    def test_soldier(self):
        test_soldier = soldier()
        self.assertEqual(test_soldier.quick_attack(), 40)
        self.assertEqual(test_soldier.power_attack(), (25,25))
        self.assertEqual(test_soldier.information(), (100,50))
        self.assertEqual(test_soldier.damage_taken(30, 0), (70,50))
        self.assertEqual(test_soldier.information(), (70,50))
        self.assertEqual(test_soldier.damage_taken(70, 0), "Game Over")
        test_soldier = soldier()
        self.assertEqual(test_soldier.damage_taken(0, 20), (100,30))
        self.assertEqual(test_soldier.damage_taken(0, 50), (80,0))
        self.assertEqual(test_soldier.information(), (80,0))
        self.assertEqual(test_soldier.damage_taken(0, 80), "Game Over")
    
    def test_input(self):
        test_soldier = soldier()
        test_mage = mage()
        test_goblin = goblin()
        test_troll = troll()
        with self.assertRaises(ValueError):
            test_soldier.damage_taken(-10, 0)
        with self.assertRaises(ValueError):
            test_mage.damage_taken(-20, 0)
        with self.assertRaises(ValueError):
            test_mage.splash_damage_attack(0)
        with self.assertRaises(ValueError):
            test_mage.splash_damage_attack(-1)
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
        # type errors/ input checks?

    def test_mage(self):
        test_mage = mage()
        self.assertEqual(test_mage.information(), (50,20))
        self.assertEqual(test_mage.magic_attack(), (100,20))
        self.assertEqual(test_mage.splash_damage_attack(3), (120,30))
        self.assertEqual(test_mage.splash_damage_attack(10), (400,100))
        self.assertEqual(test_mage.information(), (50, 20))
        self.assertEqual(test_mage.damage_taken(25,10), (12.5,10))
        self.assertEqual(test_mage.information(), (12.5, 10))
        self.assertEqual(test_mage.damage_taken(5,15), "Game Over")
        test_mage = mage()
        self.assertEqual(test_mage.damage_taken(0,15),(50,5))
        self.assertEqual(test_mage.information(), (50,5))
        self.assertEqual(test_mage.damage_taken(0,55), "Game Over")

    def test_goblin(self):    
        test_goblin = goblin()
        self.assertEqual(test_goblin.information(), 25)
        self.assertEqual(test_goblin.attack(), 25)
        self.assertEqual(test_goblin.damage_taken(30,0), "Game Over")
        test_goblin = goblin()
        self.assertEqual(test_goblin.damage_taken(10,5), 10)
        self.assertEqual(test_goblin.information(), 10)
        self.assertEqual(test_goblin.damage_taken(10,0), "Game Over") 
        test_goblin = goblin()
        self.assertEqual(test_goblin.damage_taken(0,25), "Game Over") 
        
    def test_troll(self):  
        test_troll = troll()
        self.assertEqual(test_troll.main_attack(), (30, 25))
        self.assertEqual(test_troll.information(), (75,50))
        self.assertEqual(test_troll.damage_taken(50, 10), (25, 40))
        self.assertEqual(test_troll.damage_taken(0, 50), (15, 0))
        self.assertEqual(test_troll.damage_taken(0, 15), "Game Over")
        test_troll = troll()        
        self.assertEqual(test_troll.damage_taken(75,0), "Game Over")
        test_troll = troll() 
        self.assertEqual(test_troll.damage_taken(30, 50), (45, 0))
        self.assertEqual(test_troll.damage_taken(25,0), (20, 0))

if __name__=='__main__':
	unittest.main()