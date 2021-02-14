from geometry import Rectangle, Dot


class Store:
    def __init__(self, data=None):
        if data is None:
            data = []
        self.data = data

    def delete(self, id: int) -> any:
        if id >= len(self.data):
            raise Exception("Некорректный индекс при удалении")
        return self.data.pop(id)


class RectangleStore(Store):
    def add(self, new: Rectangle):
        self.data.append(new)


class DotStore(Store):
    def add(self, new: Dot):
        self.data.append(new)


rectangleStore = RectangleStore()
dotM1Store = DotStore()
dotM2Store = DotStore()
