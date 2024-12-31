import  tkinter as tk 
root = tk.Tk()

root.title("Deftronic")
root.geometry("800x500")

#Si acum sa o facem sa se vada pe tot ecranu
root.attributes("-fullscreen", True)

root.mainloop() 
def exit_fullscreen(event=None):
    root.attributes('-fullscreen', False)

root.bind("<Escape>", exit_fullscreen)
