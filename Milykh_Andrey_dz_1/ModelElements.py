from Work3D import Point3D, Angle3D, Color, Type


class Texture:
    pass


class Poligon:
    def __init__(self):
        self.Point = Point3D()


class PoligonalModel:
    def __init__(self):
        self.Poligons = Poligon()
        self.Textures = Texture()


class Camera:
    def __init__(self):
        self.Location = Point3D()
        self.Angle = Angle3D()

    def Rotate(self, angle: Angle3D) -> None:
        pass

    def Move(self, point: Point3D) -> None:
        pass


class Flash:
    def __init__(self):
        self.Location = Point3D()
        self.Angle = Angle3D()
        self.Color = Color()
        self.Power = float()

    def Rotate(self, angle: Angle3D) -> None:
        pass

    def Move(self, point: Point3D) -> None:
        pass


class Scene:
    def __init__(self):
        self.Id = int()
        self.Models = PoligonalModel()
        self.Flashes = Flash()

    def method1(self, type1: Type) -> Type:
        return type1

    def method2(self, type1: Type, type2: Type) -> Type:
        return type1 if type1 > type2 else type2
