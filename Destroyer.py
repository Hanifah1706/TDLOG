from Vaisseau import Vessel

class Destroyer(Vessel):
    def __init__(self, coordinates, weapon):
        Vessel.__init__(self, coordinates, weapon)
        self.max_hits=4

    def go_to(self,x,y,z):
        try:
            self.coordinates = (x, y, z)
            assert z==0
        except AssertionError:
            print("le deplacement n'est possible que pour z=0")



