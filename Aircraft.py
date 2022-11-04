from Vaisseau import Vesssel
from Weapon import weapon
class aircraft(Vessel):
    def __init__(self,coordinates, max_hits, weapon):
        super().__init__(coordinates)
        self.max_hits = 1
        self.weapon= lance-missile_antisurface
    def go_to(self,x,y,z):
        if self.coordinates != (x, y, 1):
            print("impossible")
        else:
            print("go!!")

    def fire_at(self,x,y,z):
        if self.max_hits ==0:
            print("DestroyedError")
        if self.range<= self.z:
            print("OutOfRangeError")
            ammunitions = ammunitions-1