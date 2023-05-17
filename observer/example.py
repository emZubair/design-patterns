import inspect
from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        raise NotImplementedError(f"{inspect.stack()[0][3]} not implemented")

    @abstractmethod
    def remove_observer(self, observer):
        raise NotImplementedError(f"{inspect.stack()[0][3]} not implemented")

    @abstractmethod
    def notify_observer(self, **kwargs):
        raise NotImplementedError(f"{inspect.stack()[0][3]} not implemented")


class Observer(ABC):
    @abstractmethod
    def sate_update(self, **kwargs):
        raise NotImplementedError(f"{inspect.stack()[0][3]} not implemented")


class ConcreteSubject(Subject):
    def __int__(self):
        self.observers = []

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer:  Observer):
        self.observers.remove(observer)

    def notify_observer(self, **kwargs):
        for observer in self.observers:
            observer.sate_update(**kwargs)


class ConcreteObserverOne(Observer):
    def sate_update(self, **kwargs):
        pass
