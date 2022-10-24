from shape import Shape


class Square(Shape):
    """Квадрат. Конструктор принимает сторону"""
    def __init__(self, a):
        self.a = a

    def get_perimeter(self):
        return self.a * 4

    def get_area(self):
        return self.a ** 2
