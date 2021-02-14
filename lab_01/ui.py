from math import sin
from typing import List

import matplotlib
import tkinter as tk

from graph import Graph


# Приготовления
matplotlib.use('TkAgg')

x: List[float] = []
for i in range(0, 500):
    x.append(i/10)
y: List[float] = []
for i in x:
    y.append(sin(i))

# Создать окно
root = tk.Tk()
root.geometry('1920x1080')

# Создать фреймы
M1Frame = tk.Frame(root, bg="#2b2b2b")
M1Frame.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1, anchor="nw")
M2Frame = tk.Frame(root, bg="#2b2b2b")
M2Frame.place(relx=0.8, rely=0.0, relwidth=0.2, relheight=1, anchor="nw")

mainFrame = tk.Frame(root, bg="#acacac")
mainFrame.place(relx=0.2, rely=0.0, relwidth=0.6, relheight=0.5, anchor="nw")

inputFrame = tk.Frame(root, bg="orange")
rectangleFrame = tk.Frame(inputFrame, bg="red")
dotFrame = tk.Frame(inputFrame, bg="red")
solveFrame = tk.Frame(inputFrame, bg="yellow")
inputFrame.place(relx=0.2, rely=0.5, relwidth=0.6, relheight=0.5, anchor="nw")
rectangleFrame.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1, anchor="nw")
dotFrame.place(relx=0.8, rely=0.0, relwidth=0.2, relheight=1, anchor="nw")
solveFrame.place(relx=0.2, rely=0.0, relwidth=0.6, relheight=1, anchor="nw")

graph = Graph(mainFrame)

tempbut = tk.Button(solveFrame, command=lambda: graph.clear())
tempbut.place(relx=0.0, width=100, height=100)
but = tk.Button(solveFrame, command=lambda: graph.redraw(x, y))
but.place(relx=0.5, width=100, height=100)
def temp():
    x.append(10)
    y.append(10)
b = tk.Button(solveFrame, command=lambda: temp())
b.place(relx=0.25, width=100, height=100)

root.mainloop()
