from tkinter import Canvas


class Drawer(Canvas):
    def drawLine(self, points, color="black"):
        width, height = self.getCanvasSize()
        for (x, y) in points:
            if not(x < 0 or x > width or y < 0 or y > height):
                self.create_oval(x, y, x, y, outline=color, width=1)

    def drawLineWithColor(self, pointsWithColor):
        width, height = self.getCanvasSize()
        for (x, y, color) in pointsWithColor:
            if not(x < 0 or x > width or y < 0 or y > height):
                self.create_oval(x, y, x, y, outline=color, width=1)

    def clear(self):
        self.delete("all")

    def getCanvasSize(self):
        return self.winfo_width(), self.winfo_height()
