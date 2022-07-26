"""An abstract document containing a combination of hooks and abstract methods"""

from abc import ABCMeta, abstractmethod


class AbstractDocument(metaclass=ABCMeta):
    """A template class containing a template method and primitive methods"""

    @staticmethod
    @abstractmethod
    def title(document):
        """Must implement"""

    @staticmethod
    def description(document):
        """Optional"""

    @staticmethod
    def author(document):
        """Optional"""

    @staticmethod
    def background_color(document):
        """Optional with a default behavior"""
        document["background_color"] = "white"

    @staticmethod
    @abstractmethod
    def text(document, text):
        """Must implement"""

    @staticmethod
    def footer(document):
        """Optional"""

    @staticmethod
    def print(document):
        """Optional with a default behavior"""
        print("-------------------")
        for attribute in document:
            print(f"{attribute}\t : {document[attribute]}")
        print()

    @classmethod
    def create_document(cls, text):
        """The template method"""
        _document = {}
        cls.title(_document)
        cls.description(_document)
        cls.author(_document)
        cls.background_color(_document)
        cls.text(_document, text)
        cls.footer(_document)
        cls.print(_document)
