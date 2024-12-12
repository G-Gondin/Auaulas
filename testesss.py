from tkinter import *
jan = Tk()
jan.geometry("400x400+680+320")
lay = Frame(jan)

def muda():
    lb1 = Label(lay, text="Texto 1").grid()
    lb2 = Label(lay, text="Texto 2").grid()
    lb3 = Label(lay, text="Texto 3").grid()
    lay.grid()

bt = Button(jan, text="Mudar", command="muda").grid()
if Event == "muda":
    lay.grid()


jan.mainloop()
