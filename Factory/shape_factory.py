from shape import Shape
from circle import Circle
from rectangle import Rectangle


class ShapeFactory:
    def get_shape(self, shape_name: str) -> Shape:
        """
        This method takes a string, either 'circle'
        or 'rectangle' and walks the user through
        building the object.
        """
        shape = None

        if shape_name == 'circle':
            color = input('What is the color of the circle?\n> ')
            radius = input('What is the radius of the circle?\n> ')
            shape = Circle(color, radius)
        elif shape_name == 'rectangle':
            color = input('What is the color of the rectangle?\n> ')
            length = input('What is the length of the rectangle?\n> ')
            width = input('What is the width of the rectangle?\n> ')
            shape = Rectangle(color, length, width)
        else:
            print('Invalid shape name...\n')

        return shape
