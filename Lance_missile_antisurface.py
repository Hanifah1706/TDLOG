from Weapon import Weapon
from Exception import OutOfRangeError



class Lance_missile_antisurface(Weapon):
    def __init__(self, ammunitions: abs, range: int):
        super().__init__(ammunitions, range)
        self.ammunitions = 40
        self.range = 30

    def fire_at(self, x: int, y: int, z: int):
        super().fire_at(self, x, y, z)
        if self.z != 0:
            raise OutOfRangeError("la cible n'est pas admissible")
        else:
            print("cible atteignable")


A=Lance_missile_antisurface(23, 3)
print(A.fire_at(1,2,2))








