from Vaisseau import Vessel
from Weapon import Weapon
#from arme import lance_tropille

class Submarine(Vessel, Weapon):
    def __init__(self, coordinates, max_hits, weapon,x, y,z, ammunitions, range):
        Vessel.__init__(coordinates, max_hits, weapon)
        Weapon.__init__(x, y, z, ammunitions, range)
        self.max_hits = 2
        self.ammunitions =15
        self.range = 20

        #self.armement = lance_tropille

    def go_to(self, x, y, z):
        if self.coordinates == (x, y, -1) or self.coordinates == (x, y, 0):
            print( " Le vaisseau se deplace")
        else:
            print("Le deplacement n'est pas possible")



    def fire_at(self, x, y, z):
        if self.max_hits == 0:
            print( " DestroyedError")



