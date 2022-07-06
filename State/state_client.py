"""The State Design Pattern"""
from abc import ABCMeta, abstractmethod


class Context:
    """This is the object whose behavior will change"""

    def __init__(self):
        self.state_handles = [
            Started(),
            Running(),
            Finished()
        ]
        self._handle = iter(self.state_handles)

    def request(self):
        """Each time the request is called, a new class will handle it"""
        try:
            self._handle.__next__()()
        except StopIteration:
            # resetting so it loops
            self._handle = iter(self.state_handles)


class IState(metaclass=ABCMeta):
    """A State Interface"""

    @staticmethod
    @abstractmethod
    def __call__():
        """Set the default method"""


class Started(IState):
    """A ConcreteState Subclass"""

    @staticmethod
    def method():
        """A task of this class"""
        print("Task started")

    __call__ = method


class Running(IState):
    """A ConcreteState Subclass"""

    @staticmethod
    def method():
        """A task of this class"""
        print("Task running")

    __call__ = method


class Finished(IState):
    """A ConcreteState subclass"""

    @staticmethod
    def method():
        """A task of this class"""
        print("Task finished")

    __call__ = method


# The Client
CONTEXT = Context()
CONTEXT.request()
CONTEXT.request()
CONTEXT.request()
CONTEXT.request()
CONTEXT.request()
CONTEXT.request()
