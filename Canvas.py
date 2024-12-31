from tkinter import *
master = Tk()

master.title('Iza')
master.geometry('800x600')
master.configure(bg='grey')
master.resizable(False, False)
master.maxsize(800, 600)


w = Canvas(master, width=150, height=300, bg='black')
w.pack()

canvas_height=30
canvas_weight=200
y = int(canvas_height / 2)

w.create_line(0,y,canvas_weight,y)
mainloop()

