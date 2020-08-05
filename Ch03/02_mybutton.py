#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk #for new styled or themed(accroding to os) 
    
root = Tk()

# code goes here
button = ttk.Button(root, text="Click Me")
button.pack()

def callback():
    print("Clicked!")

button.config(command=callback)
# button.invoke() #simulate button click
button.state(['disabled']) #disable the button
print(button.instate(['disabled'])) #check
button.state(['!disabled'])

logo = PhotoImage(file="python_logo.gif")
button.config(image=logo, compound=LEFT)
small_logo = logo.subsample(5,5) #make image smaller
button.config(image=small_logo, compound=LEFT)



root.mainloop()
