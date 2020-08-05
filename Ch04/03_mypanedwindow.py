#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

# code goes here
panedwindow = ttk.Panedwindow(root, orient= HORIZONTAL)
panedwindow.pack(fill=BOTH, expand=True)
frame1 = ttk.Frame(panedwindow, width=100, height=300, relief=SUNKEN)
frame2 = ttk.Frame(panedwindow, width=400, height=400, relief=SUNKEN)

panedwindow.add(frame1, weight=1) #weight=how much frame will be scaled
panedwindow.add(frame2, weight=4) #4times the weight of frame 1
frame3 = ttk.Frame(panedwindow, width=50, height=400, relief=SUNKEN)
panedwindow.insert(1,frame3)#insert the frame into index 1
panedwindow.forget(1)

root.mainloop()
