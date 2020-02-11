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
    master_window = Tk()
    master_window.resizable(False, True)
    # Parent widget for the buttons
    buttons_frame = Frame(master_window)
    buttons_frame.grid(row=0, column=0)    
    tkinter.Label(master_window, text = "App/File Locker",width=26, font=("Courier",23)).grid(row = 0, column=0) 
  
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
    # add path input box
    path_entry = tkinter.Entry(content_group,width=49)
    path_entry.grid(row=1, column=1, sticky=W+N, pady=12)
    # add blockfrom label
    from_label = tkinter.Label(content_group, text="Block From:", font=("TkDefaultFont",13), width=0, height=2)
    from_label.grid(row=2, column=0, sticky=W+N)
    # add blockfrom hh label
    from_hh_label = tkinter.Label(content_group, text="hh", font=("TkDefaultFont",11), width=0, height=2)
    from_hh_label.grid(row=2, column=1, sticky=W+N, pady=1)
    # add blockfrom hour input box
    block_from_entry_hour = tkinter.Spinbox(content_group,width=3, from_=0, to=23)
    block_from_entry_hour.grid(row=2, column=1, sticky=W+N, pady=12, padx=28)
    # add blockfrom mm label
    from_mm_label = tkinter.Label(content_group, text="mm", font=("TkDefaultFont",11), width=0, height=2)
    from_mm_label.grid(row=2, column=1, sticky=W+N, pady=1, padx = 70)
    # add blockfrom minute input box
    block_from_entry_minute = tkinter.Spinbox(content_group,width=3, from_=0, to=59)
    block_from_entry_minute.grid(row=2, column=1, sticky=W+N, pady=12, padx = 109)
    # add blockuntil hh label
    until_hh_label = tkinter.Label(content_group, text="hh", font=("TkDefaultFont",11), width=0, height=2)
    until_hh_label.grid(row=3, column=1, sticky=W+N, pady=1)
    # add blockuntil label
    block_until_label = tkinter.Label(content_group, text="Block Until:", font=("TkDefaultFont",13), width=0, height=2)
    block_until_label.grid(row=3, column=0, sticky=W+N)
    # add blockuntil hour input box
    block_until_entry_hour = tkinter.Spinbox(content_group,width=3, from_=0, to=23)
    block_until_entry_hour.grid(row=3, column=1, sticky=W+N, pady=12, padx=28)
    # add blockuntil mm label
    until_mm_label = tkinter.Label(content_group, text="mm", font=("TkDefaultFont",11), width=0, height=2)
    until_mm_label.grid(row=3, column=1, sticky=W+N, pady=1, padx = 70)
    # add blockuntil minute input box
    block_until_entry_minute = tkinter.Spinbox(content_group,width=3, from_=0, to=59)
    block_until_entry_minute.grid(row=3, column=1, sticky=W+N, pady=12, padx = 109)
    # add browse for file button
    btn1 = tkinter.Button(content_group, text = "Browse...", width=0, height=1)
    btn1.grid(row=1, column=3 ,sticky=W+N, pady=9, padx=7)

    #########################################begin dates init########################################################

    mon = IntVar()
    tues = IntVar()
    weds = IntVar()
    thurs = IntVar()
    fri = IntVar()
    sat = IntVar()
    sun = IntVar()
    # sub content group to hold the dates for the dates
    sub_content_group = LabelFrame(content_group, text="Dates", font=("TkDefaultFont",15),padx=5, pady=9)
    sub_content_group.grid(row=4, column=0, columnspan=10, padx=10, pady=14, sticky=E+W+N+S)
    #add *daily?* label
    daily_label = tkinter.Label(sub_content_group, text="Daily?:", font=("TkDefaultFont",13), width=0, height=0)
    daily_label.grid(row=1, column=0, sticky=W+N)
    # add daily checkbox 
    DailyCheckbox = IntVar()
    tkinter.Checkbutton(sub_content_group,variable = DailyCheckbox,onvalue = 1, offvalue=0).grid(row=1,column=1,sticky=W)
    #add Select days label
    daily_label = tkinter.Label(sub_content_group, text="Select Days:", font=("TkDefaultFont",13), width=0, height=0)
    daily_label.grid(row=1, column=3, sticky=W+N)
    # add monday checkbox 
    tkinter.Checkbutton(sub_content_group,variable = mon,onvalue = 1, offvalue=0).grid(row=1,column=4,sticky=W)
    # add tues checkbox 
    tkinter.Checkbutton(sub_content_group,variable = tues,onvalue = 1, offvalue=0).grid(row=1,column=5,sticky=W)
    # add weds checkbox 
    tkinter.Checkbutton(sub_content_group,variable = weds,onvalue = 1, offvalue=0).grid(row=1,column=6,sticky=W)
    # add thurs checkbox 
    tkinter.Checkbutton(sub_content_group,variable = thurs,onvalue = 1, offvalue=0).grid(row=1,column=7,sticky=W)
    # add fri checkbox 
    tkinter.Checkbutton(sub_content_group,variable = fri,onvalue = 1, offvalue=0).grid(row=1,column=8,sticky=W)
    # add sat checkbox 
    tkinter.Checkbutton(sub_content_group,variable = sat,onvalue = 1, offvalue=0).grid(row=1,column=9,sticky=W)
    # add sun checkbox 
    tkinter.Checkbutton(sub_content_group,variable = sun,onvalue = 1, offvalue=0).grid(row=1,column=10,sticky=W)
    mon_label = tkinter.Label(sub_content_group, text="mon", font=("TkDefaultFont",7), width=3, height=0)
    mon_label.grid(row=0, column=4, sticky=W+N)
    tues_label = tkinter.Label(sub_content_group, text="tue", font=("TkDefaultFont",7), width=3, height=0)
    tues_label.grid(row=0, column=5, sticky=W+N)
    weds_label = tkinter.Label(sub_content_group, text="wed", font=("TkDefaultFont",7), width=3, height=0)
    weds_label.grid(row=0, column=6, sticky=W+N)
    thurs_label = tkinter.Label(sub_content_group, text="thu", font=("TkDefaultFont",7), width=3, height=0)
    thurs_label.grid(row=0, column=7, sticky=W+N)
    fri_label = tkinter.Label(sub_content_group, text="fri", font=("TkDefaultFont",7), width=3, height=0)
    fri_label.grid(row=0, column=8, sticky=W+N)
    sat_label = tkinter.Label(sub_content_group, text="sat", font=("TkDefaultFont",7), width=3, height=0)
    sat_label.grid(row=0, column=9, sticky=W+N)
    sun_label = tkinter.Label(sub_content_group, text="sun", font=("TkDefaultFont",7), width=3, height=0)
    sun_label.grid(row=0, column=10, sticky=W+N)
    #######################################end dates init###################################################
    mainloop()


if __name__ == "__main__": 
    main()

