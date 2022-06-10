#!/usr/bin/env python

"Prototype pattern concept sample code"

from abc import ABCMeta, abstractmethod


class IPrototype(metaclass=ABCMeta):
    "interface with clone method"
    @staticmethod
    @abstractmethod
    def clone():
        """the clone, deep or shallow."""


class MyClass(IPrototype):
    "A concrete class"

    def __int__(self, field):
        self.field = field

    def clone(self):
        return type(self)(
            self.field
            # a shallow copy is returned
            # self.field.copy() # this is also a shallow copy, but has also shallow copied the first level of the field.
            # So it is essentially a shallow copy but 2 levels deep.
            # To recursively deep copy collections containing inner collections, eg. lists of lists,
            # use https://docs/python.org/3/library/copyhtml instead.  example below
        )

    def __str__(self):
        return f"{id(self)}\tfield={self.field}\ttype={type(self.field)}"



# the client
OBJECT1 = MyClass([1, 2, 3, 4]) # create the object containing a list
print(f"OBJECT1 {OBJECT1}")

OBJECT2 = OBJECT1.clone() # clone

# change the value of one of the list elements in OBJECT2 to see if it also modifies the list element in OBJECT1.
# If it changed OBJECT1's copy also, then the clone was done using a 1 level shallow copy process.
# Modify the clone method above to try a 2 level shallow copy instead and cmopare the output

OBJECT2.field[1] = 101

# comparing OBJECT1 and OBJECT2
print(f"OBEJCT2 {OBJECT2}")
print(f"OBJECT1 {OBJECT1}")
