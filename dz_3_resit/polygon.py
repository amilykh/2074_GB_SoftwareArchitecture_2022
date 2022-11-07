from abc import abstractmethod
from shape import Shape


class Polygon(Shape):

    def __init__(self, vertices=0):
        self.__vertices = vertices

    def get_vertices(self) -> int:
        return self.__vertices

    def set_vertices(self, quantity: int):
        self.__vertices = quantity

    @staticmethod
    def check_numeric(side: str) -> bool:
        return True if side.isnumeric() else False

    @staticmethod
    def check_side(side) -> bool:
        return True if side > 0 else False

    @abstractmethod
    def calc_length(self):
        pass

    @abstractmethod
    def calc_area(self):
        pass
