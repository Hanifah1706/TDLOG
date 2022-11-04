from Weapon import Weapon
from Exception import OutOfRangeError
class Lance_missiles_anti_air(Weapon):
    def __init__(self):
        #super().__init__(self, ammunitions, range)

        self.range = 40
        self.ammunitions = 50

    def fire_at(self, x: int, y: int, z: int):
        if z<= 0 :
            super().fire_at(self,x,y,z)
            raise OutOfRangeError
            print("hors de la zone de tir!")
        else:
            print("tir autorisé ")
