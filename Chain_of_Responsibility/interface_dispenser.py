"The ATM bills dispenser interface"
from abc import ABCMeta, abstractmethod

class IDispenser(metaclass=ABCMeta):
    "Methods to implement"
    @staticmethod
    @abstractmethod
    def next_successor(successor):
        """set the next handler in the chain"""

    @staticmethod
    @abstractmethod
    def handle(amount):
        """handle the event"""