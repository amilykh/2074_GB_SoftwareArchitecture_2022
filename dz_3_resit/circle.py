from shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return 3.14 * self.radius * self.radius

    def calc_length(self):
        return 2 * 3.14 * self.radius

    @staticmethod
    def check_numeric(radius: str) -> bool:
        return True if radius.isnumeric() else False

    @staticmethod
    def check_radius(radius) -> bool:
        return True if radius > 0 else False
