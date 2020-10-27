import tkinter
import easygui



def on_button_check():
    easygui.msgbox("Great Choice", title="Favorite Meal")
    m.destroy()

m = tkinter.Tk() # where m is the name of the main window object
m.title('Favorite Meal')
label = tkinter.Label(m, text="Choose your favorite meal!")
label.grid(row=0)
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Breakfast", variable=var1, command=on_button_check).grid(row=1)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Second Breakfast", variable=var2, command=on_button_check).grid(row=2)
var3 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Lunch", variable=var3, command=on_button_check).grid(row=3)
var4 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Dinner", variable=var4, command=on_button_check).grid(row=4)
var5 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Waiting", variable=var5, command=on_button_check).grid(row=5)
exit_button = tkinter.Button(m, text='Exit', width=80, command=m.destroy)
exit_button.grid(row=6)
m.mainloop()  # infinite loop that waits for events to happen