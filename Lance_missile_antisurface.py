from Weapon import Weapon
from Exception import OutOfRangeError



class Lance_missile_antisurface(Weapon):
    def __init__(self, ammunitions: abs, range: int):
        super().__init__(ammunitions, range)
        self.ammunitions = 40
        self.range = 30

    def fire_at(self, x: int, y: int, z: int):
        if self.z != 0:
            super().fire_at(x, y, z)
            raise OutOfRangeError("la cible n'est pas admissible")
        else:
            print("la cible est atteignable")












