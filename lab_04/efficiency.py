from drawer import Drawer
from draw_backend import *
import time
import matplotlib.pyplot as plt
import numpy as np


#                 "Каноническое уравнение",
#                 "Параметрическое уравнение",
#                 "Алгоритм Брезенхема",
#                 "Алгоритм средней точки",
#                 "Библиотечная функция"

def compareCircleTime():
    rList = [10, 100, 200, 300, 400, 500]
    xStart, yStart = 1, 1

    normalStore = list()
    parameterStore = list()
    bresStore = list()
    middleStore = list()
    libStore = list()

    drawer = Drawer(None, "white")
    modifier = 1000
    repeats = 5

    def testNormal(x0, y0, r, color="#FF0000"):
        timeBegin = time.time()
        for i in range(repeats):
            drawer.drawLine(drawCircleNormal(x0, y0, r), color)
        timeEnd = time.time()
        normalStore.append(int((timeEnd - timeBegin) * modifier))

    def testParameter(x0, y0, r, color="#FF0000"):
        timeBegin = time.time()
        for i in range(repeats):
            drawer.drawLine(drawCircleParameter(x0, y0, r), color)
        timeEnd = time.time()
        parameterStore.append(int((timeEnd - timeBegin) * modifier))

    def testBres(x0, y0, r, color="#FF0000"):
        timeBegin = time.time()
        for i in range(repeats):
            drawer.drawLine(drawCircleBresenham(x0, y0, r), color)
        timeEnd = time.time()
        bresStore.append(int((timeEnd - timeBegin) * modifier))

    def testMiddle(x0, y0, r, color="#FF0000"):
        timeBegin = time.time()
        for i in range(repeats):
            drawer.drawLine(drawCircleMiddlePoint(x0, y0, r), color)
        timeEnd = time.time()
        middleStore.append(int((timeEnd - timeBegin) * modifier))

    def testLib(x0, y0, r, color="#FF0000"):
        timeBegin = time.time()
        for i in range(repeats):
            drawer.create_oval(x0 - r, y0 - r, x0 + r, y0 + r, outline=color)
        timeEnd = time.time()
        libStore.append(int((timeEnd - timeBegin) * modifier))

    for r in rList:
        testNormal(xStart, yStart, r)
        testParameter(xStart, yStart, r)
        testBres(xStart, yStart, r)
        testMiddle(xStart, yStart, r)
        testLib(xStart, yStart, r)

    barWidth = 0.4 / 3
    x1 = np.arange(1, 7) - barWidth * 3
    x2 = np.arange(1, 7) - barWidth * 2
    x3 = np.arange(1, 7) - barWidth
    x4 = np.arange(1, 7)
    x5 = np.arange(1, 7) + barWidth
    y1 = normalStore
    y2 = parameterStore
    y3 = bresStore
    y4 = middleStore
    y5 = libStore

    fig, ax = plt.subplots()
    ax.set_title(f"Сравнение времени на окружностях радиуса {rList} (в с * {modifier})")
    ax.bar(x1, y1, width=barWidth, label="Каноническое уравнение")
    ax.bar(x2, y2, width=barWidth, label="Параметрическое уравнение")
    ax.bar(x3, y3, width=barWidth, label="Алгоритм Брезенхема")
    ax.bar(x4, y4, width=barWidth, label="Алгоритм средней точки")
    ax.bar(x5, y5, width=barWidth, label="Библиотечная функция")

    ax.legend()
    ax.set_facecolor('seashell')
    fig.set_figwidth(12)  # ширина Figure
    fig.set_figheight(6)  # высота Figure
    fig.set_facecolor('floralwhite')

    print(f"Каноническое уравнение", normalStore)
    print(f"Параметрическое уравнение", parameterStore)
    print(f"Алгоритм Брезенхема", bresStore)
    print(f"Алгоритм средней точки", middleStore)
    print(f"Библиотечная функция", libStore)

    plt.show()


