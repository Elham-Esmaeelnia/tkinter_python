from tkinter import *
import math


def calculate():
    try:
        num1 = float(enter1.get())
        num2 = float(enter2.get())
        result = num1 * num2
        label3.config(text=str(result))
    except ValueError:
        label3.config(text='Enter numeric values!')


def calculate2():
    try:
        num1 = float(enter1.get())
        num2 = float(enter2.get())
        result = num1 / num2
        label3.config(text=str(result))
    except ValueError:
        label3.config(text='Enter numeric values!')


def calculate3():
    try:
        num1 = float(enter1.get())
        num2 = float(enter2.get())
        result = num1 + num2
        label3.config(text=str(result))
    except ValueError:
        label3.config(text='Enter numeric values!')


def calculate4():
    try:
        num1 = float(enter1.get())
        num2 = float(enter2.get())
        result = num1 - num2
        label3.config(text=str(result))
    except ValueError:
        label3.config(text='Enter numeric values!', fg="white")


def calculate5():
    try:
        num1 = float(enter1.get())
        result = num1 ** 2
        label3.config(text=str(result))
    except ValueError:
        label3.config(text='Enter numeric values!', fg="white")


def calculate6():
    try:
        num1 = float(enter1.get())
        result = math.sqrt(num1)
        label3.config(text=str(result))
    except ValueError:
        label3.config(text='Enter numeric values!', fg="white")


root = Tk()
root.configure(background='black')
label1 = Label(root, text='عدد اول', bg="black", fg="white")
label1.grid(row=0, column=0, columnspan=2)
enter1 = Entry(root, bg='white')
enter1.grid(row=1, column=0, columnspan=2)
label2 = Label(root, text='عدد دوم', bg="black", fg="white")
label2.grid(row=2, column=0, columnspan=2)
enter2 = Entry(root, bg='white')
enter2.grid(row=3, column=0, columnspan=2)
btn1 = Button(root, text='ضرب', command=calculate, bg="black", activebackground="green", fg="white")
btn1.grid(row=4, column=0)
btn2 = Button(root, text='تقسیم', command=calculate2, bg="black", activebackground="orange", fg="white")
btn2.grid(row=5, column=0)
btn3 = Button(root, text='جمع', command=calculate3, bg="black", activebackground="purple", fg="white")
btn3.grid(row=5, column=1)
btn4 = Button(root, text='تفریق', command=calculate4, bg="black", activebackground="red", fg="white")
btn4.grid(row=4, column=1)
btn5 = Button(root, text='توان ۲ عدد اول', command=calculate5, bg="black", activebackground="cyan", fg="white")
btn5.grid(row=6, column=0, columnspan=2)
btn6 = Button(root, text='ریشه عدد اول', command=calculate6, bg="black", activebackground="yellow", fg="white")
btn6.grid(row=7, column=0, columnspan=2, )
label3 = Label(root, bg="black", fg="red")
label3.grid(row=8, column=0, columnspan=2)
enter1.focus()
enter1.bind('<Return>', func=lambda e: enter2.focus_set())
root.mainloop()




