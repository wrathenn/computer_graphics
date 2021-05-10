from tkinter import *

class Drawer(Canvas):
    def __init__(self, master, bg):
        super().__init__(master, bg=bg)
        self.offsetX = 15
        self.offsetY = 15
        self.offsetAxes = 15

    def drawLine(self, points, color="black"):
        for (x, y) in points:
            self.create_oval(x + self.offsetX, y + self.offsetY, x + self.offsetX, y + self.offsetY, outline=color, width=1)
        # print(points)

    def clear(self):
        self.delete("all")
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
