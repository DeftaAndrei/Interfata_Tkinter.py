from tkinter import *
master = Tk()
master.title('Iza')
master.geometry('800x600')
master.configure(bg='grey')
master.resizable(False, False)
master.maxsize(800, 600)

w = Scale (master , from_= 0 ,to=45)

w.pack()

W = Scale (master , from_= 0 ,to=200 , orient=HORIZONTAL)
W.pack()

mainloop() 