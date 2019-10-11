# data base
dataBase = {'Cantonese Roast Duck': {'Menu':['Cantonese Duck Rice']
                                     'Operating hour':('9:30','21:00')}
            }

# function
def filter_stalls(time_chosen):  # time is integer tuple, (dd,month,yy,h,m)
    pass
    if time_chosen == (0,0,0,0,0):  # 0,0,0,0,0 is the special time when all information of all stalls is displayed
        filtered_dataBase = dataBase
    return filtered_dataBase  # return value type: dictionary

def calculate_queue_time(number_queue_people):  # parameter should only be integer!
    pass
    return queue_time # return value is integer in minutes

def change_time():
    pass
    return changed_time  # time_chosen = changed_time