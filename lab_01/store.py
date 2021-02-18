from typing import List

from geometry import Rectangle, Dot


class Store:
    def __init__(self, data=None):
        if data is None:
            data = []
        self.data = data

    def delete(self, data) -> any:
        return

    def getDataList(self):
        return


class RectangleStore(Store):
    def __init__(self, data=None):
        super().__init__(data)

    def change(self, rectangle: Rectangle) -> None:
        self.data = [rectangle]

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

    def clear(self):
        self.data = []


class DotStore(Store):
    def __init__(self, data=None):
        super().__init__(data)

    def add(self, new: Dot):
        for i in self.data:
            i: Dot
            if i.x == new.x and i.y == new.y:
                raise Exception("Такая точка уже есть")
        self.data.append(new)

    def find(self, data: List[float]) -> int:
        for dot, i in zip(self.data, range(len(self.data))):
            dot: Dot
            if data == [dot.x, dot.y]:
                return i
        return -1

    def getDataList(self):
        result = []
        for i in self.data:
            i: Dot
            result.append([i.x, i.y])

        return result

    def delete(self, data: List[float]):
        id: int = self.find(data)
        if id != -1:
            self.data.pop(id)


rectangleStore = RectangleStore()
dotM2Store = DotStore()
