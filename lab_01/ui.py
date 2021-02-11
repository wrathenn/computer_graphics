from math import sin, cos
from typing import List

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import tkinter as tk


# Приготовления
matplotlib.use('TkAgg')

# Создать окно
mainWindow = tk.Tk()
mainWindow.geometry('800x600')


plotFrame = tk.Frame(mainWindow, bg="#2b2b2b", bd=5)
plotFrame.place(relx=0.34, rely=0.34, relwidth = 0.5, relheight=0.5, anchor="nw")

figure = plt.figure()

canvas = FigureCanvasTkAgg(figure, master=plotFrame)
plotWidget = canvas.get_tk_widget()
canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


x: List[float] = []
for i in range(0, 500):
    x.append(i/10)
y: List[float] = []
for i in x:
    y.append(sin(i))
plt.plot(x,y)

x: List[float] = []
for i in range(0, 500):
    x.append(i/10)
y: List[float] = []
for i in x:
    y.append(-sin(i))
plt.plot(x,y)

mainWindow.mainloop()
