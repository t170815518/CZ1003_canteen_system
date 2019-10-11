import tkinter

if __name__ == "__main__":
    time_chosen = (11, 10, 2019, 15, 30)  # 15:00
    # stalls_list = dataBase.keys()
    stalls_list = ['Cantonese Roast Duck']
    food_list = ['Roast Duck Rice']

window = tkinter.Tk()
window.title('Real-time Canteen Information System')
window.geometry('900x600')

# TIME display area
time_displayed = tkinter.Text(master=window, height=4, width=100)
time_displayed.insert(index=1.1, chars="Display Time\n")
time_displayed.insert(index=2.1, chars="{}-{}-{}  {}:{}".format(time_chosen[2], time_chosen[1], time_chosen[0],
                                                                time_chosen[3], time_chosen[4]))
time_displayed.pack()

# STALL: display and choose area
stall = tkinter.Listbox(master=window, selectmode='SINGLE')
index_ = 0
for i in stalls_list:
    stall.insert(index_,i)
stall_chosen = stall.curselection()  # t tuple of the line numbers, from 0
stall.pack()

# INFORMATION display area
info_displayed = tkinter.Text(master=window)
info_displayed.insert(1.1,'Information of {}\n'.format(stall_chosen))
info_displayed.insert(2.1,'\tMenu\n')


window.mainloop()
