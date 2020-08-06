#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

# code goes here
text = Text(root, width=40, height=10, wrap='word')
text.grid(row=0, column=0)
scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=text.yview)#root
scrollbar.grid(row=0, column=1, sticky='ns')
text.config(yscrollcommand= scrollbar.set)




root.mainloop()
