import time
from tkinter import *
from tkinter.ttk import Combobox, Style
from tkinter.messagebox import showerror
from drawer import Drawer
from draw_backend import *
from efficiency import *
from typing import List, Tuple


class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1920x1080")
        self.window.title("Лабораторная работа №3: алгоритмы построения отрезков")
        self.window.attributes("-zoomed", True)

        style = Style()  # If you dont have a class, put your root in the()
        style.configure('TCombobox', arrowsize=30)
        style.configure('Vertical.TScrollbar', arrowsize=28)

        self.initGUI()
        self.canvas.clear()
        self.window.mainloop()

    def initGUICurve(self):
        self.drawCurveFrame = LabelFrame(self.drawParamsFrame, text="Заполнение")
        self.drawCurveFrame.place(relx=0, rely=0, relwidth=1, relheight=0.5)

        self.colors = {
            "Черный": "#000000",
            "Белый": "#FFFFFF",
            "Красный": "#FF0000",
            "Зеленый": "#00FF00",
            "Синий": "#0000FF"
        }
        self.drawCurveColorComboBox = Combobox(
            self.drawCurveFrame,
            values=list(self.colors.keys()),
            state="readonly"
        )
        self.drawCurveColorComboBox.bind("<<ComboboxSelected>>", lambda evt: self.changeCurveColor())
        self.drawCurveColorComboBox.current(0)
        self.drawCurveColorComboBox.place(relx=0.05, rely=0.07, relwidth=0.5)
        self.colorOfCurve = Label(self.drawCurveFrame, bg="black")
        self.colorOfCurve.place(relx=0.60, rely=0.07, relwidth=0.3)

        self.delayBool = BooleanVar()
        self.delayCheckButton = Checkbutton(self.drawCurveFrame, text="Включить задержку", variable=self.delayBool,
                                            onvalue=True, offvalue=False)
        self.delayCheckButton.place(relx=0.05, rely=0.15)

        self.dotLabel = Label(self.drawCurveFrame, text="Построить точку:")
        self.dotLabel.place(relx=0.05, rely=0.25)
        self.xLabel = Label(self.drawCurveFrame, text="X:")
        self.xLabel.place(relx=0.05, rely=0.35, relwidth=0.05)
        self.xEntry = Entry(self.drawCurveFrame)
        self.xEntry.place(relx=0.12, rely=0.35, relwidth=0.2)
        self.yLabel = Label(self.drawCurveFrame, text="Y:")
        self.yLabel.place(relx=0.35, rely=0.35, relwidth=0.05)
        self.yEntry = Entry(self.drawCurveFrame)
        self.yEntry.place(relx=0.42, rely=0.35, relwidth=0.2)

        self.dotButton = Button(self.drawCurveFrame, text="Добавить точку", bg="green", command=self.dotFigure)
        self.dotButton.place(relx=0.02, rely=0.42, relwidth=0.3, relheight=0.12)
        self.stopButton = Button(self.drawCurveFrame, text="Отменить фигуру", bg="orange", command=self.stopFigure)
        self.stopButton.place(relx=0.35, rely=0.42, relwidth=0.3, relheight=0.12)
        self.endButton = Button(self.drawCurveFrame, text="Готово", bg="yellow", command=self.endFigure)
        self.endButton.place(relx=0.68, rely=0.42, relwidth=0.3, relheight=0.12)

        self.fillButton = Button(self.drawCurveFrame, text="Закрасить")
        self.fillButton.place(relx=0.05, rely=0.60, relwidth=0.3, relheight=0.15)
        self.clearButton = Button(self.drawCurveFrame, text="Очистить", command=self.clear)
        self.clearButton.place(relx=0.05, rely=0.60, relwidth=0.3, relheight=0.15)

    def initGUI(self):
        self.plotFrame = Frame(self.window)
        self.canvas = Drawer(self.plotFrame, bg="white")
        self.canvas.pack(fill=BOTH, expand=True)
        self.plotFrame.place(x=500, y=0, width=1420, height=1080)

        self.paramsFrame = Frame(self.window)
        self.paramsFrame.place(relx=0, rely=0, width=500, height=1080)

        self.drawParamsFrame = LabelFrame(self.paramsFrame, text="Параметры")
        self.drawParamsFrame.place(relx=0, rely=0, relwidth=1, relheight=0.875)

        self.initGUICurve()
        self.initCanvasFunctions()

    def initCanvasFunctions(self):
        self.figureList: List[List[Tuple[int, int]]] = [[]]
        self.cur: int = 0

        def leftClick(event):
            print("on canvas - ", (event.x, event.y))
            self.figureList[self.cur].append((event.x, event.y))
            # (event.x - self.canvas.offsetX, event.y - self.canvas.offsetY)
            self.canvas.img.put(self.getCurveColor(), (event.x, event.y))
            self.canvas.create_image((0,0), image=self.canvas.img, state="normal", anchor="nw")
            # self.canvas.create_oval(event.x,
            #                         event.y,
            #                         event.x,
            #                         event.y,
            #                         width=2, outline=self.getCurveColor())

            tmpLen: int = len(self.figureList[self.cur])
            if tmpLen > 1:
                self.canvas.drawLine(ddaSegment(self.figureList[self.cur][tmpLen - 2][0] - self.canvas.offsetX,
                                                self.figureList[self.cur][tmpLen - 2][1] - self.canvas.offsetY,
                                                self.figureList[self.cur][tmpLen - 1][0] - self.canvas.offsetX,
                                                self.figureList[self.cur][tmpLen - 1][1] - self.canvas.offsetY
                                                ), self.getCurveColor())

        def rightClick(event):
            tmpLen: int = len(self.figureList[self.cur])
            if tmpLen < 3:
                showerror("Ошибка!", "Нужно отметить как минимум 3 точки")
                return

            self.canvas.drawLine(ddaSegment(self.figureList[self.cur][0][0] - self.canvas.offsetX,
                                            self.figureList[self.cur][0][1] - self.canvas.offsetY,
                                            self.figureList[self.cur][tmpLen - 1][0] - self.canvas.offsetX,
                                            self.figureList[self.cur][tmpLen - 1][1] - self.canvas.offsetY
                                            ), self.getCurveColor())
            self.cur += 1
            self.figureList.append([])

        def middleClick(event):
            self.figureList.pop()
            self.redrawFigures()
            self.figureList.append([])

        self.canvas.bind("<Button-1>", leftClick)
        self.canvas.bind("<Button-3>", rightClick)
        self.canvas.bind("<Button-2>", middleClick)

    def redrawFigures(self):
        self.canvas.clear()
        figure: List[Tuple[int, int]]
        for figure in self.figureList:
            for i in range(len(figure) - 1):
                self.canvas.drawLine(ddaSegment(figure[i][0] - self.canvas.offsetX,
                                                figure[i][1] - self.canvas.offsetY,
                                                figure[i + 1][0] - self.canvas.offsetX,
                                                figure[i + 1][1] - self.canvas.offsetY
                                                ), self.getCurveColor())
            self.canvas.drawLine(ddaSegment(figure[0][0] - self.canvas.offsetX,
                                            figure[0][1] - self.canvas.offsetY,
                                            figure[len(figure) - 1][0] - self.canvas.offsetX,
                                            figure[len(figure) - 1][1] - self.canvas.offsetY
                                            ), self.getCurveColor())

    def dotFigure(self):
        try:
            _x = int(self.xEntry.get()) + self.canvas.offsetX
        except ValueError:
            showerror("Ошибка!", "Некорректный X")
            return
        try:
            _y = int(self.yEntry.get()) + self.canvas.offsetY
        except ValueError:
            showerror("Ошибка!", "Некорректный X")
            return

        self.figureList[self.cur].append((_x, _y))

        self.canvas.create_oval(_x, _y, _x, _y, width=2, outline=self.getCurveColor())

        tmpLen: int = len(self.figureList[self.cur])
        if tmpLen > 1:
            self.canvas.drawLine(ddaSegment(self.figureList[self.cur][tmpLen - 2][0] - self.canvas.offsetX,
                                            self.figureList[self.cur][tmpLen - 2][1] - self.canvas.offsetY,
                                            self.figureList[self.cur][tmpLen - 1][0] - self.canvas.offsetX,
                                            self.figureList[self.cur][tmpLen - 1][1] - self.canvas.offsetY,
                                            ), self.getCurveColor())

    def endFigure(self):
        tmpLen: int = len(self.figureList[self.cur])
        if tmpLen < 3:
            showerror("Ошибка!", "Нужно отметить как минимум 3 точки")
            return

        self.canvas.drawLine(ddaSegment(self.figureList[self.cur][0][0] - self.canvas.offsetX,
                                        self.figureList[self.cur][0][1] - self.canvas.offsetY,
                                        self.figureList[self.cur][tmpLen - 1][0] - self.canvas.offsetX,
                                        self.figureList[self.cur][tmpLen - 1][1] - self.canvas.offsetY
                                        ), self.getCurveColor())
        self.cur += 1
        self.figureList.append([])

    def stopFigure(self):
        self.figureList.pop()
        self.redrawFigures()
        self.figureList.append([])

    def clear(self):
        w, h = self.getCanvasSize()
        print(w,h)

        self.figureList = [[]]
        self.cur = 0
        self.canvas.clear()

    @staticmethod
    def decardToScreenCoordinates(x, y, width, height):
        return int(x + width / 2), int(height / 2 - y)

    def changeCurveColor(self):
        color = self.drawCurveColorComboBox.get()
        if not color:
            return
        self.colorOfCurve.configure(bg=self.colors[color])

    def getCanvasSize(self):
        return self.canvas.winfo_width(), self.canvas.winfo_height()

    def getCurveColor(self):
        return self.colors[self.drawCurveColorComboBox.get()]

app = App()
