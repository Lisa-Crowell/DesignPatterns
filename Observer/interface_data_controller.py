"A data controller interface"

from abc import ABCMeta, abstractmethod


class IDataController(metaclass=ABCMeta):
    "A Subject interface"

    @staticmethod
    @abstractmethod
    def subscribe(observer):
        "the subscribe method"

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        "the unsubscribe method"

    @staticmethod
    @abstractmethod
    def notify(observer):
        "the notify method"
