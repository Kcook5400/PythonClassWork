
import tkinter as tk
from save_info import save_info
root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=400)
labelTitle = tk.Label(root, text="Enter Date in YYYY-MM-DD format")
canvas1.create_window(100, 50, window=labelTitle)
canvas1.grid(row=1)
labelTime = tk.Label(root, text="Time")
canvas1.create_window(100, 150, window=labelTime)


entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
canvas1.create_window(100, 100, window=entry1)
canvas1.create_window(100, 200, window=entry2)



def date_time():
    date1 = entry1.get()
    time2 = entry2.get()
    am = bool(var5.get())
    pm = bool(var6.get())
    save_info(date1, time2, am, pm)

button1 = tk.Button(text='Enter', command=date_time)
canvas1.create_window(100, 300, window=button1)
var5 = tk.IntVar()
time_check = tk.Checkbutton(root, text="AM", variable=var5)
canvas1.create_window(150, 200, window=time_check)
var6 = tk.IntVar()
time_check = tk.Checkbutton(root, text="PM", variable=var6)
canvas1.create_window(200, 200, window=time_check)



root.mainloop()