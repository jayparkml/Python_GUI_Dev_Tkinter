#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

# code goes here
ttk.Label(root, text="Hello, Tkinter!",
          background = "yellow").pack(fill=BOTH, expand=True)
ttk.Label(root, text="Hello, Tkinter!",
          background = "blue").pack(fill=BOTH)
ttk.Label(root, text="Hello, Tkinter!",
          background = "green").pack(fill=BOTH, expand=True)          

root.mainloop()
