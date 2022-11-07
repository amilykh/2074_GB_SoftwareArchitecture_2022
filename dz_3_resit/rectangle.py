from polygon import Polygon


class Rectangle(Polygon):
    """Прямоугольник. Конструктор принимает длину и ширину"""
    def __init__(self, a: int, b: int):
        super().__init__(4)
        self.a = a
        self.b = b

    def calc_length(self):
        return (self.a + self.b) * 2

    def calc_area(self):
        return self.a * self.b
