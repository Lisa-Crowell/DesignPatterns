"""A circle abstraction"""

from interface_shape import IShape


class Circle(IShape):
    """The circle is a refined abstraction"""
    def __init__(self, implementer):
        self.implementer = implementer()

    def draw(self):
        self.implementer.draw_implementation()
