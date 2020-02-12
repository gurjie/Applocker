import os
import sys
import datetime
import tkinter
from tkinter import *
from tkinter import scrolledtext
from tkcalendar import Calendar, DateEntry

def check_reachable():
    # The app will be usable from start_usable_hour until end_usable_hour
    start_usable_hour = 20
    end_usable_hour = 2
    if(os.access("C:\ProgramData\Ableton\Live 10 Suite\Program\Ableton Live 10 Suite.exe",os.F_OK)):
        print("Ableton is reachable")
        current=datetime.datetime.now()
        if (current.hour >= 20 or current.hour < 2): 
            print("You're allowed to use the app now, congratulations :)")
        else: 
            print("Access will be denied to the app now")
    else:
        #sys.exit("Ableton wasn't reachable")
        print("hello")

def main(): 
    master_window = Tk() #DECLARED
    master_window.resizable(False, True)
    # Parent widget for the buttons
    buttons_frame = Frame(master_window) #DECLARED
    buttons_frame.grid(row=0, column=0)    
    title = tkinter.Label(master_window, text = "App/File Locker",width=26, font=("Courier",23))
    title.grid(row = 0, column=0) 
  
    #btn_Image = Button(buttons_frame, text='Image')
    #btn_Image.grid(row=0, column=0, padx=(10), pady=10)


    # Group1 Frame ----------------------------------------------------
    content_group = LabelFrame(master_window, text="Parameters", font=("TkDefaultFont",18),padx=5, pady=9)
    content_group.grid(row=1, column=0, columnspan=5, padx=10, pady=14, sticky=E+W+N+S)

    master_window.columnconfigure(0, weight=1)
    master_window.rowconfigure(1, weight=1)

    content_group.rowconfigure(3, weight=1)
    content_group.rowconfigure(1, weight=1)
    content_group.rowconfigure(2, weight=1)


    # add path_label
    path_label = tkinter.Label(content_group, text="Path to block:", font=("TkDefaultFont",13), width=0, height=2)
    path_label.grid(row=1, column=0, sticky=W+N)

    mainloop()


if __name__ == "__main__": 
    main()

