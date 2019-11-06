from tkinter import *
from datetime import datetime
import tkinter.messagebox


def change_time():
    def confirm_to_change():
        lst = inp.get().split('-')
        print(lst)
        for i in range(5):
            TIME[i] = int(lst[i])  # len(TIME) should be 5, and TIME cannot be tuple
        TIME[5] = datetime.strptime(lst[0]+' '+lst[1]+' '+lst[2], '%Y %m %d').strftime('%A')
        time_str.set('{:04d}-{:02d}-{:02d} {:02d}:{:02d}, {:}'.format(TIME[0], TIME[1], TIME[2], TIME[3], TIME[4],
                                                                      TIME[5]))
        tkinter.messagebox.showinfo('Complete!', 'Time has been changed successfully!')
        w.destroy()
        def update_info():
            pass

    w = Toplevel(window)
    w.title('Change Time Window')
    l = Label(master=w, text='Please input the time (yyyy-mm-dd-hh-min  e.g 2000-10-23-00-00)')
    l.pack()
    inp = Entry(master=w)
    inp.pack()
    confirm = Button(master=w, text='Confirm', command=confirm_to_change)
    confirm.pack()


def back_time():
    tmp = datetime.now()
    TIME = [tmp.year, tmp.month, tmp.day, tmp.hour, tmp.minute, tmp.strftime('%A')]
    time_str.set('{:04d}-{:02d}-{:02d} {:02d}:{:02d}, {:}'.format(TIME[0], TIME[1], TIME[2], TIME[3], TIME[4],
                                                                  TIME[5]))
    tkinter.messagebox.showinfo('Complete!', 'Displayed time is now back to the current time.')


def view_this():
    for widget in info.winfo_children():
        widget.destroy()
    heading = Label(master=info, text='Menu')
    heading.pack()
    a = Listbox(master=info)
    m = get_menu(name_selected, tttt)  # name_selected: the name of the function, tttt: time
    display = Listbox(master=info)
    for x in m:
        display.insert('end', x)
    display.pack()
    op = get_op()  # function
    op_label = Label(master=info, text='Operating Hour: '+op, font='Georgia 16 bold ')
    op_label.pack()


def view_all():
    tkinter.messagebox.showinfo('Notes', 'You are viewing all stalls and menus, regardless of time.\
                                         To quit this mode, by either click to select a time or going back to the current \
                                          time.')
    time_str.set('State: Viewing All Stalls and Menus')
    s_list = get_all_s()
    def update_s():
        for widget in stalls.winfo_children():
            widget.destroy()
        s_title = StringVar()
        s_title.set('View All the Stalls')
        title_s = Label(master=stalls, textvariable=s_title, font='Georgia 18 bold ')
        title_s.pack()
        s = Listbox(master=stalls, selectmode='SINGLE')
        for x in s_list:
            s.insert('end', x)
        s.pack()

    update_s()


def view_all_m():
    for widget in info.winfo_children():
        widget.destroy()
    heading = Label(master=info, text='Complete Version of Menu', font='Georgia 18 bold ')
    heading.pack()
    a = Listbox(master=info)
    m = get_menu_all()  # Tan Wee Li
    display = Listbox(master=info)
    for x in m:
        display.insert('end', x)
    display.pack()
    op = get_op()  # Tan Wee Li
    op_label = Label(master=info, text='Operating Hour: '+op, font='Georgia 16 underline')
    op_label.pack()


def queue_time():
    w = Toplevel(window)
    w.title('Calculate Queue Time')
    l = Label(master=w, text='Please input the number of queueing people (e.g. 8): ')
    l.pack()
    inp = Entry(master=w)
    inp.pack()

    def confirm_to_change():
        t = queue(int(inp.get()))
        tkinter.messagebox.showinfo('Queue Time Result', 'The expected queue time is {} min.'.format(t))
        w.destroy()
    confirm = Button(master=w, text='Confirm', command=confirm_to_change)
    confirm.pack()


if __name__ == '__main__':
    s_list = ['Cantonese Roast Duck Rice', 'Salad', 'Soup Delight', 'McDonald\'s']

    def get_menu():
        if s.get(s.curselection()) == 'Cantonese Roast Duck Rice':
            return ['Roast Duck Rice', 'Roast Duck Noodle', 'Cha Siew Rice']
        elif s.get(s.curselection()) == 'Salad':
            return ['Onion', 'Pasta', 'Egg']

    def get_menu_all():
        return ['1', '2', '3', '4', '5']


    def get_op():
        if s.get(s.curselection())== 'Cantonese Roast Duck Rice':
            return '9:00-21:00'
        elif s.get(s.curselection()) == 'Salad':
            return '9:30-20:00'


    def get_all_s():
        return ['Cantonese Roast Duck Rice', 'Salad', 'Soup Delight', 'McDonald\'s', 'Chicken Rice']


    def queue(num):
        return 8*num


window = Tk()
window.title('Real Time Canteen Information System')
window.resizable(False, False)
# variable 
TIME = [2000, 10, 23, 12, 00, 'Monday'] # [yyyy, mm, dd, hh, min, weekday()]
# s_list = get_stalls(TIME.year, TIME.month, TIME.day)  # Tan Wee Li

# area 1.1, logo 
logo = Frame(window)
logo.grid(row=1, column=1)
app_name = Label(master=logo, text='Canteen A Real-time Information System', font='Georgia 20 bold')
app_name.pack()
Logo = Canvas(master=logo, height=150, width=300)
Logo.pack()
img_file = PhotoImage(file='NTULogo.png')
Logo.create_image(20, 10, anchor=NW, image=img_file)

# area 1.2, time
time = Frame(window)
time.grid(row=1, column=2)
t_l = Label(master=time, text='Displayed Time\t', font='Georgia 18 bold ')
t_l.grid(row=1, column=1)
time_str = StringVar()
time_str.set(datetime.now().strftime('%Y-%m-%d %H:%M, %A'))
time_shown = Label(master=time, textvariable=time_str, font='Georgia 16 underline', fg='red')
time_shown.grid(row=2, column=1)
time_change = Button(master=time, text='Change Displayed Time', command=change_time)
time_change.grid(row=1, column=2)
time_back = Button(master=time, text='Back to Current Time', command=back_time)
time_back.grid(row=2, column=2)

# area 2.1, list of stalls
stalls = Frame(window)
stalls.grid(row=2, column=1)
s_title = StringVar()
s_title.set('Open Stalls at Displayed Time')
title_s = Label(master=stalls, textvariable=s_title, font='Georgia 18 bold ')
title_s.pack()
s = Listbox(master=stalls, selectmode='SINGLE')
for x in s_list:
    s.insert('end', x)
s.pack()

# area 2.2, information display area
info = Frame(window)
info.grid(row=2, column=2)
title_info = Label(master=info, text='Click One Stall to View More Information', font='Georgia 13 italic')
title_info.pack()

# area 3.1, buttons on the left
b1 = Frame(window)
b1.grid(row=3, column=1)
view_t = Button(master=b1, text='View Information of Selected Stall', command=view_this)
view_t.pack()
view_a = Button(master=b1, text='View List of All Stalls', command=view_all)
view_a.pack()

# area 3.2, buttons on the right
b2 = Frame(window)
b2.grid(row=3, column=2)
view_tm = Button(master=b2, text='View All Menus', command=view_all_m)
view_tm.pack()
q = Button(master=b2, text='Calculate Queue Time', command=queue_time)
q.pack()

window.mainloop()
