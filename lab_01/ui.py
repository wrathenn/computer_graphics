from math import sin
from typing import List

import matplotlib
import tkinter as tk
import tkinter.messagebox as tkmsg

from geometry import Dot, Rectangle

from graph import Graph
from table import Table
from store import rectangleStore, dotM2Store

# Приготовления
matplotlib.use('TkAgg')

x: List[float] = []
for i in range(0, 500):
    x.append(i / 10)
y: List[float] = []
for i in x:
    y.append(sin(i))

# Создать окно
root = tk.Tk()
root.geometry('1920x1080')

# Создать фреймы
# M1Frame = tk.Frame(root, bg="#2b2b2b")
# M1Frame.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1, anchor="nw")
M2Frame = tk.Frame(root, bg="#2b2b2b")
M2Frame.place(relx=0.8, rely=0.0, relwidth=0.2, relheight=1, anchor="nw")

mainFrame = tk.Frame(root, bg="#acacac")
mainFrame.place(relx=0.0, rely=0.0, relwidth=0.8, relheight=0.5, anchor="nw")

inputFrame = tk.Frame(root, bg="orange")
rectangleFrame = tk.Frame(inputFrame, bg="red")
dotFrame = tk.Frame(inputFrame, bg="red")
solveFrame = tk.Frame(inputFrame, bg="yellow")
inputFrame.place(relx=0.0, rely=0.5, relwidth=0.8, relheight=0.5, anchor="nw")
rectangleFrame.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1, anchor="nw")
dotFrame.place(relx=0.8, rely=0.0, relwidth=0.2, relheight=1, anchor="nw")
solveFrame.place(relx=0.2, rely=0.0, relwidth=0.6, relheight=1, anchor="nw")

graph = Graph(mainFrame)

# M1Table = Table(M1Frame, ("x1", "y1", "x2", "y2", "x3", "y3", "x4", "y4"), [])
M2Table = Table(M2Frame, ("x", "y"), [])

rectangleLabel = tk.Label(rectangleFrame, text="Прямоугольник")
rectangleLabel.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.125)
rectangleXLabel = tk.Label(rectangleFrame, text="x", justify="center")
rectangleXLabel.place(relx=0.0, rely=0.125, relwidth=0.5, relheight=0.125)
rectangleYLabel = tk.Label(rectangleFrame, text="y", justify="center")
rectangleYLabel.place(relx=0.5, rely=0.125, relwidth=0.5, relheight=0.125)

rectangleDot1XInput = tk.Entry(rectangleFrame, justify="center")
rectangleDot1XInput.place(relx=0.0, rely=0.25, relwidth=0.5, relheight=0.125)
rectangleDot1YInput = tk.Entry(rectangleFrame, justify="center")
rectangleDot1YInput.place(relx=0.5, rely=0.25, relwidth=0.5, relheight=0.125)
rectangleDot2XInput = tk.Entry(rectangleFrame, justify="center")
rectangleDot2XInput.place(relx=0.0, rely=0.375, relwidth=0.5, relheight=0.125)
rectangleDot2YInput = tk.Entry(rectangleFrame, justify="center")
rectangleDot2YInput.place(relx=0.5, rely=0.375, relwidth=0.5, relheight=0.125)
rectangleDot3XInput = tk.Entry(rectangleFrame, justify="center")
rectangleDot3XInput.place(relx=0.0, rely=0.5, relwidth=0.5, relheight=0.125)
rectangleDot3YInput = tk.Entry(rectangleFrame, justify="center")
rectangleDot3YInput.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.125)
rectangleDot4XInput = tk.Entry(rectangleFrame, justify="center")
rectangleDot4XInput.place(relx=0.0, rely=0.625, relwidth=0.5, relheight=0.125)
rectangleDot4YInput = tk.Entry(rectangleFrame, justify="center")
rectangleDot4YInput.place(relx=0.5, rely=0.625, relwidth=0.5, relheight=0.125)


