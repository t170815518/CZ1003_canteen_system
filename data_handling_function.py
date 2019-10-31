import tkinter.messagebox


stall_dict = {}
ep_dict = {}
pb_dict = {}
# public holiday 2020 at Singapore
public_holiday = [(1, 1), (1, 25), (1, 26), (4, 10), (5, 1), (5, 7), (5, 23), (5, 24), (7, 30), (7, 31),
                  (8, 10), (11, 14), (12, 25)]
exameination_period = [(x,y) for x in range(11,13) for y in range(1,32)]

with open('database.txt', 'r') as f:
    everything = f.read()

# string management
blocks = everything.split('//')
for block in blocks:
    # block = block.rstrip('\\n')  # \\n
    items = block.splitlines()
    if items[0] == '':
        del items[0]
    name = items[0]
    stall_dict[name] = []
    for i in range(1, len(items)):
        if items[i][:2] == 'PH':
            pb_dict[name] = items[i][3:]
        elif items[i][:2] == 'EP':
            ep_dict[name] = items[i][3:]
        else:
            if items[i] != 'Closed':
                stall_dict[name].append(items[i])
            else:
                stall_dict[name].append(-1)


def get_stalls(time):  # time tuple(year, month, day, hour, minute, weekday):
    year = time[0]
    month = time[1]
    day = time[2]
    hour = time[3]
    minute = time[4]
    weekday = time[5]

    def logic_check():  # Error Handling
        if year <= 1991 or not(isinstance(year, int)):
            tkinter.messagebox.showinfo('Error!', 'Please input the valid year.')
        if not(isinstance(month, int) and 1<=month<=12):
            tkinter.messagebox.showinfo('Error!', 'Please input the valid month.')
        if isinstance(day, int):
        else:
            tkinter.messagebox.showinfo('Error!', 'Please input the valid month.')
    logic_check()
            

if __name__ == '__main__':
    get_stalls ((0, 0, 0, 0, 0, 0, 0))