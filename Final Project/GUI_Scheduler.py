import tkinter as tk
from easygui import msgbox
from appt import appt
from calendar_list import calendar
root = tk.Tk()
root.title("Scheduler")
calendar1 = calendar()

""" Creating the labels and window GUI"""
canvas1 = tk.Canvas(root, width=650, height=500)
labelTitle = tk.Label(root, text="Enter info to book an appointment")
labelMonth = tk.Label(root, text="Month")
labelDate = tk.Label(root, text="Date")
labelTime = tk.Label(root, text="Time")
labelDuration = tk.Label(root, text="Duration (in half hour increments)")
labelAMorPM = tk.Label(root, text="Time")
labelSubject = tk.Label(root, text="Subject")

"""Creating Months list options array"""
months_list = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
months = tk.StringVar(root)
months.set(months_list[0])

"""Creating Dates list options array"""
dates_list = ["","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22", "23","24","25","26","27","28","29","30","31"]
dates = tk.StringVar(root)
dates.set(dates_list[0])

"""Creating Times list options array"""
times_list = ["","8","9","10","11","12","1","2","3","4","5"]
times = tk.StringVar(root)
times.set(dates_list[0])

"""Creating Durations list options array"""
durations_list = ["",".5","1","1.5","2","2.5","3","3.5","4"]
durations = tk.StringVar(root)
durations.set(durations_list[0])

"""Creating the list boxes"""
Month = tk.OptionMenu(root, months, *months_list )
Date = tk.OptionMenu(root, dates, *dates_list )
Time = tk.OptionMenu(root, times, *times_list )
Duration = tk.OptionMenu(root, durations, *durations_list)
Subject = tk.Text(root)

dash = "-"
"""Setting labels/options on GUI frame and lines"""
canvas1.create_window(100, 50, window=labelTitle)
canvas1.create_window(100, 100, window=labelMonth)
canvas1.create_window(500, 100, window=Month)
canvas1.create_window(100, 150, window=labelDate)
canvas1.create_window(500, 150, window=Date)
canvas1.create_window(100, 200, window=labelTime)
canvas1.create_window(500, 200, window=Time)
canvas1.create_window(100, 250, window=labelDuration)
canvas1.create_window(500, 250, window=Duration)
canvas1.create_window(500,300,window=labelSubject)
canvas1.create_window(500,350,window=Subject, width=200, height=75)
canvas1.create_line(650,75,75,75,0,75)
canvas1.create_line(650,125,125,125,0,125)
canvas1.create_line(650,175,175,175,0,175)
canvas1.create_line(650,225,125,225,0,225)
canvas1.create_line(650,275,175,275,0,275)
canvas1.create_line(600,225,600,175)
canvas1.create_line(550,225,550,175)


"""Function when enter button is selected to enter an appointment, creates an class instance of an appointment"""
def enter_appt():
    AM = var5.get()
    PM = var6.get()
    AM_PM_String = None
    if months.get() == "" or dates.get() == "" or times.get() == "" or durations.get() == "":
        msgbox("Missing field!")
        return
    if AM>PM:
        AM_PM_String="AM"
    if AM<PM:
        AM_PM_String = "PM"
    if AM==PM:
        msgbox("Select either AM or PM")
        return
    appt1 = appt(months.get(), dates.get(), times.get(), durations.get(), AM_PM_String, Subject.get("1.0", tk.END))
    calendar1.add_appt(appt1)

def remove_appt():
    AM = var5.get()
    PM = var6.get()
    AM_PM_String = None
    if months.get() == "" or dates.get() == "" or times.get() == "" or durations.get() == "":
        msgbox("Missing field!")
        return
    if AM>PM:
        AM_PM_String="AM"
    if AM<PM:
        AM_PM_String = "PM"
    if AM==PM:
        msgbox("Select either AM or PM")
        return
    appt1 = appt(months.get(), dates.get(), times.get(), durations.get(), AM_PM_String)
    calendar1.remove_appt(appt1)
def displayAppts():
    appts_list = calendar1.display_appt()
    appts_window = tk.Toplevel()
    for x in appts_list:
        label_appt = tk.Label(appts_window, text=x)
        label_appt.pack()

    appts_window.mainloop()
""" Creating and setting Enter button, AM and PM checkboxes"""
button1 = tk.Button(text='Enter appointment', command=enter_appt)
canvas1.create_window(100, 300, window=button1)
button2 = tk.Button(text='Remove appointment', command=remove_appt)
canvas1.create_window(100, 350, window=button2)
button3 = tk.Button(text='Display Schedule', command=displayAppts)
canvas1.create_window(100, 400, window=button3)
var5 = tk.IntVar()
AM_check = tk.Checkbutton(root, text="AM", variable=var5)
canvas1.create_window(575, 200, window=AM_check)
var6 = tk.IntVar()
PM_check = tk.Checkbutton(root, text="PM", variable=var6)
canvas1.create_window(625, 200, window=PM_check)

"""Packing canvas and creating main loop"""
canvas1.pack()
root.mainloop()

