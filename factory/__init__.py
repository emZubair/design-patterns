from abc import ABC, abstractmethod
from decimal import Decimal
import inspect

from enum import Enum


class IcecreamTypes(Enum):
    Mocha = "Mocha"
    Chocolate = "Chocolate"
    Strawberry = "Strawberry"


class IceCream(ABC):
    @abstractmethod
    def prepare(self):
        raise NotImplementedError(f"{inspect.stack()[0][3]} not implemented")

    @abstractmethod
    def ingredients(self):
        raise NotImplementedError(f"{inspect.stack()[0][3]} not implemented")

    @abstractmethod
    def price(self):
        raise NotImplementedError(f"{inspect.stack()[0][3]} not implemented")


class Chocolate(IceCream):
    def prepare(self):
        print("Preparing Chocolate ICE Cream...")

    def ingredients(self):
        print(f"************ {type(self).__name__} ************ ")
        print("Milk\nChocolate\nPeanut")

    def price(self):
        total = Decimal("0.50")
        print(f"Total price will be ${total}")


class Strawberry(IceCream):
    def prepare(self):
        print("Preparing Strawberry ICE Cream...")

    def ingredients(self):
        print(f"************ {type(self).__name__} ************ ")
        print("Milk\nStrawberry\nAlmond")

    def price(self):
        total = Decimal("0.75")
        print(f"Total price will be ${total}")


class Mocha(IceCream):
    def prepare(self):
        print("Preparing Mocha ICE Cream...")

    def ingredients(self):
        print(f"************ {type(self).__name__} ************ ")
        print("Milk\nChips\nEspresso")

    def price(self):
        total = Decimal("0.65")
        print(f"Total price will be ${total}")


class SimpleIceCreamFactory:
    @classmethod
    def make_icecream(cls, icecream_type: IcecreamTypes):
        mapping = {
            IcecreamTypes.Mocha: Mocha,
            IcecreamTypes.Chocolate: Chocolate,
            IcecreamTypes.Strawberry: Strawberry,
        }
        if icecream_type not in mapping.keys():
            raise NotImplementedError(f"{icecream_type} is not implemented")
        return mapping[icecream_type]()


class IceCreamShop:
    @classmethod
    def order_icecream(cls, flavour: IcecreamTypes):
        ice_cream = SimpleIceCreamFactory.make_icecream(flavour)
        ice_cream.ingredients()
        ice_cream.prepare()
        ice_cream.price()


IceCreamShop.order_icecream(IcecreamTypes.Mocha)
IceCreamShop.order_icecream(IcecreamTypes.Chocolate)
IceCreamShop.order_icecream(IcecreamTypes.Strawberry)

"""
This is simple factory, client only interacts with the simple factory which takes care of object creations only. 
Whenever new type of Ice creams will be added, only Simple factory will be updated.
"""