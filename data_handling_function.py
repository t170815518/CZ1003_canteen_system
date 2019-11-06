import tkinter.messagebox


stall_dict = {}
ep_dict = {}
pb_dict = {}


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
    tmp = pb_dict

    def logic_check():  # Error Handling
        def month_day_check(month, day):  # Tan Wee Li
            pass

        if year <= 1991 or not(isinstance(year, int)):
            tkinter.messagebox.showinfo('Error!', 'Please input the valid year.')
        if not(isinstance(month, int) and 1<=month<=12):
            tkinter.messagebox.showinfo('Error!', 'Please input the valid month.')
        if not(isinstance(day, int) and month_day_check(month, day)):
            tkinter.messagebox.showinfo('Error!', 'Please input the valid month.')
    def public_holiday_check():
        if (month, day) in public_holiday:
            return True
    logic_check()
    if public_holiday_check():


if __name__ == '__main__':
    get_stalls ((0, 0, 0, 0, 0, 0, 0))