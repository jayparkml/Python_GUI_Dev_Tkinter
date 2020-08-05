#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

# code goes here
frame = ttk.Frame(root)
frame.pack()
frame.config(width=200 , height=100)
frame.config(relief=RIDGE)

ttk.Button(frame, text="Click Me").grid() #grid geometry inside the frame
frame.config(padding=(30,15))
ttk.Labelframe(root, height=100, width=200, text="My Frame").pack()


root.mainloop()
