"an interface to implement"

from abc import ABCMeta, abstractmethod


class ICubeA(metaclass=ABCMeta):
    "an interface for an object"
    @staticmethod
    @abstractmethod
    def manufacture(self, width, height, depth):
        "manufactures a cube"

