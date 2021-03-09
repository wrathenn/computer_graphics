from typing import Tuple, List
from geometry import Matrix

import matplotlib
import tkinter as tk
import tkinter.messagebox as tkmsg

from graph import Graph

# Приготовления
matplotlib.use('TkAgg')

# Создать окно
root = tk.Tk()
root.title("ЛР №2 Шацкий Р.Е. ИУ7-45Б")
root.geometry('1920x1080')

# Фрейм с графиком

mainFrame = tk.Frame(root)
mainFrame.place(relx=0.0, rely=0.0, relwidth=0.875, relheight=1.0, anchor="nw")

graph = Graph(mainFrame, x_offset=10, y_offset=10)
action_history = []
figure_history = []
center_history: List[Tuple[float, float]] = []

# Фрейм с полями ввода и кнопками

inputFrame = tk.Frame(root)
inputFrame.place(relx=0.875, rely=0.0, relwidth=0.125, relheight=1.0, anchor="nw")

# ЗАРАНЕЕ ЛЕЙБЛ С ЦЕНТРОМ
centerLabel = tk.Label(inputFrame, text=f"Центр эпициклоида:\n{graph.x_center:.3f}, {graph.y_center:.3f}")
centerLabel.place(relx=0.0, rely=7 / 18, relwidth=1, relheight=1 / 18)

def change_history(action: str):
    if len(action_history) == 3:
        action_history.pop(0)
        figure_history.pop(0)
        center_history.pop(0)
    action_history.append(action)
    figure_history.append(list(obj for obj in graph.drawn_epicycloid))
    center_history.append((graph.x_center, graph.y_center))

    lastActionText.configure(text=action_history[len(action_history) - 1] if len(action_history) else "")

# Переместить

# Переместить - виджеты
moveLabel = tk.Label(inputFrame, text="Перемещение")
moveLabel.place(relx=0.0, rely=0.0, relwidth=1, relheight=1 / 18)
moveXLabel = tk.Label(inputFrame, text="x", justify="center")
moveXLabel.place(relx=0.0, rely=1 / 18, relwidth=0.5, relheight=1 / 18)
moveYLabel = tk.Label(inputFrame, text="y", justify="center")
moveYLabel.place(relx=0.5, rely=1 / 18, relwidth=0.5, relheight=1 / 18)

moveXInput = tk.Entry(inputFrame, justify="center")
moveXInput.place(relx=0.0, rely=2 / 18, relwidth=0.5, relheight=1 / 18)
moveYInput = tk.Entry(inputFrame, justify="center")
moveYInput.place(relx=0.5, rely=2 / 18, relwidth=0.5, relheight=1 / 18)


# Переместить - функции
def move():
    x_offset: float
    y_offset: float
    try:
        x_offset = float(moveXInput.get())
    except ValueError:
        tkmsg.showerror("Ошибка!", "Некорректное смещение по X")
        return
    try:
        y_offset = float(moveYInput.get())
    except ValueError:
        tkmsg.showerror("Ошибка!", "Некорректное смещение по Y")
        return

    change_history(f"Перемещение\nПо x - {x_offset}\nПо y - {y_offset}")

    graph.move_epicycloid(x_offset, y_offset)
    centerLabel.configure(text=f"Центр эпициклоида:\n{graph.x_center:.3f}, {graph.y_center:.3f}")


moveButton = tk.Button(inputFrame, justify="center", bg="green", text="Переместить",
                       command=lambda: move(), fg="white")
moveButton.place(relx=0.0, rely=3 / 18, relwidth=1, relheight=1 / 18)

# Центр
centerMainLabel = tk.Label(inputFrame, text="Центр")
centerMainLabel.place(relx=0.0, rely=4 / 18, relwidth=1, relheight=1 / 18)
centerXLabel = tk.Label(inputFrame, text="x", justify="center")
centerXLabel.place(relx=0.0, rely=5 / 18, relwidth=0.5, relheight=1 / 18)
centerYLabel = tk.Label(inputFrame, text="y", justify="center")
centerYLabel.place(relx=0.5, rely=5 / 18, relwidth=0.5, relheight=1 / 18)

centerXInput = tk.Entry(inputFrame, justify="center")
centerXInput.place(relx=0.0, rely=6 / 18, relwidth=0.5, relheight=1 / 18)
centerYInput = tk.Entry(inputFrame, justify="center")
centerYInput.place(relx=0.5, rely=6 / 18, relwidth=0.5, relheight=1 / 18)

# Масштабирование
scaleLabel = tk.Label(inputFrame, text="Масштабирование")
scaleLabel.place(relx=0.0, rely=8 / 18, relwidth=1, relheight=1 / 18)

scaleRatioXLabel = tk.Label(inputFrame, text="x", justify="center")
scaleRatioXLabel.place(relx=0.0, rely=9 / 18, relwidth=0.5, relheight=1 / 18)
scaleRatioXInput = tk.Entry(inputFrame, justify="center")
scaleRatioXInput.place(relx=0.5, rely=9 / 18, relwidth=0.5, relheight=1 / 18)

