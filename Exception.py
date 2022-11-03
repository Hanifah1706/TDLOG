class NoAmmunitionError(Exception):
    def __init__(self, ammunitions, message="la reserve de munition est vide"):
        self.ammunitions = ammunitions
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.ammunitions} -> {self.message}'


class OutOfRangeError(Exception):
    def __init__(self, ammunitions, z: int, message="la côte z n'est pas valide pour cette arme"):
        self.ammunitions = ammunitions
        self.z = z
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.z} -> {self.message}'



class DestroyedError(Exception):


    def __init__(self, message):
        self.message = message


    def __str__(self):
        return self.message