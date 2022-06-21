"""An interface that each component will implement"""

from abc import ABCMeta, abstractmethod


class IComponent(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def notify(message):
        """The required notify method"""

    @staticmethod
    @abstractmethod
    def receive(message):
        """The required receive method"""
