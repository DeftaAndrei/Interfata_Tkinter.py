from tkinter import *

# Setare fereastră principală
root = Tk()
root.title('4Buttons')

root.geometry('600x800')
root.configure(bg='gray')
root.resizable(False, False)
root.maxsize(600, 800)

# Funcții pentru schimbarea culorii de fundal
def change_to_red():
    root.configure(bg='darkred')

def change_to_green():
    root.configure(bg='darkgreen')

def change_to_blue():
    root.configure(bg='darkblue')

def change_to_black():
    root.configure(bg='black')

# Stil pentru butoane
button_style = {
    'bg': '#003366',  # Albastru într-un ton mai încis
    'highlightbackground': '#99ccff',  # Contur albastru foarte deschis
    'highlightthickness': 2,
    'fg': 'white',  # Text alb pentru contrast
    'width': 10,
    'height': 2
}

# Butoane pentru schimbarea culorii
redbutton = Button(root, text='Red', command=change_to_red, **button_style)
redbutton.place(x=10, y=10)  # Stânga sus

greenbutton = Button(root, text='Green', command=change_to_green, **button_style)
greenbutton.place(x=520, y=10)  # Dreapta sus

bluebutton = Button(root, text='Blue', command=change_to_blue, **button_style)
bluebutton.place(x=10, y=750)  # Stânga jos

blackbutton = Button(root, text='Black', command=change_to_black, **button_style)
blackbutton.place(x=520, y=750)  # Dreapta jos

# Rulare aplicație
root.mainloop()
