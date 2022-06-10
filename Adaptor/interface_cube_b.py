"an interface to implement"

from abc import ABCMeta, abstractmethod


class ICubeB(metaclass=ABCMeta):
    "an interface to an object"
    @staticmethod
    @abstractmethod
    def create(top_left_front, bottom_right_back):
        "manufactures a cube with coords oofset [0, 0, 0]"