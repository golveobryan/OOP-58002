from tkinter import *
window = Tk()
window.geometry("400x300+20+10")
window.title('Simple Calculator')

class MyWindow:
    def __init__(self,window):
        self.lbl1 = Label(window,text="Standard Calculator")
        self.lbl1.grid(relx=0.50,y=50,anchor="center")

        self.lbl2 = Label(window,text="Input 1st Number:")
        self.lbl2.grid(row = 1, column = 1, padx=2)
        self.lbl2.insert(0, "row 1, column 1")

        self.txtfld2 = Entry(window,bd=3)
        self.txtfld2.grid(x=180,y=80)

        self.lbl3 = Label(window,text="Input 2nd Number:")
        self.lbl3.grid(row = 2, column = 1, padx=2)
        self.lbl3.insert(0, "row 2, column 1")

        self.txtfld3=Entry(window,bd=3)
        self.txtfld3.grid(x=180,y=120)

        self.lbl4=Label(window,text="Choose from the Operators", fg="blue")
        self.lbl4.grid(x=50,y=150)

        self.btn1=Button(window,text="Addition(+)",command=self.add)
        self.btn1.grid(x=50,y=180)

        self.btn2 = Button(window,text="Subtraction(-)")
        self.btn2.grid(x=130,y=180)
        self.btn2.bind('<Button-1>',self.subtract)

        self.btn3=Button(window,text="Multiply(*)", command=self.multiply)
        self.btn3.grid(x=230,y=180)

        self.btn4=Button(window,text="Division(/)")
        self.btn4.grid(x=320,y=180)

        self.btn4.bind('<Button-1>',self.division)
        self.lbl5=Label(window,text="Result")
        self.lbl5.grid(x=50,y=230)

        self.txtfld4=Entry(window,bd=4)
        self.txtfld4.grid(x=180,y=230)

    def add(self):
        self.txtfld4.delete(0,'end')
        num1=int(self.txtfld2.get())
        num2=int(self.txtfld3.get())
        answer = num1+num2
        self.txtfld4.insert(END,answer)
    def subtract(self,event):
        self.txtfld4.delete(0,'end')
        num1=int(self.txtfld2.get())
        num2=int(self.txtfld3.get())
        answer = num1-num2
        self.txtfld4.insert(END,answer)
    def multiply(self):
        self.txtfld4.delete(0,'end')
        num1=int(self.txtfld2.get())
        num2=int(self.txtfld3.get())
        answer = num1*num2
        self.txtfld4.insert(END,answer)

    def division(self,event):
        self.txtfld4.delete(0,'end')
        num1=int(self.txtfld2.get())
        num2=int(self.txtfld3.get())
        answer = num1/num2
        self.txtfld4.insert(END,str(answer))

mywin = MyWindow(window)

window.mainloop()

