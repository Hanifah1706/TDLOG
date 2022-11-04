from Weapon import Weapon
class Lance_missiles_anti_air(Weapon):
    def __init__(self, x:int, y:int, z:int):
        self.range = 40
        self.ammunitions = 50
        
    def fire_at(self, x: int, y: int, z: int):
        if self.z<= 0 :
            raise OutOfRangeError


