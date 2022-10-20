from ModelElements import PoligonalModel, Camera, Flash, Scene


class ModelFactory:
    def create_model(self, name):
        if name == 'PoligonalModel':
            Poligon = input("Enter the Poligon of the PoligonalMode: ")
            Texture = input("Enter the Texture of the PoligonalMode: ")
            return PoligonalModel(Poligon, Texture)

        elif name == 'Flash':
            Location = input("Enter the Location of the Flash: ")
            Angle = input("Enter the Angle of the Flash: ")
            Color = input("Enter the Color of the Flash: ")
            Power = input("Enter the Power of the Flash: ")
            return Flash(Location, Angle, Color, Power)

        elif name == 'Camera':
            Location = input("Enter the Location of the Camera: ")
            Angle = input("Enter the Angle of the Camera: ")
            return Camera(Location, Angle)

        elif name == 'Scene':
            Id = input("Enter the Id of the Scene: ")
            Models = input("Enter the Models of the Scene: ")
            Flashes = input("Enter the Flashes of the Scene: ")
            return Scene(Id, Models, Flashes)

