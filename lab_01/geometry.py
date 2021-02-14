from math import sqrt
from typing import List

FLOAT_ERROR_RATE: float = 1e-6


class Dot:
    def __init__(self, x: int = 0, y: int = 0):
        self.x: int = x
        self.y: int = y

    def setCords(self, x: int, y: int):
        self.x = x
        self.y = y


def dotDistance(dot1: Dot, dot2: Dot) -> float:
    return sqrt((dot1.x - dot2.x) ** 2 + (dot1.y - dot2.y) ** 2)


class GeometryObject:
    def __init__(self, dotList: List[Dot]):
        self.cords: List[Dot] = dotList

    def getCords(self) -> List[Dot]:
        return self.cords


class Rectangle(GeometryObject):
    # Проверить по массиву из 4 точек, что они образуют прямоугольник
    def check(dotList: List[Dot]):
        # Проверка - попарно равные отрезки
        distList: List[float] = list(map(dotDistance, dotList, [*dotList[1::], dotList[0]]))
        if distList[0] != distList[2] or distList[1] != distList[3]:
            return False

        # Проверка - ни один отрезок не должен быть = 0
        for length in distList:
            if length == 0:
                return False

        # Проверка - угол 90 градусов
        hypotenuse: float = dotDistance(dotList[0], dotList[2])
        if abs(distList[0] ** 2 + distList[1] ** 2 - hypotenuse ** 2) > FLOAT_ERROR_RATE:
            return False

        return True

    def __init__(self, *dots):
        if Rectangle.check([*dots]):
            super().__init__([*dots])
            print("Корректный прямоугольник")
        else:
            raise Exception("Некорректные точки")


a = Dot(1, 1)
b = Dot(1, 2)
c = Dot(2, 2)
d = Dot(2, 1)

test: Rectangle

try:
    test = Rectangle(a, b, c, d)
except Exception:
    print("Ошибка")
