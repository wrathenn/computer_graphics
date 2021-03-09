import matplotlib.pyplot as plt
import tkinter as tk
import time
import tkinter.messagebox as tkmsg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from geometry import Epicycloid


class Graph:
    HEIGHT_DEFAULT = 1680
    WIDTH_DEFAULT = 976
    Y_SIGN_OFFSET_DEFAULT = 15
    X_SIGN_OFFSET_DEFAULT = 10

    def __init__(self, parent: tk.Frame, x_offset: int = 0, y_offset: int = 0):
        self.parent = parent
        self.canvas = tk.Canvas(parent, bg="white")
        self.canvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.x_offset = x_offset
        self.y_offset = y_offset
        self.drawn_epicycloid = None

        self.draw_axes()
        self.draw_epicycloid()

    def clear_canvas(self):
        self.canvas.delete("all")
        self.draw_axes()

    def draw_axes(self):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        width = 1680 if width == 1 else width
        height = 976 if height == 1 else height

        # Ось X
        self.canvas.create_line(self.x_offset, self.y_offset,
                                width - self.x_offset, self.y_offset,
                                arrow=tk.LAST)

        # Ось Y
        self.canvas.create_line(self.x_offset, self.y_offset,
                                self.x_offset, height - self.y_offset,
                                arrow=tk.LAST)

        # Метки на оси X
        for x_text in range(100, width - 2 * self.x_offset, 100):
            self.canvas.create_line(x_text + self.x_offset, self.y_offset - 3,
                                    x_text + self.x_offset, self.y_offset + 3)
            self.canvas.create_text(x_text + self.x_offset, self.y_offset + self.X_SIGN_OFFSET_DEFAULT,
                                    text=f"{x_text}")

        # Метки на оси Y
        for y_text in range(100, height - 2 * self.y_offset, 100):
            self.canvas.create_line(self.x_offset - 3, y_text + self.y_offset,
                                    self.x_offset + 3, y_text + self.y_offset)
            self.canvas.create_text(self.x_offset + self.Y_SIGN_OFFSET_DEFAULT, y_text + self.y_offset,
                                    text=f"{y_text}")

    def draw_epicycloid(self):
        self.clear_canvas()
        epicycloid = Epicycloid(20, 30, 200, 300)
        x, y = epicycloid.create_figure()

        # отрисовка всех линий
        x1, y1 = x[0], y[0]
        for x2, y2 in zip(x[1:], y[1:]):
            self.canvas.create_line(x1 + self.x_offset, y1 + self.y_offset,
                                    x2 + self.x_offset, y2 + self.y_offset,
                                    fill="green", width=2)
            x1 = x2
            y1 = y2

        self.drawn_epicycloid = [x1, y1]
