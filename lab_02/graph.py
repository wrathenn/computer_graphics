import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.messagebox as tkmsg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from geometry import Epicycloid


class Graph:
    def __init__(self, parent: tk.Frame):
        self.parent = parent
        self.figure: plt.Figure = plt.figure()
        self.ax = self.figure.add_subplot()

        axes = self.figure.gca()
        axes = self.ax
        axes.set_aspect("equal")
        axes.plot(1, 0, ">k", transform=axes.get_yaxis_transform(), clip_on=False)
        axes.plot(0, 1, "^k", transform=axes.get_xaxis_transform(), clip_on=False)
        axes.set_xlabel("X", loc="right")
        axes.set_ylabel("Y", loc="top")

        # Move the left and bottom spines to x = 0 and y = 0, respectively.
        axes.spines["left"].set_position(("data", 0))
        axes.spines["bottom"].set_position(("data", 0))

        # Hide the top and right spines.
        axes.spines["top"].set_visible(False)
        axes.spines["right"].set_visible(False)
        # axes.set_xlim([-300, 300])
        # axes.set_ylim([-300, 300])

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.parent)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def draw_epicycloid(self, a):
        print(self.ax.lines)

        self.ax.lines.pop()

        epicycloid = Epicycloid(1, a, 2, 3)
        x, y = epicycloid.create_figure()

        self.ax.plot(x, y)
        self.canvas.draw()

    # def countAxes(self, triangle):
    #     localPadding = 2
    #
    #     if len(rectangleStore.data) == 0:
    #         return 0
    #
    #     rectangle: Rectangle = rectangleStore.data[0]
    #     xMax: float = rectangle.cords[0].x
    #     xMin: float = rectangle.cords[0].x
    #     yMax: float = rectangle.cords[0].y
    #     yMin: float = rectangle.cords[0].y
    #
    #     for dot in rectangleStore.data[0].getCords():
    #         xMax = dot.x if dot.x > xMax else xMax
    #         yMax = dot.y if dot.y > yMax else yMax
    #         xMin = dot.x if dot.x < xMin else xMin
    #         yMin = dot.y if dot.y < yMin else yMin
    #
    #     if triangle:
    #         for dot in triangle:
    #             xMax = dot[0] if dot[0] > xMax else xMax
    #             yMax = dot[1] if dot[1] > yMax else yMax
    #             xMin = dot[0] if dot[0] < xMin else xMin
    #             yMin = dot[1] if dot[1] < yMin else yMin
    #
    #     self.data['axisX'] = [xMin - localPadding, xMax + localPadding]
    #     self.data['axisY'] = [yMin - localPadding, yMax + localPadding]
    #     return (xMin, xMax), (yMin, yMax)
