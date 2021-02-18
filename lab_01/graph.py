import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graph:
    def __init__(self, parent: tk.Frame):
        self.parent = parent
        self.figure: plt.Figure = plt.figure()
        self.figs = []
        p = plt.Polygon([(-1, 1), (0, 0), (-1, -1)], fill=False, ec="blue", lw=3)
        self.figs.append(p)
        self.figure.gca().set_xlim([-10, 10])
        self.figure.gca().set_ylim([-10, 10])
        self.figure.gca().add_patch(p)
        self.figure.gca().set_aspect("equal")
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.parent)
        self.canvas.tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def draw(self):
        p = plt.Polygon([(-5, 1), (0, 0), (-1, -1)], fill=False, ec="red", lw=3)
        self.figure.gca().add_patch(p)
        self.figs.append(p)
        self.figs[0].remove()
        self.canvas.draw()
