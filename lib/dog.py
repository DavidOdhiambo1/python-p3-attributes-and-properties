#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Fido", breed="Pug"):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) != str or len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self.__name = name

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, breed):
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self.__breed = breed
    
