import tkinter as tk
from tkinter import *

r = tk.Tk()
r.title('Destroy')
r.geometry('500x400')
r.configure(bg='light blue')


var1 = IntVar()
var2 = IntVar()

# Checkbutton-uri
Checkbutton(r, text='A', variable=var1).grid(row=0, column=0, sticky=W, padx=10, pady=5)
Checkbutton(r, text='B', variable=var2).grid(row=1, column=0, sticky=W, padx=10, pady=5)

# Butonul "Destroy"
button = tk.Button(r, text='Destroy', width=25, command=r.destroy)
button.grid(row=2, column=0, pady=20)

r.mainloop()
