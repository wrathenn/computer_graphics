from typing import List

import matplotlib.pyplot as plt
import tkinter as tk
from math import cos, sin, pi
import tkinter.messagebox as tkmsg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from geometry import Epicycloid, Matrix


class Graph:
    HEIGHT_DEFAULT = 1680
    WIDTH_DEFAULT = 976
    Y_SIGN_OFFSET_DEFAULT = 15
    X_SIGN_OFFSET_DEFAULT = 10

    def __init__(self, parent: tk.Frame, x_offset: float = 0, y_offset: float = 0):
        self.parent = parent
        self.canvas: tk.Canvas = tk.Canvas(parent, bg="white")
        self.canvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.x_offset: float = x_offset
        self.y_offset: float = y_offset
        self.drawn_epicycloid: List[Matrix] = []
        self.x_center: float = 0
        self.y_center: float = 0

        self.draw_axes()
        self.draw_epicycloid(50, 150, 700, 600)

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

    # Рисует линии на заданном canvas, проходя по массиву 1х2/1х3 матриц с координатами точек
    def __draw_lines_matrix_array(self, array: List[Matrix]) -> None:
        if not array:
            return

        x1, y1 = array[0].data[0][0], array[0].data[0][1]
        for i in range(1, len(array)):
            x2, y2 = array[i].data[0][0], array[i].data[0][1]
            self.canvas.create_line(x1 + self.x_offset, y1 + self.y_offset,
                                    x2 + self.x_offset, y2 + self.y_offset,
                                    fill="green", width=2)
            x1, y1 = x2, y2

    def draw_epicycloid(self, a: float, b: float, x_center: float, y_center: float) -> None:
        self.clear_canvas()

        self.x_center = x_center
        self.y_center = y_center
        epicycloid = Epicycloid(a, b, x_center, y_center)
        x, y = epicycloid.create_figure()

        # запомнить точки, составляющие эпициклоид
        self.drawn_epicycloid: List[Matrix] = []
        for i in range(len(x)):
            self.drawn_epicycloid.append(Matrix(1, 3, [[x[i], y[i], 1]]))

        # отрисовка всех линий
        self.__draw_lines_matrix_array(self.drawn_epicycloid)

    def move_epicycloid(self, x_offset: float, y_offset: float) -> None:
        # Матрица преобразования для перемещения
        matrix_transform = Matrix(3, 3, [[1, 0, 0],
                                         [0, 1, 0],
                                         [x_offset, y_offset, 1]])

        # Формируем новые координаты эпициклоида
        for i in range(len(self.drawn_epicycloid)):
            self.drawn_epicycloid[i] = self.drawn_epicycloid[i] * matrix_transform

        # Переместить данные о центре
        self.x_center += x_offset
        self.y_center += y_offset

        # Отрисовка
        self.clear_canvas()
        self.__draw_lines_matrix_array(self.drawn_epicycloid)

    def scale_epicycloid(self, x_center: float = 0, y_center: float = 0, scale_x: float = 1,
                         scale_y: float = 1) -> None:
        # Матрица преобразования для масштабирования
        matrix_transform = Matrix(3, 3, [[scale_x, 0, 0],
                                         [0, scale_y, 0],
                                         [0, 0, 1]])

        # Формируем новые координаты эпициклоида
        # X1 = X*Kx + (1-Kx)*Xc & Y1 = Y*Ky + (1-Ky)*Yc
        for i in range(len(self.drawn_epicycloid)):
            self.drawn_epicycloid[i] = self.drawn_epicycloid[i] * matrix_transform
            self.drawn_epicycloid[i].data[0][0] += (1 - scale_x) * x_center
            self.drawn_epicycloid[i].data[0][1] += (1 - scale_y) * y_center

        # Отрисовка
        self.clear_canvas()
        self.__draw_lines_matrix_array(self.drawn_epicycloid)

    def rotate_epicycloid(self, x_center: float = 0, y_center: float = 0, angle: int = 0):
        # Матрица преобразования для масштабирования
        angle: float = angle / 180 * pi
        matrix_transform = Matrix(3, 3, [[cos(angle), -sin(angle), 0],
                                         [sin(angle), cos(angle), 0],
                                         [x_center, y_center, 1]])

        # Формируем новые координаты эпициклоида
        for i in range(len(self.drawn_epicycloid)):
            self.drawn_epicycloid[i] = self.drawn_epicycloid[i] * matrix_transform
            '''
            Так это было не через матрицу
            x_old, y_old = self.drawn_epicycloid[i].data[0][0], self.drawn_epicycloid[i].data[0][1]
            self.drawn_epicycloid[i].data[0][0] = x_center + (x_old - x_center) * cos(angle) + (y_old - y_center) * sin(angle)
            self.drawn_epicycloid[i].data[0][1] = y_center + (y_old - y_center) * cos(angle) - (x_old - x_center) * sin(angle)
            '''

        # Отрисовка
        self.clear_canvas()
        self.__draw_lines_matrix_array(self.drawn_epicycloid)
