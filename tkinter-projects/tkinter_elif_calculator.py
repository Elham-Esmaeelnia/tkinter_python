from tkinter import *
from tkinter import messagebox
import math

sufra= Tk()
sufra.configure(background='#FF339F')
sufra.title("ماشین حساب")

def show():
  try:
     a =asq .get()
     b = bsq.get()
     o = op.get()
     if o == '+':
        csq = a + b
        messagebox.showinfo("جواب ", csq)
     elif o == '-':
        csq = a - b
        messagebox.showinfo("جواب ", csq)
     elif o == '*':
        csq = a * b
        messagebox.showinfo("جواب", csq)
     elif o == '/':
        csq = a / b
        messagebox.showinfo("جواب", csq)
     else:
        print('بیشتر')
  except ValueError:
        tkMessageBox.showinfo("خطا!")
asq=IntVar()
bsq=IntVar()
op=StringVar()
k= Label(sufra, text="ماشین حساب ساده",background='#FF339F').grid(row=0, column=1)
E1 = Entry(sufra, bd =5,textvariable = asq).grid(row=1, column=0)
L1 = Label(sufra, text="عدد اول ",background='#FF339F').grid(row=1, column=1)
E3 = Entry(sufra, bd =5,textvariable = op).grid(row=2, column=0)
L2 = Label(sufra, text="(*/-+) ",background='#FF339F').grid(row=2, column=1)
E2 = Entry(sufra, bd =5,textvariable = bsq).grid(row=3, column=0)
L3 = Label(sufra, text="عدد دوم ",background='#FF339F').grid(row=3, column=1)

B1 = Button(sufra, text="لطفا حاصل را نمایش بده",background='#FFDA33' ,command = show).grid(row=4, column=0)
sufra.mainloop()