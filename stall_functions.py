import tkinter.messagebox


def file_management():  # file operation
    with open('database.txt', 'r') as f:
        everything = f.read()

    blocks = everything.split('//')
    for block in blocks:
        # block = block.rstrip('\\n')  # \\n
        items = block.splitlines()
        if items[0] == '':
            del items[0]
        name = items[0]
        stall_dict[name] = []
        for i in range(1, len(items)):  # use of string operations
            if items[i][:2] == 'PH':
                public_dict[name] = tuple([int(x) for x in items[i][3:].split(',')])
            elif items[i][:2] == 'EP':
                exm_p_dict[name] = tuple([int(x) for x in items[i][3:].split(',')])
            else:
                if items[i] != 'Closed':
                    stall_dict[name].append(tuple([int(x) for x in items[i][3:].split(',')]))
                else:
                    stall_dict[name].append(-1)


# initialization
    # use of dictionary 
stall_dict = {}
public_dict = {}
exm_p_dict = {}


def get_stall(time):  # time is tuple (year, month, day, hour, minute, weekday)
    def logic_check():
        def month_day_check(month, day):
            return True # written by Tan
        if year <= 1991 or not(isinstance(year, int)):
            tkinter.messagebox.showinfo('Error!', 'Please input the valid year.')
            return False
        if not(isinstance(month, int) and 1 <= month <= 12):
            tkinter.messagebox.showinfo('Error!', 'Please input the valid month.')
            return False
        if not(isinstance(day, int) and month_day_check(month, day)):
            tkinter.messagebox.showinfo('Error!', 'Please input the valid day.')
            return False

    def public_holiday_check(month, day):
        public_holiday = [(1, 1), (1, 25), (1, 26), (4, 10), (5, 1), (5, 7), (5, 23), (5, 24), (7, 30), (7, 31),
                          (8, 10), (11, 14), (12, 25)]  # use of tuple
        if (month, day) in public_holiday:
            return True
        else:
            return False

    def examination_period_check(mondth, day):
        if (month == 11 and 18 <= day <= 30) or (month == 12 and 1 <= day <= 6) or (month == 4 and 20 <= day <= 30) or \
                (month == 5 and 1 <= day <= 8):
            return True
        else:
            return False

    def hour_check(time_open):  # (hh, mm, hh, mm)
        if time_open[0] < hour < time_open[2]:
            return True
        elif (hour == time_open[0]) and (minute >= time_open[1]):
            return True
        elif (hour == time_open[2]) and (minute <= time_open[3]):
            return True
        else:
            return False

    # define variable
    tmp = stall_dict
    stall_open = []
    year = time[0]
    month = time[1]
    day = time[2]
    hour = time[3]
    minute = time[4]
    weekday = time[5]
    
    logic_check()
    if public_holiday_check():
        tmp = public_dict
    elif examination_period_check():
        tmp.update(exm_p_dict)

    # hour check
    for stall in tmp.keys():
        if isinstance(tmp[stall], list):
            if hour_check(tmp[stall][weekday-1]):
                stall_open.append(stall)
        else:
            if hour_check(tmp[stall]):
                stall_open.append(stall)

    return stall_open


