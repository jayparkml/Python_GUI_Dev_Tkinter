#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

# code goes here
btn1 = ttk.Button(root, text= "Button 1")
btn2 = ttk.Button(root, text= "Button 2")
btn1.pack()
btn2.pack()
style = ttk.Style()
print(style.theme_names())
print(style.theme_use())
style.theme_use("classic")
style.theme_use("vista")
print(btn1.winfo_class())
style.configure('TButton', foreground='blue') #change both buttons
style.configure('Alarm.TButton', foreground='orange', 
font=('Arial', 24, 'bold'))
btn2.config(style='Alarm.TButton')
style.map('Alarm.TButton', foreground=[('pressed', 'pink'), 
('disabled', 'grey')])
btn2.state(['disabled'])
print(style.layout("TButton"))#all of elements
print(style.element_options("Button.label")) #list of all options for element
print(style.lookup("TButton", 'foreground'))#current value


root.mainloop()
