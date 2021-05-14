import math
from typing import Tuple
from drawer import Drawer
from tkinter import PhotoImage, Canvas


class Test(Canvas):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.img = PhotoImage(width=1344, height=976)

    def getColorOfPixel(self, x: int, y: int) -> str:
        colorTuple = self.img.get(x, y)
        color = "#" + f"{colorTuple[0]:02X}" + f"{colorTuple[1]:02X}" + f"{colorTuple[2]:02X}"
        return color

test = Test()
test.img.put("#FFFFFF", (5, 5))
print(test.getColorOfPixel(5, 5))
test.img.put("#000000", (5, 5))
print(test.getColorOfPixel(5, 5))
print(test.getColorOfPixel(6,6))

