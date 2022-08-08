"""A game interface"""


from abc import ABCMeta, abstractmethod


class IGame(metaclass=ABCMeta):
    """A game interface"""
    @staticmethod
    @abstractmethod
    def add_winner(position, name):
        """Must implement add winner"""
