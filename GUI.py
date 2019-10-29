from tkinter import *
from datetime import datetime
import tkinter.messagebox


def time_converter():
    global TIME
    t = TIME.get()
    t_list = t.split('-')
    return (t_list[0], t_list[1], t_list[2], t_list[3], t_list[4])


def time_window():
    global e, time_win
    time_win = Toplevel(window)
    time_win.title('Change Time Window')
    lb = Label(time_win, text='Please Input the time (e.g.yyyy-mm-dd-hh-min): ')
    e = Entry(time_win)
    b = Button(time_win, text='Confirm', command=change_time)
    lb.pack()
    e.pack()
    b.pack()


def change_time():
    global e, TIME, time_win
    text = e.get().split('-')
    TIME.set("{}-{}-{} {}:{}".format(text[0], text[1], text[2], text[3], text[4]))
    time_win.destroy()


def to_current():
    TIME.set(datetime.now().strftime('%Y-%m-%d %H:%M'))
    tkinter.messagebox.showinfo('Complete!', 'The time has been changed to the current time.')


def queue_time():
    global e1, queue_win
    queue_win = Toplevel(window)
    queue_win.title('Calculate the queue time of the stall')
    lb = Label(queue_win, text='Please Input the number of people queueing (e.g. 8): ')
    e1 = Entry(queue_win)
    b = Button(queue_win, text='Confirm', command=cal_queue)
    lb.pack()
    e1.pack()
    b.pack()


def cal_queue():
    global e1, queue_win
    num = e1.get()
    result = 8  # CHANGE
    tkinter.messagebox.showinfo('Queue time', 'The queue time is {}'.format(result))
    queue_win.destroy()


def SeeAll():
    global all_state


if __name__ == '__main__':
    stalls_list = ['Cantonese Roast Duck', 'Salad', 'Soup Delight']
    menu = ['Roast Duck Rice', 'Roast Duck Soup']
    operating_hour = ('9:30', '21:00')

window = Tk()
window.title('Real-time Canteen Information System')

# initialize 
all_state = False 

# time display area
# TIME = StringVar()
# TIME.set(datetime.now().strftime('%Y-%m-%d %H:%M'))
TIME = StringVar()
TIME.set(datetime.now().strftime('%Y-%m-%d %H:%M'))
time = Label(master=window, state='disabled', textvariable=TIME)
# change time
time_change = Button(window, text='Change Time', command=time_window)
back_to_current = Button(window, text='Change the Time to Current', command=to_current)

# Stall Display Area
stall_list = StringVar()
stall_list.set(tuple([x for x in stalls_list]))
stalls = Listbox(window, selectmode='SINGLE', listvariable=stall_list)

# Information Display Area
t1 = Text(window)
info_heading = Label(master=window, text='Information of Stall')
t1.insert('end', '\n')
t1.insert('end', 'Menu\n')
for x in menu:
    t1.insert('end', x+'\n')
t1.insert('end', '\n')
t1.insert('end', 'Operating Hour: {}-{}'.format(operating_hour[0], operating_hour[1]))
t1.config(state=DISABLED)

# queue time
queue = Button(window, text='Calculate Queue Time', command=queue_time)

# See all stalls' information
see_all = Button(master=window, text='See All Stall\'s Information', command=SeeAll)

# layout

window.mainloop()

# dynamic update of information
# while True:
#    sleep(60)
#    time['text'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#    window.update()