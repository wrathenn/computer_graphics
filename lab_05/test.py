import math
from typing import Tuple

figure = [(1, 8), (6, 9)]
for i in range(-1, len(figure) - 1):
    dot1: Tuple[int, int] = figure[i]
    dot2: Tuple[int, int] = figure[i + 1]
    print(f"\n\n\nПрямая - {dot1, dot2}")

    dx: int = dot2[0] - dot1[0]
    dy: int = dot2[1] - dot1[1]
    bx: float = dx / abs(dy)
    by = dy / abs(dy)

    print(f"dx = {dx}\ndy = {dy}\nbx = {bx}\nby = {by}\n\n")

    xCur: float = dot1[0] + bx / 2
    yCur: float = dot1[1] + by / 2

    print(f"xCur = {xCur}\nyCur = {yCur}\n\n")


    def centerOfCurrentPixel():
        return math.trunc(xCur) + 0.5, math.trunc(yCur) + 0.5


    def currentPixel():
        return math.trunc(xCur), math.trunc(yCur)


    for _ in range(abs(dy)):
        xCenterOfPixel, yCenterOfPixel = centerOfCurrentPixel()
        xPixel, yPixel = currentPixel()
        print(f"Рассматриваю пиксель {xPixel, yPixel}")
        print(f"Центр пикселя - {xCenterOfPixel, yCenterOfPixel}")
        print(f"Прямая {dot1, dot2} пересекает y = {yCenterOfPixel} в точке ({xCur, yCur})")
        if xCenterOfPixel < xCur:
            print(f"\tЭто правее центра пикселя, флаг - ({xPixel + 1, yPixel})")
            # self.img.put(uniqueColor, (xPixel + 1, yPixel))
        else:
            print(f"\tЭто левее центра пикселя, флаг - ({xPixel, yPixel})")
            # self.img.put(uniqueColor, (xPixel, yPixel))
        xCur += bx
        yCur += by
        print("_____________________________")