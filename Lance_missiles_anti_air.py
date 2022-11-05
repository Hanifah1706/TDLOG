from Weapon import Weapon
from Exception import OutOfRangeError
class Lance_missiles_anti_air(Weapon):
    def __init__(self):
        super().__init__( ammunitions=50, range=40)


    def fire_at(self, x: int, y: int, z: int):
        self.z=z
        if self.z<0 or self.z== 0 :
            super().fire_at(x,y,z)# On fait appel à cette méthode pour dimunier les ammunitions
            raise OutOfRangeError ("hors de la zone de tir!")
        else:
            print("tir autorisé ")
