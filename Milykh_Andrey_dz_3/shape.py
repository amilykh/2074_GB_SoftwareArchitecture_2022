from abc import abstractmethod

lst_shapes = ['прямоугольник', 'квадрат', 'круг', 'треугольник']


class Shape:
    def __init__(self, name, a=None, b=None, c=None):
        self.name = self._is_valid_name(name)
        self.a = self._is_valid_a(a)
        self.b = self._is_valid_b(b)
        self.c = self._is_valid_c(c)

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def print_info(self, name):
        print(f'Фигура: {name}; периметр: {self.get_perimeter()}; площадь: {self.get_area()}')

    def _is_valid_name(self, name):
        if name not in lst_shapes:
            raise ValueError("Первый параметр - недопустимое название фигуры !")
        return name

    def _is_valid_a(self, a):
        if type(a) == int or type(a) == float:
            if a <= 0:
                raise ValueError("Второй параметр должен быть больше 0 !")
            return a
        else:
            raise ValueError("The variable a is not a number")

    def _is_valid_b(self, b):
        if self.name in ['квадрат', 'круг']:
            return None
        if type(b) == int or type(b) == float:
            if self.name in ['прямоугольник', 'треугольник']:
                if b <= 0:
                    raise ValueError("Третий параметр должен быть больше 0 !")
                return b
        else:
            raise ValueError("The variable b is not a number")

    def _is_valid_c(self, c):
        if self.name == 'треугольник':
            if type(c) == int or type(c) == float:
                if c <= 0:
                    raise ValueError("Третий параметр должен быть больше 0 !")
                if (self.a + self.b <= c) or (self.a + c <= self.b) or (self.b + c <= self.a):
                    raise ValueError("Сторона треугольника не может быть меньше или равна сумме двух других !")
                return c
            else:
                raise ValueError("The variable c is not a number")
        return None
