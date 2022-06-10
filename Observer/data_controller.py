"A data controller that is a subject"

from interface_data_controller import IDataController


class DataController(IDataController):
    "a Subject (Observable)"

    _observers = set()

    def __new__(cls):
        return cls

    @classmethod
    def subscribe(cls, observer):
        cls._observers.add(observer)

    @classmethod
    def unsubscribe(cls, observer):
        cls._observers.remove(observer)

    @classmethod
    def notify(cls, *args):
         for observer in cls._observers:
            observer.notify(*args)
