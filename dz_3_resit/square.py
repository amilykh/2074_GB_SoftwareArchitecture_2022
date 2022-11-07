from rectangle import Rectangle


class Square(Rectangle):
    """Квадрат. Конструктор принимает сторону"""
    def __init__(self, a):
        super().__init__(a, a)
