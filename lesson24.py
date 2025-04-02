#!/usr/bin/python

# poop



class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def drive(self):
        print("the car is being driven")
        if self.model == "poop car":
            print("oh no, geroge crashed")

pemas_car = Car("Lambo", "LP640")
fujiwaraA = Car("toyota","AE86")
gorge_car = Car("car", "poop car")

#:gorge_car.drive()



class Person:
    def __init__(self, money, isGeorge, hair, name):
        self.name = name
        self.money = money
        self.isGeorge = isGeorge
        self.hair = hair

    def spend(self, doing):
        print(f"{self.name} is spending money on {doing}")
        print(f" balance is now {self.money}")

    def drive(self):
        if self.isGeorge == True:
            print("george crashed his poop car")
        else:
            print(f"{self.name} is driving")


luka = Person(3000, False, "brown", "luka")
george = Person(-1000000, True, "black", "george")

luka.drive()
luka.spend("weapons to kill goge")
george.spend("money on poop car")

george.drive()

