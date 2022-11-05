from Aircraft import *
from Cruiser import *
from Destroyer import *
from Espace import *
from Exception import *
from Fregate import *
from Lance_missile_antisurface import *
from Lance_missiles_anti_air import *
from Lance_torpilles import *
from Submarine import *
from Vaisseau import *
from Weapon import *

import unittest

A = Lance_missiles_anti_air()
B= Lance_missile_antisurface()
C= Lances_torpilles()
class MyTestCase(unittest.TestCase):
    def test_1(self):
        with self.assertRaises(OutOfRangeError):
            A.fire_at(1,1,1)# Lorsque z> 0 on doit pas avoir d'erreur . Donc ce test doit échoué
    def test_2(self):
        with self.assertRaises(OutOfRangeError):
            A.fire_at(1,1,0)# Lorsque z<= 0 on doit avoir erreur . Donc ce test doit reussir

    def test_3(self):
        with self.assertRaises(OutOfRangeError):
            B.fire_at(1,1,0)# Lorsque z=0 on doit pas avoir d'erreur. Donc ce test doit être negatif

    def test_4(self):
        with self.assertRaises(OutOfRangeError):
            B.fire_at(1, 1, 0)  # Lorsque z!=0 on doit avoir d'erreur. Donc ce test doit être positif

    def test_5(self):
        with self.assertRaises(OutOfRangeError):
            C.fire_at(1, 1, 0)  # Lorsque z<=0 on doit pas avoir d'erreur. Donc ce test doit être negatif

    def test_6(self):
        with self.assertRaises(OutOfRangeError):
            C.fire_at(1, 1, 1)  # Lorsque z>0 on doit  avoir une erreur. Donc ce test doit être positif
        pass
    def test_2(self):
        pass
    def test_2(self):
        pass"""
if __name__ == '__main__':
    unittest.main()