from Vaisseau import Vessel
#import Lance_Torpille as lt
class Destroyer(Vessel):
    def __init__(self, coordinates):
        Vessel.__init__(self, coordinates)
        self.max_hits=4
        #self.weapon=lt.Lance_torpilles

    def go_to(self,x,y,z):
        try:
            self.coordinates = (x, y, z)
            assert z==0
        except AssertionError:
            print("le deplacement n'est possible que pour z=0")



