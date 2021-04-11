import tkinter as tk

# Создать окно
root = tk.Tk()
root.geometry('1920x1080')

# Создать фреймы
Frame = tk.Frame(root, bg="#2b2b2b")
Frame.place(relx=0.0, rely=0.0, relwidth=1, relheight=1, anchor="nw")

Canvas = tk.Canvas(root)
Canvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

dots = [[330.730316, 834.634827],
[330.730316, 765.365173],
[469.269684, 765.365173],
[469.269684, 834.634827],
[356.706451, 821.646790],
[356.706451, 778.353210],
[443.293549, 778.353210],
[443.293549, 821.646790]]

connections = [[1, 2],
               [2, 3],
               [3, 4],
               [4, 1],
               [5, 6],
               [6, 7],
               [7, 8],
               [8, 5],
               [1, 5],
               [2, 6],
               [3, 7],
               [4, 8]]

for i in connections:
    print(f"Линия - из {dots[i[0] - 1][0]}, {dots[i[0] - 1][1]} -в- {dots[i[1] - 1][0]}, {dots[i[1] - 1][1]}")
    Canvas.create_line(dots[i[0] - 1][0], dots[i[0] - 1][1], dots[i[1] - 1][0], dots[i[1] - 1][1], fill="green",
                       width="2")

Canvas.create_line(1, 1, 100, 100, fill="green", width="2")

root.mainloop()
