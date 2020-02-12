import tkinter
from tkinter import *

class View: 
    def __init__(self):
        self._master_window = Tk()
        self._buttons_frame = tkinter.Frame(master=self._master_window)
        self._title = tkinter.Label(master=self._master_window)
        self._content_group = LabelFrame(master=self._master_window) 
        self._path_label = tkinter.Label(master=self._content_group)
        self._path_entry = tkinter.Entry(master=self._content_group) 
        self._from_label = tkinter.Label(master=self._content_group)
        self._from_hh_label = tkinter.Label(master=self._content_group)
        self._block_from_entry_hour = tkinter.Spinbox(master=self._content_group)
        self._from_mm_label = tkinter.Label(master=self._content_group)
        self._block_from_entry_minute = tkinter.Spinbox(master=self._content_group)
        self._until_hh_label = tkinter.Label(master=self._content_group)
        self._block_until_label = tkinter.Label(master=self._content_group)
        self._block_until_entry_hour = tkinter.Spinbox(master=self._content_group)
        self._until_mm_label = tkinter.Label(master=self._content_group)
        self._block_until_entry_minute = tkinter.Spinbox(master=self._content_group)
        self._browse = tkinter.Button(master=self._content_group)
        self._mon = IntVar()
        self._tues = IntVar() 
        self._weds = IntVar() 
        self._thurs = IntVar()
        self._fri = IntVar() 
        self._sat = IntVar() 
        self._sun = IntVar() 
        self._daily = IntVar() 
        self._sub_content_group = tkinter.LabelFrame()
        self._daily_label = tkinter.Label(master=self._sub_content_group)
        self._select_days_label = tkinter.Label(master=self._sub_content_group)
        self._mon_label = tkinter.Label(master=self._sub_content_group)
        self._tues_label = tkinter.Label(master=self._sub_content_group)
        self._weds_label = tkinter.Label(master=self._sub_content_group)
        self._thurs_label = tkinter.Label(master=self._sub_content_group)
        self._fri_label = tkinter.Label(master=self._sub_content_group)
        self._sat_label = tkinter.Label(master=self._sub_content_group) 
        self._sun_label = tkinter.Label(master=self._sub_content_group)
        self._mon_checkbox = tkinter.Checkbutton(master=self._sub_content_group)
        self._tue_checkbox = tkinter.Checkbutton(master=self._sub_content_group)
        self._wed_checkbox = tkinter.Checkbutton(master=self._sub_content_group)
        self._thu_checkbox = tkinter.Checkbutton(master=self._sub_content_group)
        self._fri_checkbox = tkinter.Checkbutton(master=self._sub_content_group)
        self._sat_checkbox = tkinter.Checkbutton(master=self._sub_content_group)
        self._sun_checkbox = tkinter.Checkbutton(master=self._sub_content_group)
        self._daily_checkbox = tkinter.Checkbutton(master=self._sub_content_group)

    def getSunCheck(self):
        return self._sun_checkbox

    def getSatCheck(self):
        return self._sat_checkbox

    def getFriCheck(self):
        return self._fri_checkbox

    def getThuCheck(self):
        return self._thu_checkbox

    def getWedCheck(self):
        return self._wed_checkbox

    def getTueCheck(self):
        return self._tue_checkbox

    def getMonCheck(self):
        return self._mon_checkbox

    def getSunLabel(self):
        return self._sun_label

    def getSatLabel(self):
        return self._sat_label

    def getFriLabel(self):
        return self._fri_label

    def getThursLabel(self):
        return self._thurs_label

    def getWedsLabel(self):
        return self._weds_label

    def getTuesLabel(self):
        return self._tues_label

    def getMonLabel(self):
        return self._mon_label

    def getSelectDaysLabel(self):
        return self._select_days_label

    def getDailyCheckbox(self):
        return self._daily_checkbox

    def getDailyLabel(self):
        return self._daily_label

    def getSubContentGroup(self):
        return self._sub_content_group

    def getDaily(self):
        return self._daily

    def getSun(self):
        return self._sun

    def getSat(self):
        return self._sat

    def getFri(self):
        return self._fri

    def getThurs(self):
        return self._thurs

    def getWeds(self):
        return self._weds

    def getTues(self):
        return self._tues

    def getMon(self):
        return self._mon

    def getBrowse(self):
        return self._browse

    def getBlockUntilEntryMinute(self):
        return self._block_until_entry_minute

    def getUntil_mm_label(self):
        return self._until_mm_label

    def getBlockUntilEntryHour(self):
        return self._block_until_entry_hour

    def getBlockUntilLabel(self):
        return self._block_until_label

    def getUntil_hh_label(self):
        return self._until_hh_label

    def getBlockFromEntryMinute(self):
        return self._block_from_entry_minute

    def getFrom_mm_label(self):
        return self._from_mm_label
    
    def getBlockFromEntryHour(self):
        return self._block_from_entry_hour

    def getFrom_hh_label(self):
        return self._from_hh_label

    def getFromLabel(self):
        return self._from_label

    def getPathEntry(self):
        return self._path_entry

    def getPathLabel(self):
        return self._path_label

    def getContentGroup(self):
        return self._content_group 

    def getTitle(self):
        return self._title

    def getButtonsFrame(self):
        return self._buttons_frame

    def getMasterWindow(self):
        return self._master_window