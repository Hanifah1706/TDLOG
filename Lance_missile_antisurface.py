from Weapon import Weapon
from Exception import OutOfRangeError



class Lance_missile_antisurface(Weapon):
    def __init__(self):
        super().__init__(ammunitions=40, range=30)

    def fire_at(self, x: int, y: int, z: int):
        if z != 0:
            super().fire_at(x, y, z)# On fait appel à cette méthode pour dimunier les ammunitions
            raise OutOfRangeError("la cible n'est pas admissible")
        else:
            print("la cible est atteignable")












