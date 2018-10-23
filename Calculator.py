from tkinter import *
def add():
        x = e1.get()
        y = e2.get()
        d = int(x)
        e = int(y)
        r = d + e
        z = str(r)
        e3.insert(10,z)

def subtract():
        x = e1.get()
        y = e2.get()
        d = int(x)
        e = int(y)
        r = d - e
        z = str(r)
        e3.insert(10,z)

def multiply():
    x = e1.get()
    y = e2.get()
    d = int(x)
    e = int(y)
    r = d * e
    z = str(r)
    e3.insert(10, z)

def divide():
        x = e1.get()
        y = e2.get()
        d = int(x)
        e = int(y)
        r = d / e
        z = str(r)
        e3.insert(10, z)

def clear_textbox():
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
master = Tk()
master.title("Calculator")
Label(master, text="First Number").grid(row=0)
Label(master, text="Second Number").grid(row=1)
e1 = Entry(master, justify = 'center')
e2 = Entry(master, justify = 'center')
e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)
button = Button(master, text="+", fg = "black", height = 2, width = 5, command= add).grid(row = 2, column = 0)
button2 = Button(master, text="-", fg = "black", height = 2, width = 5, command = subtract).grid(row = 2, column = 1)
button3 = Button(master, text="X", fg = "black", height = 2, width = 5, command = multiply).grid(row = 2, column = 2)
button4 = Button(master, text="/", fg = "black", height = 2, width = 5, command = divide ).grid(row = 2, column = 3)
button5 = Button(master, text= "clear", fg = "black", height = 2, width = 5, command = clear_textbox).grid(row = 2, column = 4)
e3 = Entry(master, justify = 'center')
e3.grid(row = 4, column = 1)
Label(master, text= "Result!").grid(row = 4)
master.mainloop()
