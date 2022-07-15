from abc import ABC,abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def person(self):
        pass


class Car(Vehicle):
    def person(self):
        print("i have a car")


class Bike(Vehicle):
    def person(self):
        print("i have a bike")

class Flight(Vehicle):
    def person(self):
        print("i have a flight")

a=Car()
a.person()

b=Bike()
b.person()

c=Flight()
c.person()