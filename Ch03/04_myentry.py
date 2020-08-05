#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

# code goes here
entry = ttk.Entry(root, width=30)
entry.pack()
entry.delete(0, 1) #delete the entry by index(start,end)
entry.insert(0, "Enter your password") #insert the entry by index
entry.config(show = "*")
entry.state(['disabled'])
entry.state(['!disabled'])

entry.state(['readonly']) #make it readonly so user only can copy the text


root.mainloop()
