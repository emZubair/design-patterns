from abc import ABC, abstractmethod


class FlyInterface:
    def fly(self):
        pass


class Flyer(FlyInterface):
    def fly(self):
        print("Yes, I can fly")


class NotAFlyer(FlyInterface):
    def fly(self):
        print("No, I can't fly")


class Bird(ABC):

    def __init__(self, name, flyer):
        self.name = name
        self.flyer = flyer

    def fly(self):
        self.flyer.fly()

    def change_flyer(self, flyer):
        self.flyer = flyer

    @abstractmethod
    def sound(self):
        raise NotImplementedError("Sound method not implemented")


class Sparrow(Bird):
    @classmethod
    def create_sparrow(cls, name):
        return Sparrow(name, Flyer())

    def sound(self):
        print("A sparrow can produce sound")
