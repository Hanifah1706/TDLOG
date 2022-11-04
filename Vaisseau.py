from Exception import DestroyedError
from Exception import OutOfRangeError
from Weapon import *
from math import sqrt

class Vessel:# classe mère

    def __init__(self, coordinates: tuple, max_hits: int, weapon: Weapon):

        self.coordinates = coordinates
        self.max_hits = max_hits
        self.weapon = weapon

    def go_to(self, x, y, z):
        try:
            self.coordinates = (x, y, z)
            if x > 100 or y > 100 or x < 0 or y < 0 or z not in [1, 0, -1]:
                raise OutOfRangeError("Impossible de ce déplacer à cette position")
            if self.max_hits <= 0:
                raise DestroyedError("le destroyer détruis")
        except DestroyedError:
            print(" le navire est détruis, il ne peut donc se deplacer ")
        except OutOfRangeError:
            print(" Le navire ne peut se déplacer à cette position")
    def get_coordinates(self):

        print("les coordonnées actuelles du navire sont : {0}".format(self.coordinates))

    def fire_at(self, x, y, z):
        try:
            self.weapon.fire_at(x, y, z)# on utilise la fonction fire_at de la classe weapon déjà définie
            if self.max_hits <= 0:
                raise DestroyedError("le destroyer détruis")
            if distance(self.coordinates,(x,y,z))>self.weapon.range:
                raise OutOfRangeError("Distance hors d'atteinte!")
        except DestroyedError:
            print(" le navire est détruis, il ne peut donc tirer ")
        except OutOfRangeError:
            print("La cible est hors d'atteinte! Veuillez vous rapprocher")
            self.weapon.fire_at(x, y, z)

def distance(A : tuple , B : tuple):
    d=sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2 + (A[2]-B[2])**2)
    return d