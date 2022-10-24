from shape import Shape


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area(self):
        half_meter = self.get_perimeter()/2.0
        return (half_meter * (
                half_meter - self.a) * (
                half_meter - self.b) * (
                half_meter-self.c)
                ) ** 0.5
