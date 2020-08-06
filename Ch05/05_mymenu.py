#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

# code goes here
root.option_add('*tearOff', False) #not create tearible menu
menubar = Menu(root)
root.config(menu=menubar)
file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)
menubar.add_cascade(menu = file, label = "File")
menubar.add_cascade(menu = edit, label = "edit")
menubar.add_cascade(menu = help, label = "help")
file.add_command(label="New", command= lambda: print("New File"))
file.add_separator()
file.add_command(label="Open...", command= lambda: print("Opening File..."))
file.add_command(label="Save", command= lambda: print("Save File"))
file.entryconfig('New', accelerator = "Ctrl+N")

logo = PhotoImage(file='python_logo.gif').subsample(10,10)
file.entryconfig('Open...', image=logo, compound='left')
file.entryconfig('Open...', state='disabled')
file.delete("Save")

save = Menu(file) #Creating save menu in file menu
file.add_cascade(menu = save, label = "Save")
save.add_command(label="Save As", command= lambda: print("Saving As..."))
save.add_command(label="Save All", command= lambda: print("Saving All..."))


choice = IntVar()
edit.add_radiobutton(label = "One", variable=choice, value=1)
edit.add_radiobutton(label = "Two", variable=choice, value=2)
edit.add_radiobutton(label = "Three", variable=choice, value=3)

file.post(400,300)



root.mainloop()
