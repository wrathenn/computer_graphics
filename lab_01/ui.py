import matplotlib
import tkinter as tk
import tkinter.messagebox as tkmsg

from geometry import Dot, Rectangle

from graph import Graph
from table import Table
from store import rectangleStore, dotM2Store

# Приготовления
matplotlib.use('TkAgg')

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

inputFrame = tk.Frame(root)
rectangleFrame = tk.Frame(inputFrame)
dotFrame = tk.Frame(inputFrame)
solveFrame = tk.Frame(inputFrame)
inputFrame.place(relx=0.0, rely=0.5, relwidth=0.8, relheight=0.5, anchor="nw")
rectangleFrame.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1, anchor="nw")
dotFrame.place(relx=0.8, rely=0.0, relwidth=0.2, relheight=1, anchor="nw")
solveFrame.place(relx=0.2, rely=0.0, relwidth=0.6, relheight=1, anchor="nw")

graph = Graph(mainFrame)

solveButton = tk.Button(solveFrame, justify="center", bg="green", text="Решить",
                        command=lambda: graph.draw())
solveButton.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.25)
solveText = tk.Label(solveFrame, justify="left", state=tk.DISABLED, font="ubuntu 20", fg="black", bg="white",
                     text="Введите координаты вершин прямоугольника!")
solveText.place(relx=0.0, rely=0.25, relwidth=1, relheight=0.75)

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
        dot1 = Dot(float(rectangleDot1XInput.get()), float(rectangleDot1YInput.get()))
    except Exception:
        tkmsg.showwarning("Ошибка!", "Некорректная первая точка")
        return
    try:
        dot2 = Dot(float(rectangleDot2XInput.get()), float(rectangleDot2YInput.get()))
    except Exception:
        tkmsg.showwarning("Ошибка!", "Некорректная вторая точка")
        return
    try:
        dot3 = Dot(float(rectangleDot3XInput.get()), float(rectangleDot3YInput.get()))
    except Exception:
        tkmsg.showwarning("Ошибка!", "Некорректная третья точка")
        return
    try:
        dot4 = Dot(float(rectangleDot4XInput.get()), float(rectangleDot4YInput.get()))
    except Exception:
        tkmsg.showwarning("Ошибка!", "Некорректная четвертая точка")
        return

    try:
        rectangle = Rectangle(dot1, dot2, dot3, dot4)
    except Exception:
        tkmsg.showwarning("Ошибка!", "Введенные точки не образуют прямоугольник")
        return

    rectangleStore.change(rectangle)
    solveText.configure(text="Координаты текущего прямоугольника:" +
                             "\nx1 - " + str(rectangle.cords[0].x) + ", y1 - " + str(rectangle.cords[0].y) +
                             "\nx2 - " + str(rectangle.cords[1].x) + ", y2 - " + str(rectangle.cords[1].y) +
                             "\nx3 - " + str(rectangle.cords[2].x) + ", y3 - " + str(rectangle.cords[2].y) +
                             "\nx4 - " + str(rectangle.cords[1].x) + ", y4 - " + str(rectangle.cords[1].y))


def rectangleDelete():
    rectangleStore.clear()
    solveText.configure(text="Введите координаты вершин прямоугольника!")


rectangleCreateButton = tk.Button(rectangleFrame, justify="center", bg="green", text="Построить/Изменить",
                                  command=lambda: rectangleGet())
rectangleCreateButton.place(relx=0.0, rely=0.75, relwidth=1, relheight=0.125)
rectangleDeleteButton = tk.Button(rectangleFrame, justify="center", bg="red", text="Удалить",
                                  command=lambda: rectangleDelete())
rectangleDeleteButton.place(relx=0.0, rely=0.875, relwidth=1, relheight=0.125)

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
        dot = Dot(float(dotXInput.get()), float(dotYInput.get()))
    except Exception:
        tkmsg.showwarning("Ошибка!", "Некорректная первая точка")
        return

    try:
        dotM2Store.add(dot)
    except Exception:
        tkmsg.showwarning("Ошибка!", "Такая точка уже есть")
        return

    M2Table.render(dotM2Store)


def dotDelete():
    id = M2Table.table.focus()
    print(id)
    data = M2Table.table.item(id)["values"]
    data = list(map(float, data))
    dotM2Store.delete(data)
    M2Table.render(dotM2Store)

def dotDeleteAll():
    dotM2Store.data = []
    M2Table.render(dotM2Store)


def dotChange():
    id = M2Table.table.focus()
    data = M2Table.table.item(id)["values"]
    data = list(map(float, data))

    storeId = dotM2Store.find(data)
    if storeId != -1:
        changeWindow: tk.Tk = tk.Tk()
        changeWindow.geometry("300x300")
        changeWindow.title("Изменить точку")

        changeWindowFrame = tk.Frame(changeWindow)
        changeWindowFrame.place(relx=0.0, rely=0.0, relwidth=1, relheight=1)
        changeLabel = tk.Label(changeWindowFrame, justify="center",
                               text="Введите новые координаты\n"
                                    "Предыдущие - " + str(data[0]) + ", " + str(data[1]))
        changeLabel.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.25)
        changeXLabel = tk.Label(changeWindowFrame, justify="center", text="X:")
        changeXLabel.place(relx=0.0, rely=0.25, relwidth=0.3, relheight=0.25)
        changeXInput = tk.Entry(changeWindowFrame, justify="center")
        changeXInput.place(relx=0.3, rely=0.25 + 0.0625, relwidth=0.5, relheight=0.125)
        changeYLabel = tk.Label(changeWindowFrame, justify="center", text="Y:")
        changeYLabel.place(relx=0.0, rely=0.50, relwidth=0.3, relheight=0.25)
        changeYInput = tk.Entry(changeWindowFrame, justify="center")
        changeYInput.place(relx=0.3, rely=0.50 + 0.0625, relwidth=0.5, relheight=0.125)

        def localChange():
            try:
                dot = Dot(float(changeXInput.get()), float(changeYInput.get()))
            except Exception:
                tkmsg.showwarning("Ошибка!", "Некорректные данные")
                return
            dotM2Store.data[storeId] = dot
            M2Table.render(dotM2Store)
            changeWindow.destroy()

        changeButton = tk.Button(changeWindowFrame, justify="center", bg="green", text="Изменить",
                                 command=lambda: localChange())
        changeButton.place(relx=0.0, rely=0.75, relwidth=1, relheight=0.25)
        changeWindow.mainloop()


dotCreateButton = tk.Button(dotFrame, justify="center", bg="green", text="Построить",
                            command=lambda: dotGet())
dotCreateButton.place(relx=0.0, rely=0.375, relwidth=0.5, relheight=0.125)
dotDeleteButton = tk.Button(dotFrame, justify="center", bg="red", text="Удалить",
                            command=lambda: dotDelete())
dotDeleteButton.place(relx=0.5, rely=0.375, relwidth=0.5, relheight=0.125)
dotChangeButton = tk.Button(dotFrame, justify="center", bg="orange", text="изменить",
                            command=lambda: dotChange())
dotChangeButton.place(relx=0.0, rely=0.5, relwidth=1, relheight=0.125)
dotDeleteAllButton = tk.Button(dotFrame, justify="center", bg="darkred", text="УДАЛИТЬ ВСЕ",
                               command=lambda: dotDeleteAll())
dotDeleteAllButton.place(relx=0.0, rely=0.625, relwidth=1, relheight=0.125)

root.mainloop()
