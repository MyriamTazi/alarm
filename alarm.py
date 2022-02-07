from tkinter import *
import datetime 
import time
import winsound

def alarm(timer):
    while True:
        time.sleep(1)
        time_now = datetime.datetime.now()
        now = time_now.strftime("%H:%M:%S")
        date = time_now.strftime("%d/%m/%Y")
        print("Today is:", date)
        print(now)
        if now == timer:
            print("Wake up time!")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(timer)

clock = Tk()
clock.title("Myriam's Alarm Clock")
clock.geometry("500x250")
time_format=Label(clock, text= "Enter time as 24hr", fg="blue",bg="beige",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "When to wake up",fg="black",relief = "solid",font=("monospace",8,"bold")).place(x=1, y=30)

#Alarm initialization:
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time for alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "lightblue",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "lightblue",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "lightblue",width = 15).place(x=200,y=30)

#Time input by user:
submit = Button(clock,text = "Set Alarm",fg="Black",width = 10,command = actual_time).place(x =110,y=70)

clock.mainloop()