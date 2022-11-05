from Vaisseau import Vessel
from Lance_missiles_anti_air import Lance_missiles_anti_air#mets tes fichiers à jour
from Exception import OutOfRangeError

class Cruiser(Vessel):
    def __init__(self, coordinates):
        #super().__init__(self, coordinates, max_hits, weapon )
        Vessel.__init__(self, coordinates, max_hits= 6, weapon= Lance_missiles_anti_air())
        if self.coordinates[2] != 0:
            raise OutOfRangeError("Ne prend que les coordonnées z= 0")


    def go_to(self, x, y, z):
        if z == 0:
            super().go_to(x, y, z)
            print(" Le vaisseau se déplace")

        else:
            raise OutOfRangeError("Pas de déplacement du vaisseau")
            print("le déplacement n'est pas possible")

