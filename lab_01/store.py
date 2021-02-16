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
    # def add(self, new: Rectangle):
    #     self.data.append(new)

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


class DotStore(Store):
    def __init__(self, data=None):
        super().__init__(data)

    def add(self, new: Dot):
        self.data.append(new)

    def getDataList(self):
        result = []
        for i in self.data:
            i: Dot
            result.append([i.x, i.y])

        return result

    def delete(self, data: List[float]):
        for dot, i in zip(self.data, range(len(self.data))):
            dot: Dot
            if data == [dot.x, dot.y]:
                self.data.pop(i)
                break


rectangleStore = RectangleStore()
dotM2Store = DotStore()
