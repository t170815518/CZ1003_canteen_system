from tkinter import *
from time_modification import time_changed, input_time
from datetime import datetime, timedelta
from time import sleep

window = Tk()
window.title('Real-time Canteen Information System')


# time display area
time = Label(master=window, state='disabled', text=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# pack
time.pack()

# dynamic update of information
while True:
    sleep(1)
    time['text'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    window.update()
window.mainloop()