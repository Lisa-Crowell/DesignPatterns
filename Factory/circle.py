from shape import Shape


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
        self.type = 'circle'
