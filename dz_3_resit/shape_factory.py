from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle


class ShapeFactory:
    @staticmethod
    def create_shape(name):
        numeric_side_error = "The side must be a positive integer number !"
        numeric_radius_error = "The radius must be a positive integer number !"
        side_error = "The side must be greater than 0 !"
        radius_error = "The radius must be greater than 0 !"
        triangle_error = "The side of the triangle must be less than " \
                         "the sum of the other two sides !"
        if name == 'circle':
            radius = input("Enter the radius of the circle "
                           "(positive integer): ")
            if not Circle.check_numeric(radius):
                print(numeric_radius_error)
                return None
            if not Circle.check_radius(int(radius)):
                print(radius_error)
                return None
            return Circle(int(radius))
        elif name == 'rectangle':
            height = input("Enter the height of the rectangle "
                           "(positive integer): ")
            if not Rectangle.check_numeric(height):
                print(numeric_side_error)
                return None
            if not Rectangle.check_side(int(height)):
                print(side_error)
                return None
            width = input("Enter the width of the rectangle "
                          "(positive integer): ")
            if not Rectangle.check_numeric(width):
                print(numeric_side_error)
                return None
            if not Rectangle.check_side(int(width)):
                print(side_error)
                return None
            return Rectangle(int(width), int(height))
        elif name == 'square':
            width = input("Enter the width of the square (positive integer): ")
            if not Rectangle.check_numeric(width):
                print(numeric_side_error)
                return None
            if not Rectangle.check_side(int(width)):
                print(side_error)
                return None
            return Square(int(width))
        elif name == 'triangle':
            a = input("Enter the size of the first side of the triangle "
                      "(positive integer): ")
            if not Triangle.check_numeric(a):
                print(numeric_side_error)
                return None
            if not Triangle.check_side(int(a)):
                print(side_error)
                return None
            b = input("Enter the size of the second side of the triangle "
                      "(positive integer): ")
            if not Triangle.check_numeric(b):
                print(numeric_side_error)
                return None
            if not Triangle.check_side(int(b)):
                print(side_error)
                return None
            c = input("Enter the size of the third side of the triangle "
                      "(positive integer): ")
            if not Triangle.check_numeric(c):
                print(numeric_side_error)
                return None
            if not Triangle.check_side(int(c)):
                print(side_error)
                return None
            if not Triangle.check_triangle(int(a), int(b), int(c)):
                print(triangle_error)
                return None
            return Triangle(int(a), int(b), int(c))
