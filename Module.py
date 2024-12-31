from tkinter import *
from tkinter.ttk import *

root = Tk()

root.title("Deftronic")
root.geometry("800x500")
root.configure(bg="black")
root.focus_set()

b1 = Button(root, text="Green")
b1.place(relx = 1,x = -2 , y = 2 , anchor=NE)
b1.configure(command=lambda: root.configure(bg="green"))


b2 = Button(root, text="Red")
b2.place(relx = 0.5,rely = 0.5, anchor=CENTER)


mainloop()