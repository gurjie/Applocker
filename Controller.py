import View as v
import sys
import tkinter
from tkinter import *
from tkinter import filedialog


class Controller: 

    def __init__(self):
        self.view = v.View() # init view and its components
        self.initView()

    def initView(self):
        self.view.getMasterWindow().resizable(False,True)
        self.view.getButtonsFrame().master = self.view.getMasterWindow()
        self.view.getButtonsFrame().grid(row=0, column=0)
        self.view.getTitle().configure(text = "App/File Locker",width=26, font=("Courier",23))
        self.view.getTitle().grid(row=0,column=0)
        self.view.getContentGroup().configure(text="Parameters", font=("TkDefaultFont",18),padx=5, pady=9)
        self.view.getContentGroup().grid(row=1, column=0, columnspan=5, padx=10, pady=14, sticky=E+W+N+S)
        # config columns and row for master to ensure resizing
        self.view.getMasterWindow().columnconfigure(0, weight=1)
        self.view.getMasterWindow().rowconfigure(1, weight=1)
        # row config contentgroup to make the content stretch
        self.view.getContentGroup().rowconfigure(3, weight=1)
        self.view.getContentGroup().rowconfigure(1, weight=1)
        self.view.getContentGroup().rowconfigure(2, weight=1)
        # config path label
        self.view.getPathLabel().configure(text="Path to block:", font=("TkDefaultFont",13), width=0, height=2)
        self.view.getPathLabel().grid(row=1, column=0, sticky=W+N)
        # config path input box
        self.view.getPathEntry().configure(width=49)
        self.view.getPathEntry().grid(row=1, column=1, sticky=W+N, pady=12)
        # config blockfrom label
        self.view.getFromLabel().configure(text="Block From:", font=("TkDefaultFont",13), width=0, height=2)
        self.view.getFromLabel().grid(row=2, column=0, sticky=W+N)
        # config blockfrom hh label
        self.view.getFrom_hh_label().configure(text="hh", font=("TkDefaultFont",11), width=0, height=2)
        self.view.getFrom_hh_label().grid(row=2, column=1, sticky=W+N, pady=1) 
        # config blockfrom hour spinbox
        self.view.getBlockFromEntryHour().configure(width=3, from_=0, to=23)
        self.view.getBlockFromEntryHour().grid(row=2, column=1, sticky=W+N, pady=12, padx=28)
        # config blockfrom mm label
        self.view.getFrom_mm_label().configure(text="mm", font=("TkDefaultFont",11), width=0, height=2)
        self.view.getFrom_mm_label().grid(row=2, column=1, sticky=W+N, pady=1, padx = 70)
        # config blockfrom minute spinbox
        self.view.getBlockFromEntryMinute().configure(width=3, from_=0, to=59)
        self.view.getBlockFromEntryMinute().grid(row=2, column=1, sticky=W+N, pady=12, padx = 109)
        # config blockuntil hh label
        self.view.getUntil_hh_label().configure(text="hh", font=("TkDefaultFont",11), width=0, height=2)
        self.view.getUntil_hh_label().grid(row=3, column=1, sticky=W+N, pady=1)
        # config blockuntil label
        self.view.getBlockUntilLabel().configure(text="Block Until:", font=("TkDefaultFont",13), width=0, height=2)
        self.view.getBlockUntilLabel().grid(row=3, column=0, sticky=W+N)
        # config block until spinbox
        self.view.getBlockUntilEntryHour().configure(width=3, from_=0, to=23)
        self.view.getBlockUntilEntryHour().grid(row=3, column=1, sticky=W+N, pady=12, padx=28)
        # config block until mm label
        self.view.getUntil_mm_label().configure(text="mm", font=("TkDefaultFont",11), width=0, height=2)
        self.view.getUntil_mm_label().grid(row=3, column=1, sticky=W+N, pady=1, padx = 70)
        # config blockuntil spinbox input box 
        self.view.getBlockUntilEntryMinute().configure(width=3, from_=0, to=59)
        self.view.getBlockUntilEntryMinute().grid(row=3, column=1, sticky=W+N, pady=12, padx = 109)
        # config browse... button
        self.view.getBrowse().configure(text = "Browse...", width=0, height=1)
        self.view.getBrowse().grid(row=1, column=3 ,sticky=W+N, pady=9, padx=7)
        # config sub content group to hold the date selection
        self.view.getSubContentGroup().configure(text="Dates", font=("TkDefaultFont",15),padx=5, pady=9)
        self.view.getSubContentGroup().grid(row=4, column=0, columnspan=10, padx=10, pady=14, sticky=E+W+N+S)
        # config 'daily' label
        self.view.getDailyLabel().configure(text="Daily?:", font=("TkDefaultFont",13), width=0, height=0)
        self.view.getDailyLabel().grid(row=1, column=0, sticky=W+N)
        # config daily checkbox
        self.view.getDailyCheckbox().configure(variable = self.view.getDaily(),onvalue = 1, offvalue=0)
        self.view.getDailyCheckbox().grid(row=1,column=1,sticky=W)
        # config select days label
        self.view.getSelectDaysLabel().configure(text="Select Days:", font=("TkDefaultFont",13), width=0, height=0)
        self.view.getSelectDaysLabel().grid(row=1, column=3, sticky=W+N)
        # config mondays checkbox
        self.view.getMonCheck().configure(variable = self.view.getMon(),onvalue = 1, offvalue=0)
        self.view.getMonCheck().grid(row=1,column=4,sticky=W)
        # config tues checkbox
        self.view.getTueCheck().configure(variable = self.view.getTues(),onvalue = 1, offvalue=0)
        self.view.getTueCheck().grid(row=1,column=5,sticky=W)
        # config weds checkbox
        self.view.getWedCheck().configure(variable = self.view.getWeds(),onvalue = 1, offvalue=0)
        self.view.getWedCheck().grid(row=1,column=6,sticky=W)
        # config thu checkbox
        self.view.getThuCheck().configure(variable = self.view.getThurs(),onvalue = 1, offvalue=0)
        self.view.getThuCheck().grid(row=1,column=7,sticky=W)
        # config fri checkbox
        self.view.getFriCheck().configure(variable = self.view.getFri(),onvalue = 1, offvalue=0)
        self.view.getFriCheck().grid(row=1,column=8,sticky=W)
        # config sat checkbox
        self.view.getSatCheck().configure(variable = self.view.getSat(),onvalue = 1, offvalue=0)
        self.view.getSatCheck().grid(row=1,column=9,sticky=W)
        # config sun checkbox
        self.view.getSunCheck().configure(variable = self.view.getSun(),onvalue = 1, offvalue=0)
        self.view.getSunCheck().grid(row=1,column=10,sticky=W) 
        # config mon label
        self.view.getMonLabel().configure(text="mon", font=("TkDefaultFont",7), width=3, height=0)
        self.view.getMonLabel().grid(row=0, column=4, sticky=W+N)
        # config tue label
        self.view.getTuesLabel().configure(text="tue", font=("TkDefaultFont",7), width=3, height=0)
        self.view.getTuesLabel().grid(row=0, column=5, sticky=W+N)
        # config weds label
        self.view.getWedsLabel().configure(text="wed", font=("TkDefaultFont",7), width=3, height=0)
        self.view.getWedsLabel().grid(row=0, column=6, sticky=W+N)
        # config thurs label
        self.view.getThursLabel().configure(text="thu", font=("TkDefaultFont",7), width=3, height=0)
        self.view.getThursLabel().grid(row=0, column=7, sticky=W+N)
        # config fri label
        self.view.getFriLabel().configure(text="fri", font=("TkDefaultFont",7), width=3, height=0)
        self.view.getFriLabel().grid(row=0, column=8, sticky=W+N)
        # config sat label
        self.view.getSatLabel().configure(text="sat", font=("TkDefaultFont",7), width=3, height=0)
        self.view.getSatLabel().grid(row=0, column=9, sticky=W+N)
        # config sun label
        self.view.getSunLabel().configure(text="sun", font=("TkDefaultFont",7), width=3, height=0)
        self.view.getSunLabel().grid(row=0, column=10, sticky=W+N)
        # config browse button onclick
        self.view.getBrowse().configure(command = self.fileDialogue)

    def fileDialogue(self): 
        file = filedialog.askopenfilename()
        if file != None:
            print(file)
            self.view.getPathEntry().delete(0,END)
            self.view.getPathEntry().insert(INSERT,file)


