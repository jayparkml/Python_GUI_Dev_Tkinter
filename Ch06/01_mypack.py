#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

# code goes here
label = ttk.Label(root, text="Hello, Tkinter!",
          background = "yellow")
label.pack(side= LEFT, anchor = 'nw')

print(label)

ttk.Label(root, text="Hello, Tkinter!",
          background = "blue").pack(side= LEFT, padx=10, pady=10)
ttk.Label(root, text="Hello, Tkinter!",
          background = "green").pack(side= LEFT, ipadx = 10, ipady = 10)          

for widget in root.pack_slaves():
    widget.pack_configure(fill=BOTH, expand=True)
    print(widget.pack_info())#properties


root.mainloop()
