import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkmsg
from typing import Tuple, List


class Table:
    def __init__(self, parent: tk.Frame,
                 headings: Tuple,
                 rows: List):
        self.table: ttk.Treeview = ttk.Treeview(parent, show="headings", selectmode="browse")
        self.table["columns"] = headings
        self.table["displaycolumns"] = headings

        for head in headings:  # Вставить колонки
            self.table.heading(head, text=head, anchor=tk.CENTER)
            self.table.column(head, anchor=tk.CENTER, width=0)

        for row, i in zip(rows, range(len(rows))):  # Вставить строки
            self.table.insert('', tk.END,
                         values=(i, *row) if (len(headings) - len(rows[i]) == 1) else row)

        # Добавить скролл
        scrolltable = tk.Scrollbar(master=parent, command=self.table.yview)
        self.table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)

        self.table.pack(expand=tk.YES, fill=tk.BOTH)

    def delRow(self):
        id: int = self.table.focus()
        if id:
            self.table.delete(id)
        else:
            tkmsg.showwarning("Ошибка!", "Перед удалением выберите нужную точку!")



root = tk.Tk()
root.geometry('1920x1080')

testFrame = tk.Frame(root, bg="#2b2b2b", bd=5)
testFrame.place(relx=0.0, rely=0.0, relwidth=0.25, relheight=1, anchor="nw")

tablea = Table(testFrame, headings=('№', 'x', 'y'), rows=[(31, 13), (31, 13), (31, 13),(31, 13), (31, 13), (31, 13),(31, 13), (31, 13), (31, 13),(31, 13), (31, 13), (31, 13),(31, 13), (31, 13), (31, 13),(31, 13), (31, 13), (31, 13),(31, 13), (31, 13), (31, 13),(31, 13), (31, 13), (31, 13),(31, 13), (31, 13), (31, 13),(31, 13), (31, 13), (31, 13),(31, 13), (31, 13), (31, 13),(31, 13), (31, 13), (31, 13),(31, 13), (31, 13), (31, 13),(31, 13), (31, 13), (31, 13),(31, 13), (31, 13), (31, 13),(31, 13), (31, 13), (31, 13),(31, 13), (31, 13), (31, 13),(31, 13), (31, 13), (31, 13), (31, 13), (31, 13), (31, 13)])

but = tk.Button(root, command=lambda: tablea.delRow())
but.place(relx=0.01, rely=0.46, relwidth=0.99, relheight=0.42, anchor="nw")

root.mainloop()
