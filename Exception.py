class NoAmmunitionError(Exception):
    def __init__(self, ammunitions, message="la reserve de munition est vide"):
        self.ammunitions = ammunitions
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.ammunitions} -> {self.message}'


class OutOfRangeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class DestroyedError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

