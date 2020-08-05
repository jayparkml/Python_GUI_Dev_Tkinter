#!/usr/bin/python3
# widgets.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import * #all of the function from basic tkinter
from tkinter import ttk #themed tk widget

root = Tk() # top level window

button = ttk.Button(root, text = 'Click Me')
button.pack()

print(button['text'])
button['text'] = 'Press Me' #assigning new value
button.config(text = 'Push Me')
print(button.config())

print(str(button))
print(str(root))

ttk.Label(root, text ='Hello, Tkinter!').pack()

# mainloop() add
root.mainloop()