def rectangleGet():
    try:
        dot1 = Dot(int(rectangleDot1XInput.get()), int(rectangleDot1YInput.get()))
    except Exception:
        tkmsg.showwarning("Ошибка!", "Некорректная первая точка")
        return
    try:
        dot2 = Dot(int(rectangleDot2XInput.get()), int(rectangleDot2YInput.get()))
    except Exception:
        tkmsg.showwarning("Ошибка!", "Некорректная вторая точка")
        return
    try:
        dot3 = Dot(int(rectangleDot3XInput.get()), int(rectangleDot3YInput.get()))
    except Exception:
        tkmsg.showwarning("Ошибка!", "Некорректная третья точка")
        return
    try:
        dot4 = Dot(int(rectangleDot4XInput.get()), int(rectangleDot4YInput.get()))
    except Exception:
        tkmsg.showwarning("Ошибка!", "Некорректная четвертая точка")
        return
    
    try:
        rectangle = Rectangle(dot1, dot2, dot3, dot4)
    except Exception:
        tkmsg.showwarning("Ошибка!", "Введенные точки не образуют прямоугольник")
        return

    rectangleStore.add(rectangle)
    M1Table.render(rectangleStore)


def rectangleDelete():
    id = M1Table.table.focus()
    print(id)


rectangleCreateButton = tk.Button(rectangleFrame, justify="center", bg="green", text="Построить",
                                  command=lambda: rectangleGet())
rectangleCreateButton.place(relx=0.0, rely=0.75, relwidth=0.5, relheight=0.125)
rectangleDeleteButton = tk.Button(rectangleFrame, justify="center", bg="red", text="Удалить",
                                  command=lambda: rectangleDelete())
rectangleDeleteButton.place(relx=0.5, rely=0.75, relwidth=0.5, relheight=0.125)
rectangleDeleteAllButton = tk.Button(rectangleFrame, justify="center", bg="darkred", text="УДАЛИТЬ ВСЕ",
                                     command=lambda: print("Заглушка на удаление ВСЕХ прямоугольников"))
rectangleDeleteAllButton.place(relx=0.0, rely=0.875, relwidth=1, relheight=0.125)

dotLabel = tk.Label(dotFrame, text="Точка")
dotLabel.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.125)
dotXLabel = tk.Label(dotFrame, text="x", justify="center")
dotXLabel.place(relx=0.0, rely=0.125, relwidth=0.5, relheight=0.125)
dotYLabel = tk.Label(dotFrame, text="y", justify="center")
dotYLabel.place(relx=0.5, rely=0.125, relwidth=0.5, relheight=0.125)

dotXInput = tk.Entry(dotFrame, justify="center")
dotXInput.place(relx=0.0, rely=0.25, relwidth=0.5, relheight=0.125)
dotYInput = tk.Entry(dotFrame, justify="center")
dotYInput.place(relx=0.5, rely=0.25, relwidth=0.5, relheight=0.125)

def dotGet():
    try:
        dot = Dot(int(dotXInput.get()), int(dotYInput.get()))
    except Exception:
        tkmsg.showwarning("Ошибка!", "Некорректная первая точка")
        return 

    dotM2Store.add(dot)
    M2Table.render(dotM2Store)

def dotDelete():
    id = M2Table.table.focus()
    print(id)
    data = M2Table.table.item(id)["values"]
    dotM2Store.delete(data)
    M2Table.render(dotM2)
    

dotCreateButton = tk.Button(dotFrame, justify="center", bg="green", text="Построить",
                            command=lambda: dotGet())
dotCreateButton.place(relx=0.0, rely=0.375, relwidth=0.5, relheight=0.125)
dotDeleteButton = tk.Button(dotFrame, justify="center", bg="red", text="Удалить",
                            command=lambda: dotDelete())
dotDeleteButton.place(relx=0.5, rely=0.375, relwidth=0.5, relheight=0.125)
dotDeleteAllButton = tk.Button(dotFrame, justify="center", bg="darkred", text="УДАЛИТЬ ВСЕ",
                            command=lambda: print("Заглушка на удаление ВСЕХ точек"))
dotDeleteAllButton.place(relx=0.0, rely=0.5, relwidth=1, relheight=0.125)

editLabel = tk.Label(dotFrame, justify="center", text="Правка")
editLabel.place(relx=0.0, rely=0.625, relwidth=1, relheight=0.125)
revertButton = tk.Button(dotFrame, justify="center", bg="orange", text="Отмена",
                         command=lambda: print("Заглушка на отмену действия"))
revertButton.place(relx=0.0, rely=0.75, relwidth=0.5, relheight=0.125)

solveButton = tk.Button(solveFrame, justify="center", bg="green", text="Решить",
                        command=lambda: print("Заглушка на решение"))
solveButton.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.25)
solveText = tk.Entry(solveFrame, justify="left", state=tk.DISABLED)
solveText.place(relx=0.0, rely=0.25, relwidth=1, relheight=0.75)

root.mainloop()
