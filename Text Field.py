from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry("390x120+10+20")
win.title("Text Field")

# text field
t = Text(win, width= 28, height = 3)
t.place(x=80, y=30)

win.mainloop()
