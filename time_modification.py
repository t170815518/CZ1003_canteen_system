import datetime


current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
time_changed = False
input_time = '2019-10-23 15:30'

if __name__=='__main__':
    while True:
        print(current_time)