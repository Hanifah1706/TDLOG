from Vaisseau import Vessel
from Lance_missile_antisurface import Lance_missile_antisurface
from Exception import OutOfRangeError
class Aircraft(Vessel):
    def __init__(self, coordinates):
        Vessel.__init__(self, coordinates, max_hits= 1, weapon=Lance_missile_antisurface)
        if self.coordinates[3] != 1:
            raise OutOfRangeError("Ne prend que la coordonnée z=1")
    def go_to(self,x,y,z):
        if z == 1:
            super().go_to(x,y,z)
            print("le vaisseau se deplace")
        else:
            raise OutOfRangeError("Pas de déplacement du vaisseau")
            print("Le déplacement n'est pas possible")




