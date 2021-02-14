import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Graph:
    def __init__(self, parent: tk.Frame):
        print("init")
        self.figure = plt.figure()
        self.canvas = None
        self.parent: tk.Frame = parent

    # ужасно, из-за этого утекает память
    # TODO: обязательно придумать фикс
    def clear(self):
        if self.canvas:
            self.canvas.tkcanvas.pack_forget()

    def tkDraw(self):
        self.clear()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.parent)
        self.canvas.tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def redraw(self, *args):
        self.clear()
        plt.plot(*args)
        self.tkDraw()