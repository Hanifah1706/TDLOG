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
        if self.z <=0:
           print("cible atteignable")
        else:
            super().fire_at(x, y, z)# On fait appel à cette méthode pour dimunier les ammunitions
            raise OutOfRangeError("cible inatteignable")



