from tkinter import *
from datetime import datetime
import tkinter.messagebox
from stall import get_stall, get_operating_hour
from queuetime import waiting_time
from store2 import get_menu


def change_time():
    global mode

    def confirm_to_change_time():
        tmp_list = input_time.get().split('-')  # demo: ['2000', '10', '23', '00', '00']
        try:
            for i in range(5):
                TIME[i] = int(tmp_list[i])
            TIME[5] = int(datetime.strptime(tmp_list[0]+' '+tmp_list[1]+' '+tmp_list[2], '%Y %m %d').strftime('%w'))
            wkd = datetime.strptime(tmp_list[0]+' '+tmp_list[1]+' '+tmp_list[2], '%Y %m %d').strftime('%A')
            # [2000, 10, 23, 00, 30, 1]
        except:
            tkinter.messagebox.showinfo('Error', 'Please input the valid date according to the format!')
        else:
            tkinter.messagebox.showinfo('Success', 'The time has been changed successfully')
            time_str.set('{:4d}-{:2d}-{:2d} {:02d}:{:02d} {}'.format(TIME[0], TIME[1], TIME[2], TIME[3], TIME[4], wkd))
            stall_update()
        finally:
            w_time.destroy()
    mode = 0  # quit the view-all-mode
    w_time = Toplevel(window)
    w_time.title('Change Time Window')
    l_time = Label(master=w_time, text='Please input the time (yyyy-mm-dd-hh-min  e.g 2000-10-23-00-00)')
    l_time.pack()
    input_time = Entry(master=w_time)
    input_time.pack()
    confirm_time = Button(master=w_time, text='Confirm', command=confirm_to_change_time)
    confirm_time.pack()


def back_to_current():
    global mode, z, TIME
    z = datetime.now()
    TIME = [z.year, z.month, z.day, z.hour, z.minute, z.weekday()]
    mode = 0
    stall_update()


def stall_update():
    global st
    for widget in stalls.winfo_children():  # initialize the frame whenever updated
        widget.destroy()
    if mode == 1:
        s_title.set('State: Viewing All Stalls and Menus')
    else:
        s_title.set('Open Stalls at Displayed Time')
    title_s = Label(master=stalls, textvariable=s_title, font='Georgia 18 bold ')
    title_s.pack()
    st = Listbox(master=stalls, selectmode='SINGLE')
    s_list = get_stall(TIME, mode)
    print(s_list)
    if s_list:
        for x in s_list:
            st.insert('end', x)
    else:
        s_title.set('No open stalls currently')
    st.pack()


def queue_time():
    def confirm_to_change():
        t = waiting_time(inp.get())
        if t: 
            tkinter.messagebox.showinfo('Queue Time Result', 'The expected queue time is {} min.'.format(t))
        else:
            tkinter.messagebox.showinfo('Error!', 'Please input the valid number.')
        w.destroy()

    w = Toplevel(window)
    w.title('Calculate Queue Time')
    l = Label(master=w, text='Please input the number of queueing people (e.g. 8): ')
    l.pack()
    inp = Entry(master=w)
    inp.pack()
    confirm = Button(master=w, text='Confirm', command=confirm_to_change)
    confirm.pack()


def view():
    for widget in info.winfo_children():  # initialize the display area
        widget.destroy()
    info_heading = StringVar()
    if mode == 1:
        info_heading.set('Complete Version of Menu')
    else:
        info_heading.set('Menu')
    menus = get_menu(st.get(st.curselection()), TIME, mode)
    heading = Label(master=info, textvariable=info_heading, font='Georgia 18 bold ')
    heading.pack()
    display = Listbox(master=info)
    for x in menus:
        display.insert('end', x)
    display.pack()
    op = get_operating_hour(st.get(st.curselection()), TIME)  # function
    op_label = Label(master=info, text='Operating Hour: '+op, font='Georgia 16 bold ')
    op_label.pack()


def all_mode():
    tkinter.messagebox.showinfo('Notes', 'You are viewing all stalls and menus, regardless of time.\
                                         To quit this mode, by either click to select a time or going back to the current \
                                         time.')
    global mode
    mode = 1
    stall_update()


# basic settings for the main window
window = Tk()
window.title('Real Time Canteen Information System')
window.resizable(False, False)
# variable initialization
z = datetime.now()
TIME = [z.year, z.month, z.day, z.hour, z.minute, z.weekday()]
mode = 0

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
time_back = Button(master=time, text='Back to Current Time', command=back_to_current)
time_back.grid(row=2, column=2)
# area 2.1, list of stalls
stalls = Frame(window)
stalls.grid(row=2, column=1)
s_title = StringVar()
stall_update()
# area 2.2, information display area
info = Frame(window)
info.grid(row=2, column=2)
title_info = Label(master=info, text='Click One Stall to View More Information', font='Georgia 13 italic')
title_info.pack()
# area 3.1, buttons on the left
b1 = Frame(window)
b1.grid(row=3, column=1)
view_t = Button(master=b1, text='View Information of Selected Stall', command=view)
view_t.pack()
view_a = Button(master=b1, text='View List of All Stalls', command=all_mode)
view_a.pack()
# area 3.2, buttons on the right
b2 = Frame(window)
b2.grid(row=3, column=2)
view_tm = Button(master=b2, text='View All Menus')
view_tm.pack()
q = Button(master=b2, text='Calculate Queue Time', command=queue_time)
q.pack()


window.mainloop()

if __name__ == '__main__':
    print(TIME)  # demo: [2019, 11, 7, 23, 44, 3]
