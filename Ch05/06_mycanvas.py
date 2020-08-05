#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

# code goes here
canvas = Canvas(root)
canvas.pack()
canvas.config(width=640, height=480)
line = canvas.create_line(160, 360, 480, 120, fill='blue', width=5)
canvas.itemconfig(line, fill='green')
canvas.coords(line)
canvas.coords(line, 0, 0, 320, 240, 640, 0)
canvas.itemconfigure(line, smooth=True)
canvas.itemconfigure(line, splinesteps=5) #using 5 steps to smooth
canvas.itemconfigure(line, splinesteps=100) #using 100 steps to smooth
canvas.delete(line)




root.mainloop()
