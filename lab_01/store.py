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

    def getDataList(self):
        return


class RectangleStore(Store):
    def add(self, new: Rectangle):
        self.data.append(new)

    def getDataList(self):
        result = []
        for i in self.data:
            i: Rectangle
            temp = []

            for k in i.cords:
                k: Dot
                temp.append(k.x)
                temp.append(k.y)

            result.append(temp)
        return result


class DotStore(Store):
    def add(self, new: Dot):
        self.data.append(new)

    def getDataList(self):
        result = []
        for i in self.data:
            i: Dot
            result.append([i.x, i.y])

        return result


rectangleStore = RectangleStore()
dotM2Store = DotStore()
