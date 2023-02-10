### Strategy Pattern

Suppose you are designing a system to keep track of all birds, you can create a base class named `Bird` and place 
all the common or core functionality there
```python
from abc import ABC, abstractmethod

class Bird(ABC):

    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def fly(self):
        raise NotImplementedError("Fly method not implemented")


    @abstractmethod
    def sound(self):
        raise NotImplementedError("Sound method not implemented")


class Sparrow(Bird):

    def fly(self):
        print("A sparrow can fly")


    def sound(self):
        print("A sparrow can produce sound")
```

The problem with using pure inheritance is that we might need to add toy birds, which don't fly or walk, but because 
of inheritance, those classes will end up implementing `fly` method which doesn't make sense, similar dynamic 
requirement  rise where some features from the inheritance chain are not appropriate for all classed.

```python
class RubberBird(Bird):
    def fly(self):
        print("we've a problem here")


    def sound(self):
        print("Music sound")
```

The solution to this problem would be take away the changing part and encapsulate them to different structure. 
We can create more interfaces as per our requirement and concrete implementations of those interfaces and 
use the composition in the base class.
```python
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

    @abstractmethod
    def sound(self):
        raise NotImplementedError("Sound method not implemented")


class Sparrow(Bird):
    @classmethod
    def create_sparrow(cls, name):
        return Sparrow(name, Flyer())
    def sound(self):
        print("A sparrow can produce sound")


sparrow = Sparrow.create_sparrow("Jack")
```

The above technique is called `Strategy` pattern
```markdown
Strategy
    defines a family of algorithms/behaviours, encapsulates them and uses them interchangeably, it also allows 
algorithms vary independently from clients that use them
```
