import tkinter
from function_tangyuting import change_time, see_all, queue_time

def display():
    global info_str, food_list
    info_str.setvar(value='')
    info_str.insert('end', 'Information of {}'.format(stall.curselection()))
    info_str.insert('end', '\tMenu',)
    for i in food_list:
        info_str.insert('end', i)
    info_str.insert('end', '\tOperating Hour:{}:{}'.format(operating_hour[0], operating_hour[1]))

if __name__== '__main__':
    time_chosen = (11, 10, 2019, 15, 30)  # 15:00
    # stalls_list = dataBase.keys()


window = tkinter.Tk()
window.title('Real-time Canteen Information System')
window.geometry('900x600')

#initialization
info_str = tkinter.Text(window)

# change time
change_time_button = tkinter.Button(window, text='Change Time', command=change_time())

# see all information
see_all_button = tkinter.Button(window, text='See All Information', command=see_all())

# calculate queue time
queue = tkinter.Button(window, text='Calculate Queue Time', command=queue_time())

# exit
esc_button = tkinter.Button(window, text='Exit')


# TIME display area
time_displayed = tkinter.Text(master=window, height=4, width=100)
time_displayed.insert(index=1.1, chars="Display Time\n")
time_displayed.insert(index=2.1, chars="{}-{}-{}  {}:{}".format(time_chosen[2], time_chosen[1], time_chosen[0],
                                                                time_chosen[3], time_chosen[4]))


# STALL: display and choose area
stall = tkinter.Listbox(master=window)
for i in stalls_list:
    stall.insert('end', i)
# display information
display = tkinter.Button(master=window, text='View the selected stall\'s information', command=display())

# information display area
info = tkinter.Message(window, textvariable=info_str, width=80)

esc_button.pack()
time_displayed.pack()
see_all_button.pack()
queue.pack()
stall.pack()
display.pack()
info.pack()
window.mainloop()
change_time_button.pack()
