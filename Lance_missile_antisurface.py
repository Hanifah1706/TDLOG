from Weapon import Weapon
class Lance_missile_antisurface(Weapon):

    def __init__(self, x: int, y: int, z: int, ammunitions: int, range: int):
        super().__init__(x: int, y: int, z: int, ammunitions: int, range: int)
        self.z = 0

    def fire_at(self, x:float, y:float, z:float):

