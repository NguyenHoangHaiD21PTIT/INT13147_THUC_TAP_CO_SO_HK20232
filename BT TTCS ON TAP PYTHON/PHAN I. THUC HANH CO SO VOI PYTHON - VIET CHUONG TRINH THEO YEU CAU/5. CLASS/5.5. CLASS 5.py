class Vehicle:
    def __init__(self, name, max_speed, seating_capacity):
        self.name = name
        self.max_speed = max_speed
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        maintenance_charge = total_fare * 0.1
        final_amount = total_fare + maintenance_charge
        return final_amount

class Car(Vehicle):
    pass

a = []
from sys import stdin
for line in stdin: a.append(line.strip())
for x in a:
    tmp = x.split()
    if tmp[3][1:-1:] == "car":
        vec = Car(tmp[0], tmp[1], int(tmp[2]))
        print("Total Car fare is: " + "{}".format(vec.fare()))
    else:
        vec = Bus(tmp[0], tmp[1], int(tmp[2]))
        print("Total Bus fare is: " + "{}".format(vec.fare()))
    


