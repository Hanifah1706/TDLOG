class aircraft(Vessel):
    def __init__(self,coordinates,max_hits,weapon):
        super().__init__(coordinates,weapon)
        self.max_hits = 1
    def go_to(self,x,y,z):
        if self.coordinates != (x,y,1):
            print("impossible")
        else:
            print("go!!")

    def fire_at(self,x,y,z):
        if self.max_hits ==0:
            raise DestroyedError
        if self.range<= self.z:
            raise OutOfRangeError
            ammunitions=ammunitions-1
