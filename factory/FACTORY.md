### FACTORY Pattern
Factories take care of object creation, and they do only this one job.

There is common practice used called `Simple Factory`, in simple factory one class takes care of the instance initialization 
of the concrete objects. The client class passes it an object type of particular object it wants factory to create.
```markdown
A broader version of Factory method is creating chain of factories where each factory takes care of objects which 
vary from area to area. For example, we can create an abstract interface for Icecream, and different implementations for 
this factory will be creating different icecream base upon the city/area they are located in, as there can be variations 
in flavours and choices as per the climate of different areas.
```
Ice cream factory with base abstract
```python
import inspect
from abc import ABC, abstractmethod

class IceCreamShop(ABC):
    def prepare(self, type):
        print("Your ice cream is being prepared")
        icecream = self.create_icecream(type)
        icecream.prepare()
        icecream.ingredients()
        icecream.price()

    @abstractmethod
    def create_icecream(self, type):
        NotImplementedError(f"{inspect.stack()[0][3]} not implemented")

```

The abstract class to serve as guidelines to create ice creams

```python
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
```
Following are two different ice cream flavours varying from city to village

```python
class DarkBwornChocolate(IceCream):
    def prepare(self):
        print("Preparing Chocolate ICE Cream...")

    def ingredients(self):
        print(f"************ {type(self).__name__} ************ ")
        print("Milk\nChocolate\nPeanut")

    def price(self):
        total = Decimal("0.50")
        print(f"Total price will be ${total}")
        
class LightSugarChocolate(IceCream):
    def prepare(self):
        print("Preparing Chocolate ICE Cream...")

    def ingredients(self):
        print(f"************ {type(self).__name__} ************ ")
        print("Milk\nChocolate\nPeanut")

    def price(self):
        total = Decimal("0.50")
        print(f"Total price will be ${total}")

```

Following snippet shows two stores for ice creams
```python
class CityCreamShop(IceCreamShop):
    def create_icecream(self, type):
        if type == "xx":
            return XX()
        elif type == "xy":
            return XY()


class VillageCreamShop(IceCreamShop):
    def create_icecream(self, type):    
        if type == "aa":
            return AA()
        elif type == "bb":
            return BB()
```

An abstract factory gives an interface for creating a family of products.  