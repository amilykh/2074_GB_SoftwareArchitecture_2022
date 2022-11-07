from polygon import Polygon


class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__(3)
        self.a = a
        self.b = b
        self.c = c

    def calc_length(self):
        return self.a + self.b + self.c

    def calc_area(self):
        half_meter = self.calc_length()/2.0
        return (half_meter * (
                half_meter - self.a) * (
                half_meter - self.b) * (
                half_meter-self.c)
                ) ** 0.5

    @staticmethod
    def check_triangle(a: int, b: int, c: int) -> bool:
        if a >= b + c:
            return False
        if b >= a + c:
            return False
        if c >= a + b:
            return False

        return True
