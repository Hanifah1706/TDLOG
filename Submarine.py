from Vaisseau import Vessel
#from arme import lance_tropille

class V2(Vessel):
    def __init__(self, coordinates, max_hits, weapon):
        super().__init__(coordinates, max_hits, weapon)
        self.max_hits = 2
        #self.armement = lance_tropille

    def go_to(self, x, y, z):
        if self.coordinates == (x, y, -1) or self.coordinates == (x, y, 0):
            print( " Le vaisseau se deplace")
        else:
            print("Le deplacement n'est pas possible")



    def fire_at(self, x, y, z):
        if self.max_hits == 0:
            print( " DestroyedError")
            

