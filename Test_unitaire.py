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
D=Cruiser((1,1,0))
E=Submarine((1,2,-1))
F=Fregate((1, 3, 0))
G= Destroyer((0,1,0))
I= Aircraft((2,3,1))

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
            B.fire_at(1, 1, 1)  # Lorsque z!=0 on doit avoir d'erreur. Donc ce test doit être positif

    def test_5(self):
        with self.assertRaises(OutOfRangeError):
            C.fire_at(1, 1, 0)  # Lorsque z<=0 on doit pas avoir d'erreur. Donc ce test doit être negatif

    def test_6(self):
        with self.assertRaises(OutOfRangeError):
            C.fire_at(1, 1, 1)  # Lorsque z>0 on doit  avoir une erreur. Donc ce test doit être positif
        pass
    def test_7(self):
        with self.assertRaises(OutOfRangeError):
            D.go_to(1, 1, 1)# ne peut pas atteindre ce point car z !=0 .Donc le test est positif

    def test_8(self):
        with self.assertRaises(OutOfRangeError):
            D.go_to(1, 1, 0)#  peut  atteindre ce point car z =0 .Donc le test est négatif
    def test_9(self):
        with self.assertRaises(OutOfRangeError):
            E.go_to(1, 1, 0)#  peut  atteindre ce point car z =0 .Donc le test est négatif

    def test_10(self):
        with self.assertRaises(OutOfRangeError):
            E.go_to(1, 1, 1)# ne peut pas atteindre ce point car z !=0 et z!=-1 .Donc le test est positif

    def test_11(self):
        with self.assertRaises(OutOfRangeError):
            F.go_to(1, 1, 1)# ne peut pas atteindre ce point car z !=0  .Donc le test est positif

    def test_12(self):
        with self.assertRaises(OutOfRangeError):
            F.go_to(1, 1, 0)# peut  atteindre ce point car z =0  .Donc le test est negatif

    def test_13(self):
        with self.assertRaises(OutOfRangeError):
            G.go_to(1, 1, 1)  # ne peut pas atteindre ce point car z !=0  .Donc le test est positif

    def test_14(self):
        with self.assertRaises(OutOfRangeError):
            G.go_to(1, 1, 0)  # peut  atteindre ce point car z =0  .Donc le test est negatif

    def test_15(self):
        with self.assertRaises(OutOfRangeError):
            I.go_to(1, 1, -1)  # ne peut pas atteindre ce point car z !=1  .Donc le test est positif

    def test_16(self):
        with self.assertRaises(OutOfRangeError):
            I.go_to(1, 1, 1)  # peut  atteindre ce point car z =1  .Donc le test est negatif
if __name__ == '__main__':
    unittest.main()