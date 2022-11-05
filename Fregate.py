from Exception import OutOfRangeError
from Vaisseau import Vessel
from Lance_missile_antisurface import Lance_missile_antisurface


class Fregate(Vessel):
    def __init__(self, coordinates):
        Vessel.__init__(self, coordinates, max_hits=5, weapon=Lance_missile_antisurface())
        self.coordinates = coordinates
        if self.coordinates[2] != 0:
            raise OutOfRangeError("Ce navire ne se déplace qu'à la surface !, donc z doit être égale à 0")

    def go_to(self, x, y, z):
        if z == 0:
            super().go_to(x, y, z)
            print(" Le vaisseau se deplace")
        else:
            raise OutOfRangeError("vous ne pouvez pas vous deplacez dans cette zone")

    def fire_at(self, x, y, z):
        super().fire_at(x, y, z)
