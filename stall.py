#Function by Yu Ting
import tkinter.messagebox
from checkdate import month_day_check


def file_management():  # file operation
    def convert_string_to_tuple():
        # string operations: convert operating hour from string to integer tuple
        for i in range(1, len(items)):
            if items[i][:2] == 'PH':
                public_dict[name] = tuple([int(x) for x in items[i][3:].split(',')])
            elif items[i][:2] == 'EP':
                exm_p_dict[name] = tuple([int(x) for x in items[i][3:].split(',')])
            else:
                if items[i] != 'Closed':
                    stall_dict[name].append(tuple([int(x) for x in items[i].split(',')]))
                else:
                    stall_dict[name].append(-1)

    with open('database.txt', 'r') as f:
        everything = f.read()

    blocks = everything.split('//')
    for block in blocks:
        items = block.splitlines()
        if items[0] == '':
            del items[0]
        name = items[0].strip()
        stall_dict[name] = []
        convert_string_to_tuple()


def get_stall(time, mode):  # time is tuple (year, month, day, hour, minute, weekday)
    global tmp

    def logic_check():
        if year <= 1991 or not (isinstance(year, int)):
            tkinter.messagebox.showinfo('Error!', 'Please input the valid year.')
            return False
        if not (isinstance(day, int) and month_day_check(year, month, day)):
            tkinter.messagebox.showinfo('Error!', 'Please input the valid month and day.')
            return False
        return True

    def public_holiday_check():
        public_holiday = [(1, 1), (1, 25), (1, 26), (4, 10), (5, 1), (5, 7), (5, 23), (5, 24), (7, 30), (7, 31),
                          (8, 10), (11, 14), (12, 25)]  # public holiday in sg in 2020
        if (month, day) in public_holiday:
            return True
        else:
            return False

    def examination_period_check():
        if (month == 11 and 18 <= day <= 30) or (month == 12 and 1 <= day <= 6) or (month == 4 and 20 <= day <= 30) or \
                (month == 5 and 1 <= day <= 8):  # NTU examination period, AY2019-2020
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

    # define variables
    if mode == 1:
        return [x for x in stall_dict.keys()]

    tmp = stall_dict

    year = time[0]
    month = time[1]
    day = time[2]
    hour = time[3]
    minute = time[4]
    weekday = time[5]

    stall_open = []

    # check special period
    if not (logic_check()) or not(month_day_check(year, month, day)):
        return False
    if public_holiday_check():
        tmp = public_dict
    elif examination_period_check():
        tmp.update(exm_p_dict)

    # check open stalls based on hour and minute
    for stall in tmp.keys():
        if isinstance(tmp[stall], list):
            if tmp[stall][weekday] != -1 and hour_check(tmp[stall][weekday]):
                stall_open.append(stall)
        else:
            if hour_check(tmp[stall]):
                stall_open.append(stall)

    return stall_open


def get_operating_hour(stall_name, time):
    for stall in tmp.keys():
        if isinstance(tmp[stall], list):
            x = tmp[stall_name][time[5]]
            return '{:02d}:{:02d}-{:02d}:{:02d}'.format(x[0], x[1], x[2], x[3])
        else:
            x = tmp[stall_name]
            return '{:02d}:{:02d}-{:02d}:{:02d}'.format(x[0], x[1], x[2], x[3])


# initialization, use of dictionary
stall_dict = {}
public_dict = {}
exm_p_dict = {}
file_management()

if __name__ == '__main__':
    file_management()
    print(stall_dict)
    print(exm_p_dict)
    print(public_dict)
    print(get_stall((2019, 11, 5, 12, 00, 4), 1))
