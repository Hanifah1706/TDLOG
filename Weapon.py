from Exception import NoAmmunitionError
from Exception import OutOfRangeError


class Weapon:
    def __init__(self, x: int, y: int, z: int, ammunitions: int, range: int):
        self.z = z
        self.y = y
        self.x = x
        self.ammunitions = ammunitions
        self.range = range

    def fire_at(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        if not self.ammunitions != 0:
            raise NoAmmunitionError
        if not self.z <= 0 or self.z > 0 or self.z == 0:
            raise OutOfRangeError
        self.ammunitions = self.ammunitions - 1








