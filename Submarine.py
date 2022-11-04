from Vaisseau import Vessel


class Submarine(Vessel):
    def __init__(self, coordinates, max_hits, weapon):
        Vessel.__init__(coordinates, max_hits, weapon)
        self.max_hits = 2
        self.ammunitions =15
        self.range = 20



    def go_to(self, x, y, z):
        if self.coordinates == (x, y, -1) or self.coordinates == (x, y, 0):
            self.go_to(x,y,z)
            print( " Le vaisseau se deplace")
        else:
            raise OutOfRangeError
            print("Le deplacement n'est pas possible")



   # def fire_at(self, x, y, z):
    #    self.weapon.fire_at(x, y, z)
    #   if self.max_hits == 0:
    #        print( " DestroyedError")

    #    while d > self.range :
    #        print("OutOfRangeError")
    #        self.ammunitions -= 1



