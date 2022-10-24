from math import pi
from shape import Shape


class Circle(Shape):
    """Круг. Конструктор принимает радиус"""
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius * self.radius

    def get_perimeter(self):
        return 2 * pi * self.radius
