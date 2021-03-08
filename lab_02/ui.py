import matplotlib
import tkinter as tk

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

graph = Graph(mainFrame)

# Фрейм с полями ввода и кнопками

inputFrame = tk.Frame(root)
inputFrame.place(relx=0.875, rely=0.0, relwidth=0.125, relheight=1.0, anchor="nw")

# Переместить
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

moveButton = tk.Button(inputFrame, justify="center", bg="green", text="Переместить",
                       command=lambda: print(), fg="white")
moveButton.place(relx=0.0, rely=3 / 18, relwidth=1, relheight=1 / 18)

# Разделитель
separateLabel = tk.Label(inputFrame, bg="blue")
separateLabel.place(relx=0.0, rely=4 / 18, relwidth=1, relheight=1 / 18)

# Центр
centerLabel = tk.Label(inputFrame, text="Центр")
centerLabel.place(relx=0.0, rely=5 / 18, relwidth=1, relheight=1 / 18)
centerXLabel = tk.Label(inputFrame, text="x", justify="center")
centerXLabel.place(relx=0.0, rely=6 / 18, relwidth=0.5, relheight=1 / 18)
centerYLabel = tk.Label(inputFrame, text="y", justify="center")
centerYLabel.place(relx=0.5, rely=6 / 18, relwidth=0.5, relheight=1 / 18)

centerXInput = tk.Entry(inputFrame, justify="center")
centerXInput.place(relx=0.0, rely=7 / 18, relwidth=0.5, relheight=1 / 18)
centerYInput = tk.Entry(inputFrame, justify="center")
centerYInput.place(relx=0.5, rely=7 / 18, relwidth=0.5, relheight=1 / 18)

# Масштабирование
zoomLabel = tk.Label(inputFrame, text="Масштабирование")
zoomLabel.place(relx=0.0, rely=8 / 18, relwidth=1, relheight=1 / 18)

zoomRatioLabel = tk.Label(inputFrame, text="x", justify="center")
zoomRatioLabel.place(relx=0.0, rely=9 / 18, relwidth=0.5, relheight=1 / 18)
zoomRatioInput = tk.Entry(inputFrame, justify="center")
zoomRatioInput.place(relx=0.5, rely=9 / 18, relwidth=0.5, relheight=1 / 18)

zoomButton = tk.Button(inputFrame, justify="center", bg="green", text="Увеличить",
                       command=lambda: print(), fg="white")
zoomButton.place(relx=0.0, rely=10 / 18, relwidth=1, relheight=1 / 18)

# Поворот
rotationLabel = tk.Label(inputFrame, text="Поворот")
rotationLabel.place(relx=0.0, rely=11 / 18, relwidth=1, relheight=1 / 18)

rotationAngleLabel = tk.Label(inputFrame, text="Угол", justify="center")
rotationAngleLabel.place(relx=0.0, rely=12 / 18, relwidth=0.5, relheight=1 / 18)
rotationAngleInput = tk.Entry(inputFrame, justify="center")
rotationAngleInput.place(relx=0.5, rely=12 / 18, relwidth=0.5, relheight=1 / 18)

rotationButton = tk.Button(inputFrame, justify="center", bg="green", text="Повернуть",
                           command=lambda: print(), fg="white")
rotationButton.place(relx=0.0, rely=13 / 18, relwidth=1, relheight=1 / 18)

# Разделитель
separateLabel2 = tk.Label(inputFrame, bg="blue")
separateLabel2.place(relx=0.0, rely=14 / 18, relwidth=1, relheight=1 / 18)

# Правка
rotationLabel = tk.Label(inputFrame, text="Правка")
rotationLabel.place(relx=0.0, rely=15 / 18, relwidth=1, relheight=1 / 18)

lastActionText = tk.Label(inputFrame, justify=tk.LEFT, state=tk.NORMAL, font="ubuntu 14", fg="black", bg="white",
                          anchor="nw", text="Предыдущее действие?")
lastActionText.place(relx=0.0, rely=16 / 18, relwidth=1, relheight=1 / 18)

undoButton = tk.Button(inputFrame, justify="center", bg="green", text="Отмена",
                       command=lambda: print(), fg="white")
undoButton.place(relx=0.0, rely=17 / 18, relwidth=1, relheight=1 / 18)

root.mainloop()
