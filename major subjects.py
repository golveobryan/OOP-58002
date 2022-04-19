from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry("330x105+10+20")
win.title("Major Subjects")

lstbx = Listbox(win, selectmode= 'single', height=5)
data = "reading"
data1 = "writing"
data2 = "arithmetic"
data3 = "coding"
lstbx.insert(END,data)
lstbx.insert(END,data1)
lstbx.insert(END,data2)
lstbx.insert(END,data3)
lstbx.place(x=100, y=10)

win.mainloop()