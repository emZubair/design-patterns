### DECORATOR Pattern
Decorator is used give responsibilities to an object without modifying the underlying classes. Decorators have 
same supertype as the objects they are decorating and an object can be decorated by multiple decorators.
```commandline
Decorator is used to attach additional responsibilites dynamically and act as an alternative to subclassing.
```
The decorator implements the same interface as the object it is used to wrap.
```python
from abc import ABC, abstractmethod

class Toy(ABC):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @abstractmethod
    def get_cost(self):
        raise NotImplementedError("get_cost method not implemented")

```

Here we've a toy base class, which has one abstract method named `get_cost` used to get the price of the toy object.
There can be multiple type of toys, i.e Simple Toy, Toy with Sound, Toy with Sound and walk feature. Each feature will 
cost extra, so this behaviour can be implemented using decorator pattern.

```python
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
        NotImplementedError("get_name method not implemented")

    @abstractmethod
    def get_cost(self):
        raise NotImplementedError("get_cost method not implemented")
```
Above we've declared an abstract decorator, which will wrap the original object, as we mentioned earlier, the decorator 
implements the same interface as the original wrapped object. So the concrete decorator will add the additional costs by 
calling their `get_cost` method and adding the price over the wrapped object.

```python
class Doll(Toy):
    def get_cost(self):
        return Decimal("2.5")
```

This is simple Doll toy, which costs only `2.5`. Now let's create more exciting features as no one likes a simple toy.
```python
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
```

Here we've declared concrete decoractor which will wrap the original object. Let's see the implementation in action.

```python
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
```

Price of the simple doll will be `2.5`, but a doll with sound feature will cost extra `0.5`, so total will be `3.0`

This is the decorator pattern in action, without changing the existing Doll class, we can create different doll having 
different feature, the decorator helps us here to add dynamic feature over the existing objects.
