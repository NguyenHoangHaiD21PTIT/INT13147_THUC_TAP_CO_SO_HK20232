class Vehicle:
    def __init__(self, model, max_speed, mileage_instance):
        self.model = model
        self.max_speed = max_speed
        self.mileage_instance = mileage_instance
    
    def __str__(self):
        return "{} {} {}".format(self.model, self.max_speed, self.mileage_instance)

class Bus(Vehicle):
    pass

mau, tocDo, soDam = input().split()
bus = Bus(mau, tocDo, soDam)
print(bus)  

