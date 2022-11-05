from Vaisseau import Vessel
from Exception import OutOfRangeError
from Lance_torpilles import Lances_torpilles
class Destroyer(Vessel):
    def __init__(self, coordinates):
        Vessel.__init__(self,coordinates, max_hits=4,weapon=Lances_torpilles())
        if self.coordinates[2]!=0:
            raise OutOfRangeError ("Deplacement non autorisé tant que z n'est pas égal à 0")

    def go_to(self,x,y,z):
        self.z=z
        if self.z== 0 :
            super().go_to(x,y,z)
            print ("Deplacement autorisé")
        else:
            raise OutOfRangeError ("Déplacement non autorisé, revenir à z=0")




