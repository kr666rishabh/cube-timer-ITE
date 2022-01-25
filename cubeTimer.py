# importing Tkinter, a standard GUI library for Python
from tkinter import *
from tkinter.ttk import *
# importing Tkinter, a standard GUI library for Python

# Declaring required variables
ms = 0
s = 0
m = 0
h = 0
pause = 0

min = int(360000)
solves = ["s1", "s2", "s3", "s4", "s5"]
i = 0
yAxis = 50
# Declaring required variables


# 'start' function, which (starts the timer and updates displayed time)


def start():
    global ms, s, m, h, yAxis
    ms += 1
    if (ms == 99):
        s += 1
        ms = 0
    if (s == 59):
        m += 1
        s = 0
    if (m == 59):
        h += 1
        m = 0
    if (pause == 0):
        solves[i] = Label(root, text='%i:%i:%i:%i' %
                          (h, m, s, ms), font=('arial', 15, 'bold'), foreground='darkviolet', background='silver', width=10)
        solves[i].after(4, start)
        solves[i].place(x=110, y=yAxis)
# 'start' function, which (starts the timer and updates displayed time)

# 'stop' function, which (stops timer), (checks and updates the minimum time)


def stop():
    global pause, min
    pause = 1
    if (min > ((h*60*60*100)+(m*60*100)+(s*100)+(ms))):
        min = (h*60*60*100)+(m*60*100)+(s*100)+(ms)
        minimum = Label(root, text='%i:%i:%i:%i' %
                        (h, m, s, ms), font=('arial', 15, 'bold'), foreground='darkviolet', background='silver', width=10)
        minimum.after(300, start)
        minimum.place(x=110, y=200)
# 'stop' function, which (stops timer), (checks and updates the minimum time)

# 'new' function, which (changes the solve count and its position), (turns 'Start' button functional), (sets timer to zero)


def new():
    global i, pause, yAxis, ms, s, m, h
    i += 1
    pause = 0
    yAxis += 30
    ms = 0
    s = 0
    m = 0
    h = 0
# 'new' function, which (changes the solve count and its position), (turns 'Start' button functional), (sets timer to zero)


# Declaring properties (name, shape, etc) of the application window
root = Tk()  # To initialize tkinter, we create a Tk root widget, seen as a window
root.title("Cube Timer")
root.geometry("300x300")
root.configure(bg="silver")

style = Style()
style.configure('Tbutton', font=('arial', 12, 'bold'), borderwidth='500')
# Declaring properties (name, shape, etc) of the application window

# 'Start', 'Stop', and 'New' buttons
Start = Button(root, text="Start", command=start).place(x=10, y=10)
Stop = Button(root, text="Stop", command=stop).place(x=100, y=10)
New = Button(root, text="New", command=new).place(x=200, y=10)
# 'Start', 'Stop', and 'New' buttons

# Constant label of minimum time
Min = Label(root, text="Min Time- ", font=('arial', 15, 'bold'),
            foreground='darkviolet', background='silver')
Min.place(x=10, y=200)
# Constant label of minimum time

# Constant labels of 5 solves
s1 = Label(root, text="Solve 1- ", font=('arial', 15, 'bold'),
           foreground='darkviolet', background='silver')
s1.place(x=10, y=50)
s2 = Label(root, text="Solve 2- ", font=('arial', 15, 'bold'),
           foreground='darkviolet', background='silver')
s2.place(x=10, y=80)
s3 = Label(root, text="Solve 3- ", font=('arial', 15, 'bold'),
           foreground='darkviolet', background='silver')
s3.place(x=10, y=110)
s4 = Label(root, text="Solve 4- ", font=('arial', 15, 'bold'),
           foreground='darkviolet', background='silver')
s4.place(x=10, y=140)
s5 = Label(root, text="Solve 5- ", font=('arial', 15, 'bold'),
           foreground='darkviolet', background='silver')
s5.place(x=10, y=170)
# Constant labels of 5 solves

root.mainloop()
