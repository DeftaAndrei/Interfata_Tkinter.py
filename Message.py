from tkinter import *
main = Tk() 

main.title('Destroy')
main.geometry('500x400')
main.configure(bg='light blue')
main.aspect(1, 1, 1, 1)
Message(main, text='I am Destroyer', bg='light blue', font=('Arial', 24)).pack()




main.mainloop()