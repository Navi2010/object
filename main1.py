class vehicle:
    def __init__(self, speed, mileage):
        self.x = speed
        self.y = mileage

ob = vehicle(240, 36.92) 
print(ob.x)
print(ob.y)