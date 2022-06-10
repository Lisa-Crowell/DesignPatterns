"a data model interface"

from abc import ABCMeta, abstractmethod


class IDataModel(metaclass=ABCMeta):
    "A Subject Interface"

    @staticmethod
    @abstractmethod
    def subscribe(observer):
        "the subscribe method"

    @staticmethod
    @abstractmethod
    def unsubscribe(observer_id):
        "the unsubscribe method"

    @staticmethod
    @abstractmethod
    def notify(data):
        "the notify method"