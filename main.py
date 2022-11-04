from Vaisseau import *
from Weapon import *

"""
Arme=Weapon(50,50)
Bateau=Vessel((1, 1, 1), 6, Arme)
Bateau.fire_at(100,1,1)
Arme=Weapon(0,50)
Bateau1=Vessel((1, 1, 1), 6, Arme)
Bateau1.fire_at(10,1,1)"""
Arme=Weapon(50,50)
A=Vessel((1,1,1), "a", 10)
print(A.coordinates)
A.go_to(1,2,2)
print(A.coordinates)

