class Vehicle:
    def __init__(self, name, max_speed, seating_capacity):
        self.name = name
        self.max_speed = max_speed
        self.seating_capacity = seating_capacity

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

a = []
from sys import stdin
for line in stdin: a.append(line.strip())
for x in a:
    tmp = x.split()
    if tmp[3][1:-1:] == "car":
        vec = Car(tmp[0], tmp[1], int(tmp[2]))
        print("Also a Vehicle")
    else:
        vec = Bus(tmp[0], tmp[1], int(tmp[2]))
        print(type(vec))