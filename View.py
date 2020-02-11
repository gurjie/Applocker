import os
import sys
import datetime
import tkinter
from tkinter import *

class View: 
    def __init__(self, r = 0, i=0):
        self.master_window = Tk()
        self.buttons_frame = Frame()
        self.title = tkinter.Label()
        self.content_group = LabelFrame() 
        self.path_label = tkinter.Label()
        self.path_entry = tkinet.Entry() 
        self.from_label = tkinter.Label()
        self.from_hh_label = tkinter.Label()
        self.block_from_entry_hour = tkinter.Spinbox()
        self.from_mm_label = tkinter.Label()
        self.block_from_entry_minute = tkinter.Spinbox()
        self.until_hh_label = tkinter.Label()
        self.block_until_label = tkinter.Label()
        self.block_until_entry_hour = tkinter.Spinbox()
        self.until_mm_label = tkinter.Label()
        self.block_until_entry_minute = tkinter.Spinbox()
        self.browse = tkinter.Button()
        self.mon = IntVar()
        self.tues = IntVar() 
        self.weds = IntVar() 
        self.thurs = IntVar()
        self.fri = IntVar() 
        self.sat = IntVar() 
        self.sun = IntVar() 
        self.daily = IntVar() 
        self.sub_content_group = tkinter.LabelFrame()
        self.daily_label = tkinter.Label()
        self.daily_checkbox = tkinter.Label()
        self.select_days_label = tkiner.Label() 
        self.mon_label = tkinter.Label()
        self.tues_label = tkinter.Label()
        self.weds_label = tkinter.Label()
        self.thurs_label = tkinter.Label()
        self.fri_label = tkinter.Label()
        self.sat_label = tkinter.Label() 
        self.sat_label = tkinter.Label() 

	def getMaster_window() :
		return this.();
	}

	def setTk()(= Tk()) :
		this.Tk() = Tk();
	}

	def getFrame()() :
		return this.Frame();
	}

	def setFrame()(= Frame()) :
		this.Frame() = Frame();
	}

	def getTkinter.Label()() :
		return this.tkinter.Label();
	}

	def setTkinter.Label()(= tkinter.Label()) :
		this.tkinter.Label() = tkinter.Label();
	}

	def getLabelFrame()() :
		return this.LabelFrame();
	}

	def setLabelFrame()(= LabelFrame()) :
		this.LabelFrame() = LabelFrame();
	}

	def getTkinter.Label()() :
		return this.tkinter.Label();
	}

	def setTkinter.Label()(= tkinter.Label()) :
		this.tkinter.Label() = tkinter.Label();
	}

	def getTkinet.Entry()() :
		return this.tkinet.Entry();
	}

	def setTkinet.Entry()(= tkinet.Entry()) :
		this.tkinet.Entry() = tkinet.Entry();
	}

	def getTkinter.Label()() :
		return this.tkinter.Label();
	}

	def setTkinter.Label()(= tkinter.Label()) :
		this.tkinter.Label() = tkinter.Label();
	}

	def getTkinter.Label()() :
		return this.tkinter.Label();
	}

	def setTkinter.Label()(= tkinter.Label()) :
		this.tkinter.Label() = tkinter.Label();
	}

	def getTkinter.Spinbox()() :
		return this.tkinter.Spinbox();
	}

	def setTkinter.Spinbox()(= tkinter.Spinbox()) :
		this.tkinter.Spinbox() = tkinter.Spinbox();
	}

	def getTkinter.Label()() :
		return this.tkinter.Label();
	}

	def setTkinter.Label()(= tkinter.Label()) :
		this.tkinter.Label() = tkinter.Label();
	}

	def getTkinter.Spinbox()() :
		return this.tkinter.Spinbox();
	}

	def setTkinter.Spinbox()(= tkinter.Spinbox()) :
		this.tkinter.Spinbox() = tkinter.Spinbox();
	}

	def getTkinter.Label()() :
		return this.tkinter.Label();
	}

	def setTkinter.Label()(= tkinter.Label()) :
		this.tkinter.Label() = tkinter.Label();
	}

	def getTkinter.Label()() :
		return this.tkinter.Label();
	}

	def setTkinter.Label()(= tkinter.Label()) :
		this.tkinter.Label() = tkinter.Label();
	}

	def getTkinter.Spinbox()() :
		return this.tkinter.Spinbox();
	}

	def setTkinter.Spinbox()(= tkinter.Spinbox()) :
		this.tkinter.Spinbox() = tkinter.Spinbox();
	}

	def getTkinter.Label()() :
		return this.tkinter.Label();
	}

	def setTkinter.Label()(= tkinter.Label()) :
		this.tkinter.Label() = tkinter.Label();
	}

	def getTkinter.Spinbox()() :
		return this.tkinter.Spinbox();
	}

	def setTkinter.Spinbox()(= tkinter.Spinbox()) :
		this.tkinter.Spinbox() = tkinter.Spinbox();
	}

	def getTkinter.Button()() :
		return this.tkinter.Button();
	}

	def setTkinter.Button()(= tkinter.Button()) :
		this.tkinter.Button() = tkinter.Button();
	}

	def getIntVar()() :
		return this.IntVar();
	}

	def setIntVar()(= IntVar()) :
		this.IntVar() = IntVar();
	}

	def getIntVar()() :
		return this.IntVar();
	}

	def setIntVar()(= IntVar()) :
		this.IntVar() = IntVar();
	}

	def getIntVar()() :
		return this.IntVar();
	}

	def setIntVar()(= IntVar()) :
		this.IntVar() = IntVar();
	}

	def getIntVar()() :
		return this.IntVar();
	}

	def setIntVar()(= IntVar()) :
		this.IntVar() = IntVar();
	}

	def getIntVar()() :
		return this.IntVar();
	}

	def setIntVar()(= IntVar()) :
		this.IntVar() = IntVar();
	}

	def getIntVar()() :
		return this.IntVar();
	}

	def setIntVar()(= IntVar()) :
		this.IntVar() = IntVar();
	}

	def getIntVar()() :
		return this.IntVar();
	}

	def setIntVar()(= IntVar()) :
		this.IntVar() = IntVar();
	}

	def getIntVar()() :
		return this.IntVar();
	}

	def setIntVar()(= IntVar()) :
		this.IntVar() = IntVar();
	}

	def getTkinter.LabelFrame()() :
		return this.tkinter.LabelFrame();
	}

	def setTkinter.LabelFrame()(= tkinter.LabelFrame()) :
		this.tkinter.LabelFrame() = tkinter.LabelFrame();
	}

	def getTkinter.Label()() :
		return this.tkinter.Label();
	}

	def setTkinter.Label()(= tkinter.Label()) :
		this.tkinter.Label() = tkinter.Label();
	}

	def getTkinter.Label()() :
		return this.tkinter.Label();
	}

	def setTkinter.Label()(= tkinter.Label()) :
		this.tkinter.Label() = tkinter.Label();
	}

	def getTkiner.Label()() :
		return this.tkiner.Label();
	}

	def setTkiner.Label()(= tkiner.Label()) :
		this.tkiner.Label() = tkiner.Label();
	}

	def getTkinter.Label()() :
		return this.tkinter.Label();
	}

	def setTkinter.Label()(= tkinter.Label()) :
		this.tkinter.Label() = tkinter.Label();
	}

	def getTkinter.Label()() :
		return this.tkinter.Label();
	}

	def setTkinter.Label()(= tkinter.Label()) :
		this.tkinter.Label() = tkinter.Label();
	}

	def getTkinter.Label()() :
		return this.tkinter.Label();
	}

	def setTkinter.Label()(= tkinter.Label()) :
		this.tkinter.Label() = tkinter.Label();
	}

	def getTkinter.Label()() :
		return this.tkinter.Label();
	}

	def setTkinter.Label()(= tkinter.Label()) :
		this.tkinter.Label() = tkinter.Label();
	}

	def getTkinter.Label()() :
		return this.tkinter.Label();
	}

	def setTkinter.Label()(= tkinter.Label()) :
		this.tkinter.Label() = tkinter.Label();
	}

	def getTkinter.Label()() :
		return this.tkinter.Label();
	}

	def setTkinter.Label()(= tkinter.Label()) :
		this.tkinter.Label() = tkinter.Label();
	}

	def getTkinter.Label()() :
		return this.tkinter.Label();
	}

	def setTkinter.Label()(= tkinter.Label()) :
		this.tkinter.Label() = tkinter.Label();
	}

 




