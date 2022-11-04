from Exception import NoAmmunitionError


class Weapon:
    def __init__(self, ammunitions: abs, range: int):

        self.ammunitions = ammunitions
        self.range = range

    def fire_at(self, x: int, y: int, z: int):
        if not self.ammunitions != 0:
            raise NoAmmunitionError(self.ammunitions)
        if self.ammunitions != 0:
            self.ammunitions = self.ammunitions - 1



