from Exception import OutOfRangeError
from Weapon import Weapon

class lances_torpilles(Weapon):
    def __init__(self,):
         super().__init__()
         self.range = 20
         self.ammunitions = 15
    def fire_at(self, x:int, y:int, z:int):
        super().fire_at(x, y, z)
        if self.z <=0:
           print("cible atteignable")
        else:
            raise OutOfRangeError("cible inatteignable")



