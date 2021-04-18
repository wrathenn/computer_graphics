import time
from tkinter import *
from tkinter.ttk import Combobox, Style
from tkinter.messagebox import showerror
from drawer import Drawer
from draw_backend import *
from efficiency import *


class App:
    def __init__(self):
        self.window = Tk()
        self.window.title("Лабораторная работа №3: алгоритмы построения отрезков")
        self.window.attributes("-zoomed", True)

        style = Style()  # If you dont have a class, put your root in the()
        style.configure('TCombobox', arrowsize=30)
        style.configure('Vertical.TScrollbar', arrowsize=28)

        self.initGUI()
        self.canvas.clear()
        self.window.mainloop()

    def initGUICurve(self):
        self.drawCurveFrame = LabelFrame(self.drawParamsFrame, text="Построение кривой")
        self.drawCurveFrame.place(relx=0, rely=0, relwidth=1, relheight=0.5)

        self.drawCurveAlgLabel = Label(self.drawCurveFrame, text="Алгоритм:")
        self.drawCurveAlgLabel.place(relx=0, rely=0, relwidth=0.15, relheight=0.05)
        self.drawCurveAlgComboBox = Combobox(
            self.drawCurveFrame,
            values=[
                "Каноническое уравнение",
                "Параметрическое уравнение",
                "Алгоритм Брезенхема",
                "Алгоритм средней точки",
                "Библиотечная функция"
            ],
            state="readonly"
        )
        self.drawCurveAlgComboBox.current(0)
        self.drawCurveAlgComboBox.place(relx=0.17, rely=0, relwidth=0.8, relheight=0.05)

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

    def initGUICircle(self):
        self.drawCircleFrame = LabelFrame(self.drawCurveFrame, text="Окружность")
        self.drawCircleFrame.place(relx=0, rely=0.14, relwidth=1, relheight=0.38)

        self.drawCircleXLabel = Label(self.drawCircleFrame, text="X центр:")
        self.drawCircleXEntry = Entry(self.drawCircleFrame)
        self.drawCircleXLabel.place(relx=0.02, rely=0.05, relwidth=0.1, relheight=0.15)
        self.drawCircleXEntry.place(relx=0.14, rely=0.05, relwidth=0.15, relheight=0.15)

        self.drawCircleYLabel = Label(self.drawCircleFrame, text="Y центр:")
        self.drawCircleYEntry = Entry(self.drawCircleFrame)
        self.drawCircleYLabel.place(relx=0.02, rely=0.22, relwidth=0.1, relheight=0.15)
        self.drawCircleYEntry.place(relx=0.14, rely=0.22, relwidth=0.15, relheight=0.15)

        self.drawCircleRLabel = Label(self.drawCircleFrame, text="Радиус:")
        self.drawCircleREntry = Entry(self.drawCircleFrame)
        self.drawCircleRLabel.place(relx=0.31, rely=0.05, relwidth=0.1, relheight=0.15)
        self.drawCircleREntry.place(relx=0.43, rely=0.05, relwidth=0.15, relheight=0.15)

        self.drawCircleDrawButton = Button(self.drawCircleFrame, text="Построить", command=self.drawCircle)
        self.drawCircleDrawButton.place(relx=0.02, rely=0.5, relwidth=0.4, relheight=0.4)

        self.drawCircleClearButton = Button(self.drawCircleFrame, text="Очистить")
        self.drawCircleClearButton.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.4)

    def initGUIEllipse(self):
        self.drawEllipseFrame = LabelFrame(self.drawCurveFrame, text="Эллипс")
        self.drawEllipseFrame.place(relx=0, rely=0.55, relwidth=1, relheight=0.38)

        self.drawEllipseRWLabel = Label(self.drawEllipseFrame, text="Ширина:")
        self.drawEllipseRWEntry = Entry(self.drawEllipseFrame)
        self.drawEllipseRWLabel.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.25)
        self.drawEllipseRWEntry.place(relx=0.17, rely=0.05, relwidth=0.3, relheight=0.25)

        self.drawEllipseRHLabel = Label(self.drawEllipseFrame, text="Высота:")
        self.drawEllipseRHEntry = Entry(self.drawEllipseFrame)
        self.drawEllipseRHLabel.place(relx=0.52, rely=0.05, relwidth=0.1, relheight=0.25)
        self.drawEllipseRHEntry.place(relx=0.67, rely=0.05, relwidth=0.3, relheight=0.25)

        self.drawEllipseDrawButton = Button(self.drawEllipseFrame, text="Построить")
        self.drawEllipseDrawButton.place(relx=0.02, rely=0.5, relwidth=0.4, relheight=0.4)

        self.drawEllipseClearButton = Button(self.drawEllipseFrame, text="Очистить")
        self.drawEllipseClearButton.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.4)

    def initGUISpectrum(self):
        self.drawSpectrumFrame = LabelFrame(self.drawParamsFrame, text="Построение спектра")
        self.drawSpectrumFrame.place(relx=0, rely=0.5 , relwidth=1, relheight=0.5)

        self.drawSpectrumAlgLabel = Label(self.drawSpectrumFrame, text="Алгоритм:")
        self.drawSpectrumAlgLabel.place(relx=0, rely=0, relwidth=0.15, relheight=0.05)
        self.drawSpectrumAlgComboBox = Combobox(
            self.drawSpectrumFrame,
            values=[
                "Цифровой дифференциальный анализатор",
                "Целочисленный алгоритм Брезенхема",
                "Вещественный алгоритм Брезенхема",
                "Алгоритм Брезенхема с устранением ступенчатости",
                "Алгоритм Ву",
                "Библиотечная функция"
            ],
            state="readonly"
        )
        self.drawSpectrumAlgComboBox.current(0)
        self.drawSpectrumAlgComboBox.place(relx=0.17, rely=0, relwidth=0.8, relheight=0.05)

        self.colors = {
            "Черный": "#000000",
            "Белый": "#FFFFFF",
            "Красный": "#FF0000",
            "Зеленый": "#00FF00",
            "Синий": "#0000FF"
        }
        self.drawSpectrumColorComboBox = Combobox(
            self.drawSpectrumFrame,
            values=list(self.colors.keys()),
            state="readonly"
        )
        self.drawSpectrumColorComboBox.bind("<<ComboboxSelected>>", lambda evt: self.changeSpectrumColor())
        self.drawSpectrumColorComboBox.current(0)
        self.drawSpectrumColorComboBox.place(relx=0.05, rely=0.07, relwidth=0.5)
        self.colorOfSpectrum = Label(self.drawSpectrumFrame, bg="black")
        self.colorOfSpectrum.place(relx=0.60, rely=0.07, relwidth=0.3)

    def initGUISpectrumCircle(self):
        self.drawSpectrumCircleFrame = LabelFrame(self.drawSpectrumFrame, text="Окружность")
        self.drawSpectrumCircleFrame.place(relx=0, rely=0.14, relwidth=1, relheight=0.38)

        self.drawSpectrumCircleRminLabel = Label(self.drawSpectrumCircleFrame, text="R min:")
        self.drawSpectrumCircleRminEntry = Entry(self.drawSpectrumCircleFrame)
        self.drawSpectrumCircleRminLabel.place(relx=0.02, rely=0.05, relwidth=0.1, relheight=0.15)
        self.drawSpectrumCircleRminEntry.place(relx=0.14, rely=0.05, relwidth=0.15, relheight=0.15)

        self.drawSpectrumCircleRmaxLabel = Label(self.drawSpectrumCircleFrame, text="R min:")
        self.drawSpectrumCircleRmaxEntry = Entry(self.drawSpectrumCircleFrame)
        self.drawSpectrumCircleRmaxLabel.place(relx=0.02, rely=0.22, relwidth=0.1, relheight=0.15)
        self.drawSpectrumCircleRmaxEntry.place(relx=0.14, rely=0.22, relwidth=0.15, relheight=0.15)

        self.drawSpectrumCircleStepLabel = Label(self.drawSpectrumCircleFrame, text="Шаг:")
        self.drawSpectrumCircleStepEntry = Entry(self.drawSpectrumCircleFrame)
        self.drawSpectrumCircleStepLabel.place(relx=0.31, rely=0.05, relwidth=0.1, relheight=0.15)
        self.drawSpectrumCircleStepEntry.place(relx=0.43, rely=0.05, relwidth=0.15, relheight=0.15)

        self.drawSpectrumCircleAmountLabel = Label(self.drawSpectrumCircleFrame, text="Кол-во:")
        self.drawSpectrumCircleAmountEntry = Entry(self.drawSpectrumCircleFrame)
        self.drawSpectrumCircleAmountLabel.place(relx=0.31, rely=0.22, relwidth=0.1, relheight=0.15)
        self.drawSpectrumCircleAmountEntry.place(relx=0.43, rely=0.22, relwidth=0.15, relheight=0.15)

        self.drawSpectrumCircleButton = Button(self.drawSpectrumCircleFrame, text="Построить")
        self.drawSpectrumCircleButton.place(relx=0.02, rely=0.5, relwidth=0.4, relheight=0.4)

        self.drawSpectrumCircleClearButton = Button(self.drawSpectrumCircleFrame, text="Очистить")
        self.drawSpectrumCircleClearButton.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.4)

    def initGUISpectrumEllipse(self):
        self.drawSpectrumEllipseFrame = LabelFrame(self.drawSpectrumFrame, text="Эллипс")
        self.drawSpectrumEllipseFrame.place(relx=0, rely=0.55, relwidth=1, relheight=0.38)

        self.drawSpectrumEllipseRminLabel = Label(self.drawSpectrumEllipseFrame, text="R min:")
        self.drawSpectrumEllipseRminEntry = Entry(self.drawSpectrumEllipseFrame)
        self.drawSpectrumEllipseRminLabel.place(relx=0.02, rely=0.05, relwidth=0.1, relheight=0.15)
        self.drawSpectrumEllipseRminEntry.place(relx=0.14, rely=0.05, relwidth=0.15, relheight=0.15)

        self.drawSpectrumEllipseRmaxLabel = Label(self.drawSpectrumEllipseFrame, text="R min:")
        self.drawSpectrumEllipseRmaxEntry = Entry(self.drawSpectrumEllipseFrame)
        self.drawSpectrumEllipseRmaxLabel.place(relx=0.02, rely=0.22, relwidth=0.1, relheight=0.15)
        self.drawSpectrumEllipseRmaxEntry.place(relx=0.14, rely=0.22, relwidth=0.15, relheight=0.15)

        self.drawSpectrumEllipseStepLabel = Label(self.drawSpectrumEllipseFrame, text="Шаг:")
        self.drawSpectrumEllipseStepEntry = Entry(self.drawSpectrumEllipseFrame)
        self.drawSpectrumEllipseStepLabel.place(relx=0.31, rely=0.05, relwidth=0.1, relheight=0.15)
        self.drawSpectrumEllipseStepEntry.place(relx=0.43, rely=0.05, relwidth=0.15, relheight=0.15)

        self.drawSpectrumEllipseAmountLabel = Label(self.drawSpectrumEllipseFrame, text="Кол-во:")
        self.drawSpectrumEllipseAmountEntry = Entry(self.drawSpectrumEllipseFrame)
        self.drawSpectrumEllipseAmountLabel.place(relx=0.31, rely=0.22, relwidth=0.1, relheight=0.15)
        self.drawSpectrumEllipseAmountEntry.place(relx=0.43, rely=0.22, relwidth=0.15, relheight=0.15)

        self.drawSpectrumEllipseButton = Button(self.drawSpectrumEllipseFrame, text="Построить")
        self.drawSpectrumEllipseButton.place(relx=0.02, rely=0.5, relwidth=0.4, relheight=0.4)

        self.drawSpectrumEllipseClearButton = Button(self.drawSpectrumEllipseFrame, text="Очистить")
        self.drawSpectrumEllipseClearButton.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.4)

    def initGUI(self):
        self.plotFrame = Frame(self.window)
        self.canvas = Drawer(self.plotFrame, bg="white")
        self.canvas.pack(fill=BOTH, expand=True)
        self.plotFrame.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)

        self.paramsFrame = Frame(self.window)
        self.paramsFrame.place(relx=0, rely=0, relwidth=0.3, relheight=1)

        self.drawParamsFrame = LabelFrame(self.paramsFrame, text="Параметры")
        self.drawParamsFrame.place(relx=0, rely=0, relwidth=1, relheight=0.875)

        self.initGUICurve()
        self.initGUICircle()
        self.initGUIEllipse()
        self.initGUISpectrum()
        self.initGUISpectrumCircle()
        self.initGUISpectrumEllipse()


    #
    #     self.clearLineButton = Button(
    #         self.drawLinesFrame,
    #         text="Стереть",
    #         command=self.canvas.clear)
    #     self.clearLineButton.place(relx=0.02, rely=0.67, relwidth=0.45, relheight=0.28)
    #
    #     self.drawLineDrawButton = Button(
    #         self.drawLinesFrame,
    #         text="Построить",
    #         command=self.drawLine)
    #
    #     self.drawLineDrawButton.place(relx=0.52, rely=0.67, relwidth=0.45, relheight=0.28)
    #
    #     self.profilingParams = LabelFrame(self.paramsFrame, text="Исследование характеристик")
    #     self.profilingParams.place(relx=0, rely=0.875, relwidth=1, relheight=0.125)
    #
    #     self.compareTimeButton = Button(self.profilingParams, text="Сравнить эффективность",
    #                                     command=compareTime)
    #     self.compareTimeButton.place(relx=0.02, rely=0.1, relwidth=0.45, relheight=0.8)
    #     self.compareStairsButton = Button(self.profilingParams, text="Сравнить ступенчатость",
    #                                       command=compareStairs)
    #     self.compareStairsButton.place(relx=0.52, rely=0.1, relwidth=0.45, relheight=0.8)
    #
    #     ### ffffffffffffffffffffffffffffffffffffff ###
    #
    #     self.drawSpectrumFrame = LabelFrame(self.drawParamsFrame, text="Построение спектра")
    #     self.drawSpectrumFrame.place(relx=0, rely=0.35, relwidth=1, relheight=0.3)
    #
    #     self.drawSpectrumAlgLabel = Label(self.drawSpectrumFrame, text="Алгоритм:")
    #     self.drawSpectrumAlgLabel.place(relx=0, rely=0, relwidth=0.15)
    #     self.drawSpectrumAlgComboBox = Combobox(
    #         self.drawSpectrumFrame,
    #         values=[
    #             "Цифровой дифференциальный анализатор",
    #             "Целочисленный алгоритм Брезенхема",
    #             "Вещественный алгоритм Брезенхема",
    #             "Алгоритм Брезенхема с устранением ступенчатости",
    #             "Алгоритм Ву",
    #             "Библиотечная функция"
    #         ],
    #         state="readonly"
    #     )
    #     self.drawSpectrumAlgComboBox.current(0)
    #     self.drawSpectrumAlgComboBox.place(relx=0.17, rely=0, relwidth=0.8)
    #
    #     self.drawSpectrumAngleLabel = Label(self.drawSpectrumFrame, text="Угол:")
    #     self.drawSpectrumLengthLabel = Label(self.drawSpectrumFrame, text="Длина:")
    #
    #     self.drawSpectrumAngleEntry = Entry(self.drawSpectrumFrame)
    #     self.drawSpectrumLengthEntry = Entry(self.drawSpectrumFrame)
    #
    #     self.drawSpectrumAngleLabel.place(relx=0, rely=0.2, relwidth=0.1)
    #     self.drawSpectrumAngleEntry.place(relx=0.1, rely=0.2, relwidth=0.15)
    #
    #     self.drawSpectrumLengthLabel.place(relx=0.28, rely=0.2, relwidth=0.1)
    #     self.drawSpectrumLengthEntry.place(relx=0.38, rely=0.2, relwidth=0.15)
    #
    #     self.drawSpectrumColorComboBox = Combobox(
    #         self.drawSpectrumFrame,
    #         values=list(self.colors.keys()),
    #         state="readonly"
    #     )
    #     self.drawSpectrumColorComboBox.bind("<<ComboboxSelected>>", lambda evt: self.changeSpectrumColor())
    #     self.drawSpectrumColorComboBox.current(0)
    #     self.drawSpectrumColorComboBox.place(relx=0.05, rely=0.35, relwidth=0.5)
    #     self.colorOfSpectrum = Label(self.drawSpectrumFrame, bg="black")
    #     self.colorOfSpectrum.place(relx=0.60, rely=0.35, relwidth=0.3)
    #
    #     self.clearSpectrumButton = Button(
    #         self.drawSpectrumFrame,
    #         text="Стереть",
    #         command=self.canvas.clear)
    #     self.clearSpectrumButton.place(relx=0.02, rely=0.67, relwidth=0.45, relheight=0.28)
    #
    #     self.drawSpectrumDrawButton = Button(
    #         self.drawSpectrumFrame,
    #         text="Построить",
    #         command=lambda: self.drawSpectrum())
    #
    #     self.drawSpectrumDrawButton.place(relx=0.52, rely=0.67, relwidth=0.45, relheight=0.28)
    #
    def drawCircle(self):
        xCenter: int
        yCenter: int
        radius: int
        try:
            xCenter = int(self.drawCircleXEntry.get())
        except ValueError:
            showerror("Ошибка!", "Некорректный X центра")
            return
        try:
            yCenter = int(self.drawCircleYEntry.get())
        except ValueError:
            showerror("Ошибка!", "Некорректный Y центра")
            return
        try:
            radius = int(self.drawCircleREntry.get())
        except ValueError:
            showerror("Ошибка!", "Некорректный радиус окружности")
            return

        method = self.drawCurveAlgComboBox.get()
        color = self.getCurveColor()

        if method == "Каноническое уравнение":
            self.canvas.drawLine(drawCircleNormal(xCenter, yCenter, radius), color)
        elif method == "Параметрическое уравнение":
            self.canvas.drawLine(drawCircleParameter(xCenter, yCenter, radius), color)
        elif method == "Алгоритм Брезенхема":
            self.canvas.drawLine(drawCircleBresenham(xCenter, yCenter, radius), color)
        elif method == "Алгоритм средней точки":
            self.canvas.drawLine(drawCircleMiddlePoint(xCenter, yCenter, radius), color)
        elif method == "Библиотечная функция":
            self.canvas.create_oval(xCenter - radius + self.canvas.offsetX, yCenter - radius + self.canvas.offsetY,
                                    xCenter + radius + self.canvas.offsetX, yCenter + radius + self.canvas.offsetY,
                                    outline=color)
    #
    # def drawSpectrum(self):
    #     lineLen = 0
    #     angleStep = 0
    #     try:
    #         lineLen = int(self.drawSpectrumLengthEntry.get())
    #     except ValueError:
    #         showerror("Ошибка!", "Некорректная длина спектра")
    #         return
    #     if lineLen < 0:
    #         showerror("Ошибка!", "Некорректная длина спектра")
    #         return
    #
    #     try:
    #         angleStep = int(self.drawSpectrumAngleEntry.get())
    #     except ValueError:
    #         showerror("Ошибка!", "Некорректный угол")
    #         return
    #     if angleStep > 360 or angleStep < 0:
    #         showerror("Ошибка!", "Некорректный угол")
    #         return
    #
    #     width, height = self.getCanvasSize()
    #     xStart, yStart = self.decardToScreenCoordinates(0, 0, width, height)
    #
    #     result = list()
    #     angle = 0
    #     angleStep = angleToRadians(angleStep)
    #     while angle < 2 * math.pi:
    #         xEnd, yEnd = lineLen * math.cos(angle), lineLen * math.sin(angle)
    #         xEnd, yEnd = self.decardToScreenCoordinates(xEnd, yEnd, width, height)
    #
    #         result.append((xEnd, yEnd))
    #         angle += angleStep
    #
    #     method = self.drawSpectrumAlgComboBox.get()
    #     color = self.getSpectrumColor()
    #     for xEnd, yEnd in result:
    #         if method == "Цифровой дифференциальный анализатор":
    #             self.canvas.drawLine(digitalDiffAnalyzer(xStart, yStart, xEnd, yEnd), color)
    #         elif method == "Целочисленный алгоритм Брезенхема":
    #             self.canvas.drawLine(bresenhamInt(xStart, yStart, xEnd, yEnd), color)
    #         elif method == "Вещественный алгоритм Брезенхема":
    #             self.canvas.drawLine(bresenhamDouble(xStart, yStart, xEnd, yEnd), color)
    #         elif method == "Алгоритм Брезенхема с устранением ступенчатости":
    #             self.canvas.drawLineWithColor(bresenhamStairsReduce(xStart, yStart, xEnd, yEnd, color))
    #         elif method == "Алгоритм Ву":
    #             self.canvas.drawLineWithColor(wu(xStart, yStart, xEnd, yEnd, color))
    #         elif method == "Библиотечная функция":
    #             self.canvas.create_line(xStart, yStart, xEnd, yEnd, fill=color)

    @staticmethod
    def decardToScreenCoordinates(x, y, width, height):
        return int(x + width / 2), int(height / 2 - y)

    def changeCurveColor(self):
        color = self.drawCurveColorComboBox.get()
        if not color:
            return
        self.colorOfCurve.configure(bg=self.colors[color])

    def changeSpectrumColor(self):
        color = self.drawSpectrumColorComboBox.get()
        if not color:
            return
        self.colorOfSpectrum.configure(bg=self.colors[color])

    def getCanvasSize(self):
        return self.canvas.winfo_width(), self.canvas.winfo_height()

    def getCurveColor(self):
        return self.colors[self.drawCurveColorComboBox.get()]

    def changeSpectrumColor(self):
        color = self.drawSpectrumColorComboBox.get()
        if not color:
            return
        self.colorOfSpectrum.configure(bg=self.colors[color])

    def getSpectrumColor(self):
        return self.colors[self.drawSpectrumColorComboBox.get()]


app = App()
