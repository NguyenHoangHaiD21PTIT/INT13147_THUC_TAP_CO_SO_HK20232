class Vehicle:
    color = "White"
    def __init__(self, model, max_speed, mileage_instance, type):
        self.model = model
        self.max_speed = max_speed
        self.mileage_instance = mileage_instance
        self.type = type
    
    def __str__(self):
        return "{} {} {} {}".format(self.color, self.model, self.max_speed, self.mileage_instance)

for i in range (2):
    mau, tocDo, soDam, loai = input().split()
    xe = Vehicle(mau, tocDo, soDam, loai)
    print(xe)  