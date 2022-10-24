from shape import Shape


class Rectangle(Shape):
    """Прямоугольник. Конструктор принимает длину и ширину"""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_perimeter(self):
        return (self.a + self.b) * 2

    def get_area(self):
        return self.a * self.b
