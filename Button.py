from tkinter import Tk, Frame, BOTH, LEFT
from tkinter.ttk import Button
from tkinter import messagebox

master = Tk()

pane = Frame(master)
pane.pack(fill=BOTH, expand=True)

# Primul buton
b1 = Button(pane, text="Pompm", command=lambda: messagebox.showinfo("Pompm", "Pompm"))
b1.pack(side=LEFT, padx=5, pady=5)

# Al doilea buton
b2 = Button(pane, text="Pompm", command=lambda: messagebox.showinfo("Pompm", "Pompm"))
b2.pack(fill=BOTH, expand=True)

master.mainloop()
