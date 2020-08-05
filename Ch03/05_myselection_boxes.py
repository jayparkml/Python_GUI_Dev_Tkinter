#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

# code goes here
month = StringVar()
combobox = ttk.Combobox(root, textvariable= month)
combobox.pack()
combobox.config(values= ["Jan", "Feb", "Mar", "Apr", "May", "Jun"])
month.get()
month.set('Mar') #little risky cuz you can setup value which not exist
year = StringVar()
Spinbox(root, from_=1990, to = 2014, textvariable=year).pack()
year.get()


root.mainloop()
