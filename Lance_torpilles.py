from Exception import OutOfRangeError
from Weapon import Weapon
import unittest
class Lances_torpilles(Weapon):
    def __init__(self):
         super().__init__(ammunitions=15,range=20)
         #self.range = 20
         #self.ammunitions = 15
    def fire_at(self, x:int, y:int, z:int):
        self.z=z
        super().fire_at(x, y, z)
        if self.z <=0:
           print("cible atteignable")
        else:
            raise OutOfRangeError("cible inatteignable")



A=Lances_torpilles()
A.fire_at(1,1,-1)
