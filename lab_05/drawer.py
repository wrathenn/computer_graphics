from tkinter import *
from typing import List, Tuple

from draw_backend import ddaSegment


class Drawer(Canvas):
    def __init__(self, master, bg):
        super().__init__(master, bg=bg)
        self.offsetX = 15
        self.offsetY = 15
        self.offsetAxes = 15
        self.img = PhotoImage(width=1344, height=976)

    def drawLine(self, points, color="black"):
        for (x, y) in points:
            self.img.put(color, (x + self.offsetX, y + self.offsetY))
            # self.create_oval(x + self.offsetX, y + self.offsetY, x + self.offsetX, y + self.offsetY, outline=color,
            #                  width=1)
        # 688, 503)
        self.create_image((0, 0), image=self.img, state="normal", anchor="nw")

    def imgDrawLine(self, x1, y1, x2, y2, color):
        lineDots = ddaSegment(x1, y1, x2, y2)
        for dot in lineDots:
            self.img.put(color, dot)

    def redraw(self):
        self.delete("all")
        self.create_image((0, 0), image=self.img, state="normal", anchor="nw")
        self.drawAxes()

    def clear(self):
        self.delete("all")
        self.img = PhotoImage(width=1344, height=976)
        self.drawAxes()

    def getCanvasSize(self):
        return self.winfo_width(), self.winfo_height()

    def drawAxes(self):
        width, height = self.getCanvasSize()
        width = 1350 if width == 1 else width
        height = 1000 if height == 1 else height

        self.create_line(self.offsetX, self.offsetY,
                         width - self.offsetX, self.offsetY,
                         arrow=LAST)

        self.create_line(self.offsetX, self.offsetY,
                         self.offsetX, height - self.offsetY - 30,
                         arrow=LAST)

        for x_text in range(100, width - 2 * self.offsetX, 100):
            self.create_line(x_text + self.offsetX, self.offsetY - 3,
                             x_text + self.offsetX, self.offsetY + 3)
            self.create_text(x_text + self.offsetX, self.offsetY + self.offsetAxes,
                             text=f"{x_text}")

        for y_text in range(100, height - 2 * self.offsetY, 100):
            self.create_line(self.offsetX - 3, y_text + self.offsetY,
                             self.offsetX + 3, y_text + self.offsetY)
            self.create_text(self.offsetX + self.offsetAxes, y_text + self.offsetY,
                             text=f"{y_text}")

        self.create_text(self.offsetX + self.offsetAxes, self.offsetY + self.offsetAxes,
                         text="0")
        self.create_text(width - self.offsetX, self.offsetY + self.offsetAxes, text="X")
        self.create_text(self.offsetX + self.offsetAxes, height - self.offsetY, text="Y")

    def getColorOfPixel(self, x: int, y: int) -> str:
        colorTuple = self.img.get(x, y)
        color = "#" + f"{colorTuple[0]:X}" + f"{colorTuple[1]:X}" + f"{colorTuple[2]:X}"
        return color

    def fillFigure(self, figureList: List[List[Tuple[int, int]]], isDelayed: bool = False) -> None:
        uniqueColor = "#BOOB69"
        bgColor = "#FFFFFF"
        # Найти максимумы
        xMax: int = figureList[0][0][0]
        xMin: int = figureList[0][0][0]
        yMax: int = figureList[0][0][0]
        yMin: int = figureList[0][0][0]

        figure: List[Tuple[int, int]]
        for figure in figureList:
            for dot in figure:
                xMax = max(dot[0], xMax)
                xMin = min(dot[0], xMin)
                yMax = max(dot[1], yMax)
                yMin = min(dot[1], yMin)

        inFigure: bool = False
        for figure in figureList:
            for dot in figure:
                xMax = max(dot[0], xMax)
                xMin = min(dot[0], xMin)
                yMax = max(dot[1], yMax)
                yMin = min(dot[1], yMin)


