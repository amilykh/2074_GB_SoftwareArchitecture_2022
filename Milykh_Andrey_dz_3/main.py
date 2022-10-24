from shape import Shape
from rectangle import Rectangle
from square import Square
from circle import Circle
from triangle import Triangle


def main():
    shapes = list()
    shapes.append(Shape('прямоугольник', 20, 40))
    shapes.append(Shape('квадрат', 10))
    shapes.append(Shape('круг', 20))
    shapes.append(Shape('треугольник', 3, 4, 5))
    # shapes.append(Shape('прямоугольник', 3, -4))
    # shapes.append(Shape('треугольник', 3, 3, 6))

    # print(shapes)

    for shape in shapes:
        if shape.name == 'прямоугольник':
            r = Rectangle(shape.a, shape.b)
            r.print_info(shape.name)
        elif shape.name == 'квадрат':
            sq = Square(shape.a)
            sq.print_info(shape.name)
        elif shape.name == 'круг':
            c = Circle(shape.a)
            c.print_info(shape.name)
        elif shape.name == 'треугольник':
            tr = Triangle(shape.a, shape.b, shape.c)
            tr.print_info(shape.name)


if __name__ == "__main__":
    main()
