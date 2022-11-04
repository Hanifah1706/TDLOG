from Vaisseau import *
from Weapon import *

Arme=Weapon(50,50)
Bateau=Vessel((1, 1, 1), 6, Arme)
Bateau.fire_at(100,1,1)
