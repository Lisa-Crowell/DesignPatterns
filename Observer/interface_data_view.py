"The data View interface"

from abc import ABCMeta, abstractmethod


class IDataView(metaclass=ABCMeta):
    "A method for the observer to implement"

    @staticmethod
    @abstractmethod
    def notify(data):
        "receive notifications"

    @staticmethod
    @abstractmethod
    def draw(data):
        "draw the view"

    @staticmethod
    @abstractmethod
    def delete():
        "a delete methodto remove observer specific resources"