scaleRatioYLabel = tk.Label(inputFrame, text="y", justify="center")
scaleRatioYLabel.place(relx=0.0, rely=10 / 18, relwidth=0.5, relheight=1 / 18)
scaleRatioYInput = tk.Entry(inputFrame, justify="center")
scaleRatioYInput.place(relx=0.5, rely=10 / 18, relwidth=0.5, relheight=1 / 18)


def scale():
    x_scale: float
    y_scale: float
    try:
        x_scale = float(scaleRatioXInput.get())
    except ValueError:
        tkmsg.showerror("Ошибка!", "Некорректное увеличение по X")
        return
    try:
        y_scale = float(scaleRatioYInput.get())
    except ValueError:
        tkmsg.showerror("Ошибка!", "Некорректное увеличение по Y")
        return

    x_center: float
    y_center: float
    try:
        x_center = float(centerXInput.get())
    except ValueError:
        tkmsg.showerror("Ошибка!", "Некорректное смещение по X")
        return
    try:
        y_center = float(centerYInput.get())
    except ValueError:
        tkmsg.showerror("Ошибка!", "Некорректное смещение по Y")
        return

    change_history(f"Масштабирование\nПо x - {x_scale}\nПо y -  {y_scale}\nЦентр - {x_center}, {y_center}")

    graph.scale_epicycloid(x_center, y_center, x_scale, y_scale)
    centerLabel.configure(text=f"Центр эпициклоида: {graph.x_center:.3f}, {graph.y_center:.3f}")


scaleButton = tk.Button(inputFrame, justify="center", bg="green", text="Увеличить",
                        command=lambda: scale(), fg="white")
scaleButton.place(relx=0.0, rely=11 / 18, relwidth=1, relheight=1 / 18)

# Поворот
rotationLabel = tk.Label(inputFrame, text="Поворот")
rotationLabel.place(relx=0.0, rely=12 / 18, relwidth=1, relheight=1 / 18)

rotationAngleLabel = tk.Label(inputFrame, text="Угол", justify="center")
rotationAngleLabel.place(relx=0.0, rely=13 / 18, relwidth=0.5, relheight=1 / 18)
rotationAngleInput = tk.Entry(inputFrame, justify="center")
rotationAngleInput.place(relx=0.5, rely=13 / 18, relwidth=0.5, relheight=1 / 18)


def rotate():
    angle: int
    try:
        angle = int(rotationAngleInput.get())
    except ValueError:
        tkmsg.showerror("Ошибка!", "Некорректно введен угол вращения")
        return

    x_center: float
    y_center: float
    try:
        x_center = float(centerXInput.get())
    except ValueError:
        tkmsg.showerror("Ошибка!", "Некорректное смещение по X")
        return
    try:
        y_center = float(centerYInput.get())
    except ValueError:
        tkmsg.showerror("Ошибка!", "Некорректное смещение по Y")
        return

    change_history(f"Масштабирование\nНа угол {angle}\nЦентр - {x_center}, {y_center}")

    graph.rotate_epicycloid(x_center, y_center, angle)
    centerLabel.configure(text=f"Центр эпициклоида: {graph.x_center:.3f}, {graph.y_center:.3f}")


rotationButton = tk.Button(inputFrame, justify="center", bg="green", text="Повернуть",
                           command=lambda: rotate(), fg="white")
rotationButton.place(relx=0.0, rely=14 / 18, relwidth=1, relheight=1 / 18)

# Правка
rotationLabel = tk.Label(inputFrame, text="Правка")
rotationLabel.place(relx=0.0, rely=15 / 18, relwidth=1, relheight=1 / 18)

lastActionText = tk.Label(inputFrame, justify=tk.LEFT, state=tk.NORMAL, font="ubuntu 14", fg="black", bg="white",
                          anchor="nw", text="Предыдущее действие?")
lastActionText.place(relx=0.0, rely=16 / 18, relwidth=1, relheight=1 / 18)


def undo():
    id: int = len(action_history) - 1
    if id < 0:
        return

    graph.redraw_epicycloid(figure_history[id])
    graph.x_center, graph.y_center = center_history[id]

    action_history.pop(id)
    figure_history.pop(id)
    center_history.pop(id)

    lastActionText.configure(text=action_history[len(action_history) - 1] if len(action_history) else "")
    centerLabel.configure(text=f"Центр эпициклоида: {graph.x_center:.3f}, {graph.y_center:.3f}")


undoButton = tk.Button(inputFrame, justify="center", bg="green", text="Отмена",
                       command=lambda: undo(), fg="white")
undoButton.place(relx=0.0, rely=17 / 18, relwidth=1, relheight=1 / 18)

root.mainloop()
