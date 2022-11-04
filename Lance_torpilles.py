import unittest
from Weapon import weapon

class lances_torpilles(Weapon):
    def __init__(self):
         self.range = 20
         self.ammunitions = 15
    def fire_at(self,x,y,z):
        if self.z <=0:
           print("OutOfRangeError")


