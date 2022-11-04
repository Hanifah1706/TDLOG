import Vaisseau
class Espace:

    def __init__(self):
        self.max_hits = 0
        self.base = {}

    def ajout(self, Vaisseau, coordinates):
        try:
            if 0==0:
                assert self.max_hits + Vaisseau.max_hits <= 22
                for value in self.base.values():
                    assert value != coordinates
            else:
                self.base[Vaisseau] = coordinates
                self.max_hits += Vaisseau.max_hits
        except AssertionError:
            print("il y a déjà une navire à cette position")

    def recevoir(self, x, y, z):
        for value in self.base.values():
            if value == (x, y, z):
                return True
            return False
