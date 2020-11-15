"""
PEP: 8
Title: Rider
Author: Kevin Cook
Status: Active
Type: Process
Created: 11-12-2020
Post: 11-12-2020
History:
"""
from abc import ABC, abstractmethod


class Rider(ABC):
    @abstractmethod
    def Ride(self):
        pass
    @abstractmethod
    def Riders(self):
        pass

class Bicycle(Rider):

    def __init__(self):
        self.num_wheels = 2
        self.Riders=1

    def Ride(self):
        return self.num_wheels
    def Riders(self):
        return self.Riders
    def __str__(self):
        return 'Bicycle, Number of Wheels= '+str(self.num_wheels)+', Number of Riders= '+str(self.Riders)


class Motorcycle(Rider):

    def __init__(self):
        self.num_wheels = 2
        self.Riders = 1

    def Ride(self):
        return self.num_wheels

    def Riders(self):
        return self.Riders
    def __str__(self):
        return 'Motorcycle, Number of Wheels= '+str(self.num_wheels)+', Number of Riders= '+str(self.Riders)


class Car(Rider):

    def __init__(self):
        self.num_wheels = 4
        self.Riders = 4

    def Ride(self):
        return self.num_wheels

    def Riders(self):
        return self.Riders

    def __str__(self):
        return 'Car, Number of Wheels= '+str(self.num_wheels)+', Number of Riders= '+str(self.Riders)

C=Car()
print(str(C))

M=Motorcycle()
print(str(M))

B=Bicycle()
print(str(B))