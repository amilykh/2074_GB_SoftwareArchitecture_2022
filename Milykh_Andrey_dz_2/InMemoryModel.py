from ModelElements import PoligonalModel, Scene, Flash, Camera


class IModelChangedObserver:
    def ApplyUpdateModel(self):
        pass


class IModelChanger:
    def NotifyChange(self):
        return self


class ModelStore:
    def __init__(self):
        self.Models = PoligonalModel()
        self.Scenes = Scene()
        self.Flash = Flash()
        self.Cameras = Camera()
        self.__changeObsevers = IModelChangedObserver()

    def GetScena(self, Id: int) -> Scene:
        if self.Scenes.Id == Id:
            return self.Scenes

    def NotifyChange(self, sender: IModelChanger):
        pass