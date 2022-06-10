#!/usr/bin/env python

from abc import ABCMeta, abstractmethod


class IA(metaclass=ABCMeta):
    "An interface for an object"
    @staticmethod
    @abstractmethod
    def method_a():
        "an abstract method A"


class ClassA(IA):
    "a sample class that implements IA"

    def method_a(self):
        print('method A')


class IB(metaclass=ABCMeta):
    "an interface for an object"
    @staticmethod
    @abstractmethod
    def method_b():
        "an abstract method B"


class ClassB(IB):
    "a sample class that implements IB"
    def method_b(self):
        print('method B')


class ClassBAdapter(IA):
    "ClassB doese not have a method_a, so can create an adapter"

    def __init__(self):
        self.class_b = ClassB()

    def method_a(self):
        "calls the class b method method_b instead"
        self.class_b.method_b()


# the client
# before the adapter I need to test the objects class to know which  method to call

ITEMS = [ClassA(), ClassBAdapter()]
for item in ITEMS:
    if isinstance(item, ClassB):
        item.method_b()
    else:
        item.method_a()


# after creating an adapter for ClassB I can reuse the same method
# signature as ClassA (preferred)

ITEMS = [ClassA(), ClassBAdapter()]
for item in ITEMS:
    item.method_a()
