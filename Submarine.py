from Vaisseau import Vessel
from Exception import OutOfRangeError
from Lance_torpilles import Lances_torpilles

class Submarine(Vessel):
    def __init__(self, coordinates):
        Vessel.__init__(self, coordinates, max_hits= 2, weapon=Lances_torpilles())
        if self.coordinates[2] not in [-1,0]:
            raise OutOfRangeError("Ne prend que les coordonnées z=0 ou -1")




    def go_to(self, x, y,z):

        if z == -1 or z == 0:
            super().go_to(x, y, z)
            print(" Le vaisseau se deplace")
        else:
            raise OutOfRangeError("Pas de déplacement du vaisseau")
            print("Le deplacement n'est pas possible")





A= Submarine((1, 2, 0))
#print(A.coordinates)
#A.go_to(2,2,-1)
A.fire_at(1,2,2)
#rint(A.coordinates)
#print(A.max_hits)





