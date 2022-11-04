from Exception import OutOfRangeError, DestroyedError
from Vaisseau import Vessel, distance
from Weapon import Weapon


class Fregate(Vessel, Weapon):
    def __init__(self, coordinates, max_hits, weapon, ammunitions, range, x=int, y=int, z=int):
        Vessel.__init__(self, coordinates, max_hits, weapon)
        Weapon.__init__(self, ammunitions, range)
        self.coordinates = (x, y, z)
        self.weapon = "lance_missile_anti-surface"
        self.max_hits = 5

    def go_to(self, x, y, z):
        try:
            self.coordinates = (x, y, 0)
        except OutOfRangeError("vous ne pouvez pas vous deplacez dans cette zone"):
            print("Rester dans votre zone")

    def fire_at(self, x, y, z=0):
        try:
            self.max_hits != 0

        except DestroyedError:
            print("Votre vaisseau est détruit; vous ne pouvez ni tirer, ni vous déplacer")
        if distance(self.coordinates, (x, y, 0)) > self.weapon.range:
            raise OutOfRangeError
