from graphical_interface import window
from tkinter import *


def change_time():
    time_win = Toplevel(window)
    time_win.title('Change Time Window')
    lb = Label(time_win, text='Please Input the time (e.g.yyyy-mm-dd-hh-min): ')
    e = Entry(time_win)
    b = Button(time_win, text='Confirm', command=change)
    lb.pack()
    e.pack()
    b.pack()


def back_time():
    pass


def view_this():
    pass


def view_all():
    pass


def view_all_m():
    pass


def queue_time():
    pass
