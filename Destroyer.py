from Vaisseau import Vessel
import Lance_missiles_anti_air
#import Lance_Torpille as lt
class Destroyer(Vessel):
    def __init__(self, coordinates):
        Vessel.__init__(coordinates, max_hits=4,weapon=Lance_missiles_anti_air())
        if self.coordinates
        #self.weapon=lt.Lance_torpilles

    def go_to(self,x,y,z):
        try:
            self.coordinates = (x, y, z)
            assert z==0
        except AssertionError:
            print("le deplacement n'est possible que pour z=0")
Bateau= Destroyer((3,4,5))
Bateau.go_to((3,4,5))



