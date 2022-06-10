#!/usr/bin/env python

from shape_factory import ShapeFactory

shape_name = input('Please enter the shape name: ')

shape_factory = ShapeFactory()
shape = shape_factory.get_shape(shape_name)
print('This is a ' + shape.color + ' ' + shape.type)
