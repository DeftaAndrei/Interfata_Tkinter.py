import tkinter as tk
import random

r = tk.Tk()
r.title('Stars')

canvas = tk.Canvas(r, width=800, height=800, bg='black')
canvas.pack()

for i in range(1, 100):
    x = random.randint(1, 800)
    y = random.randint(1, 800)
    canvas.create_oval(x, y, x+2, y+2, fill='white')  # Creștem dimensiunea punctului pentru o mai bună vizibilitate

r.mainloop()
