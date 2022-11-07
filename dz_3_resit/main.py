from sys import exit
from shape import Shape
from rectangle import Rectangle
from shape_factory import ShapeFactory
from square import Square
from circle import Circle
from triangle import Triangle
from typing import List

names_of_shapes = ['rectangle', 'square', 'triangle', 'circle']


def shapes_client(shapes: List):
    shape_factory = ShapeFactory()
    shape_name = input("Enter the name of the shape (rectangle, square, "
                       "triangle or circle): ")
    if shape_name in names_of_shapes:
        shape = shape_factory.create_shape(shape_name)
        if shape is not None:
            shapes.append(shape)
            print("The shape is created!")
        else:
            print("The shape is not created!")
    else:
        print("The name of the shape not entered correctly!")


def show_shapes(shapes: List):
    if len(shapes) == 0:
        print("The list of shapes is empty")
        return

    for shape in shapes:
        if type(shape) in [Rectangle, Square, Triangle]:
            print(f"{type(shape)}, area: {shape.calc_area()}, perimeter: "
                  f"{shape.calc_length()}")
        elif type(shape) == Circle:
            print(f"{type(shape)}, area: {shape.calc_area()}, length:"
                  f" {shape.calc_length()}")


def menu():
    main_menu = "Select the menu item [1] - create shape, [2] - show shapes, " \
           "[3] - exit: "
    l: List[Shape] = []
    cmd = input(main_menu)
    while cmd != "3":
        if cmd == "1":
            shapes_client(l)
            cmd = input(main_menu)
        elif cmd == "2":
            show_shapes(l)
            cmd = input(main_menu)
        else:
            print("Selection error!")
            cmd = input(main_menu)

    exit()


def main():
    menu()


if __name__ == "__main__":
    main()