def compareEllipseTime():
    rhList = [10, 100, 200, 300, 400, 500]
    rwList = [30, 300, 600, 900, 1200, 1500]
    xStart, yStart = 1, 1

    normalStore = list()
    parameterStore = list()
    bresStore = list()
    middleStore = list()
    libStore = list()

    drawer = Drawer(None, "white")
    modifier = 1000
    repeats = 5

    def testNormal(x0, y0, rw, rh, color="#FF0000"):
        timeBegin = time.time()
        for i in range(repeats):
            drawer.drawLine(drawEllipseNormal(x0, y0, rw, rh), color)
        timeEnd = time.time()
        normalStore.append(int((timeEnd - timeBegin) * modifier))

    def testParameter(x0, y0, rw, rh, color="#FF0000"):
        timeBegin = time.time()
        for i in range(repeats):
            drawer.drawLine(drawEllipseParameter(x0, y0, rw, rh), color)
        timeEnd = time.time()
        parameterStore.append(int((timeEnd - timeBegin) * modifier))

    def testBres(x0, y0, rw, rh, color="#FF0000"):
        timeBegin = time.time()
        for i in range(repeats):
            drawer.drawLine(drawEllipseBresenham(x0, y0, rw, rh), color)
        timeEnd = time.time()
        bresStore.append(int((timeEnd - timeBegin) * modifier))

    def testMiddle(x0, y0, rw, rh, color="#FF0000"):
        timeBegin = time.time()
        for i in range(repeats):
            drawer.drawLine(drawEllipseMiddlePoint(x0, y0, rw, rh), color)
        timeEnd = time.time()
        middleStore.append(int((timeEnd - timeBegin) * modifier))

    def testLib(x0, y0, rw, rh, color="#FF0000"):
        timeBegin = time.time()
        for i in range(repeats):
            drawer.create_oval(x0 - rw, y0 - rh, x0 + rw, y0 + rh, outline=color)
        timeEnd = time.time()
        libStore.append(int((timeEnd - timeBegin) * modifier))

    for rW, rH in zip(rwList, rhList):
        testNormal(xStart, yStart, rW, rH)
        testParameter(xStart, yStart, rW, rH)
        testBres(xStart, yStart, rW, rH)
        testMiddle(xStart, yStart, rW, rH)
        testLib(xStart, yStart, rW, rH)

    barWidth = 0.4 / 3
    x1 = np.arange(1, 7) - barWidth * 3
    x2 = np.arange(1, 7) - barWidth * 2
    x3 = np.arange(1, 7) - barWidth
    x4 = np.arange(1, 7)
    x5 = np.arange(1, 7) + barWidth
    y1 = normalStore
    y2 = parameterStore
    y3 = bresStore
    y4 = middleStore
    y5 = libStore

    fig, ax = plt.subplots()
    ax.set_title(f"Сравнение времени на эллипсах радиусами {rwList}, {rhList} (в с * {modifier})")
    ax.bar(x1, y1, width=barWidth, label="Каноническое уравнение")
    ax.bar(x2, y2, width=barWidth, label="Параметрическое уравнение")
    ax.bar(x3, y3, width=barWidth, label="Алгоритм Брезенхема")
    ax.bar(x4, y4, width=barWidth, label="Алгоритм средней точки")
    ax.bar(x5, y5, width=barWidth, label="Библиотечная функция")

    ax.legend()
    ax.set_facecolor('seashell')
    fig.set_figwidth(12)  # ширина Figure
    fig.set_figheight(6)  # высота Figure
    fig.set_facecolor('floralwhite')

    print(f"Каноническое уравнение", normalStore)
    print(f"Параметрическое уравнение", parameterStore)
    print(f"Алгоритм Брезенхема", bresStore)
    print(f"Алгоритм средней точки", middleStore)
    print(f"Библиотечная функция", libStore)

    plt.show()
