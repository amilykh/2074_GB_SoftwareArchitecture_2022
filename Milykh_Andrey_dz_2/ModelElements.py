from Work3D import Point3D, Angle3D, Color, Type


class Texture:
    pass


class Poligon:
    def __init__(self, Points: Point3D):
        self.Points = Points


class PoligonalModel:
    def __init__(self, Poligons: Poligon, Textures: Texture):
        self.Poligons = Poligons
        self.Textures = Textures


class Camera:
    def __init__(self, Location: Point3D, Angle: Angle3D):
        self.Location = Location
        self.Angle = Angle

    def Rotate(self, angle: Angle3D) -> None:
        pass

    def Move(self, point: Point3D) -> None:
        pass


class Flash:
    def __init__(self, Location: Point3D, Angle: Angle3D, Color: Color, Power: float):
        self.Location = Location
        self.Angle = Angle
        self.Color = Color
        self.Power = Power

    def Rotate(self, angle: Angle3D) -> None:
        pass

    def Move(self, point: Point3D) -> None:
        pass


class Scene:
    def __init__(self, Id: int, Models: PoligonalModel, Flashes: Flash):
        self.Id = Id
        self.Models = Models
        self.Flashes = Flashes

    def method1(self, type1: Type) -> Type:
        return type1

    def method2(self, type1: Type, type2: Type) -> Type:
        return type1 if type1 > type2 else type2
