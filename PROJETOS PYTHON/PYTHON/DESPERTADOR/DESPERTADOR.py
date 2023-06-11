from tkinter import *
import datetime
import time
import winsound

from threading import *
root = Tk()
root.geometry("400x200")
def Threading():
    t1=Thread(target=alarm)
    t1.start
    
def alarm():
    
    while true:
        set_alarm_time = f" {hour.get()}: {minute.get()}: {second.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().