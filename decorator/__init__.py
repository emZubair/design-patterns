from abc import ABC, abstractmethod
from decimal import Decimal
import  inspect


class Toy(ABC):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @abstractmethod
    def get_cost(self):
        raise NotImplementedError(f"{inspect.stack()[0][3]} not implemented")


class FeatureDecorator(Toy):
    """
    Base decorator which will hold reference to the wrapped object
    """

    wrapped_obj: Toy = None

    def __init__(self, wrapper_obj):
        self.wrapped_obj = wrapper_obj
        super().__init__("")

    @abstractmethod
    def get_name(self):
        raise NotImplementedError(f"{inspect.stack()[0][3]} not implemented")

    @abstractmethod
    def get_cost(self):
        raise NotImplementedError(f"{inspect.stack()[0][3]} not implemented")


class Doll(Toy):
    def get_cost(self):
        return Decimal("2.5")


class SoundFeature(FeatureDecorator):
    def get_name(self):
        return self.wrapped_obj.get_name() + ", Special sound feature"

    def get_cost(self):
        return self.wrapped_obj.get_cost() + Decimal("0.5")


class WalkingFeature(FeatureDecorator):
    def get_name(self):
        return self.wrapped_obj.get_name() + ", Special walking feature"

    def get_cost(self):
        return self.wrapped_obj.get_cost() + Decimal("0.7")


simple_doll = Doll("Sleeping Beauty")
print(simple_doll.get_name())
print(simple_doll.get_cost())

doll_with_sound = SoundFeature(simple_doll)
print(doll_with_sound.get_name())
print(doll_with_sound.get_cost())

doll_with_walk = WalkingFeature(simple_doll)
print(doll_with_walk.get_name())
print(doll_with_walk.get_cost())

full_feature_doll = WalkingFeature(doll_with_sound)
print(full_feature_doll.get_name())
print(full_feature_doll.get_cost())
