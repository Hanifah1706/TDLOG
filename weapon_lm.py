class lances_torpilles(Weapon):
    def __init__(self,ammunitions,range):
         self.range = 20
         self.ammunitions = 15
    def fire_at(self,x,y,z):
        if self.ammunitions==0:
            raise NoAmminitionError
        if self.z <=0:
            raise OutOfRangeError