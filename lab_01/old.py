import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

figure = plt.figure()

canvas = FigureCanvasTkAgg(figure, master=plotFrame)
plotWidget = canvas.get_tk_widget()
canvas.tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)



plt.plot(x,y)

x: List[float] = []
for i in range(0, 500):
    x.append(i/10)
y: List[float] = []
for i in x:
    y.append(-sin(i))
# plt.plot(x,y)