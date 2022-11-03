class Vessel:# classe mère

    def __init__(self, coordinates, max_hits, weapon):

        self.coordinates = coordinates
        self.max_hits = max_hits
        self.weapon = weapon

    def go_to(self, x, y, z):
        try:
            self.coordinates = (x, y, z)
            assert self.max_hits > 0
        except AssertionError:
            print(" le navire est détruis, il ne peut donc se deplacer ")

    def get_coordinates(self):

        print("les coordonnées actuelles du navire sont : {0}".format(self.coordinates))

    def fire_at(self, x, y, z):
        try:
            self.weapon.fire_at(x, y, z)  # on utilise la fonction fire_at de la classe weapon déjà définie
            assert self.max_hits > 0
        except AssertionError:
            print(" le navire est détruis, il ne peut donc tirer ")
