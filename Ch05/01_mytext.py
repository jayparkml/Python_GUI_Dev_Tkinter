#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

# code goes here
text= Text(root, width = 40, height = 10)
text.pack()
text.config(wrap='word') #'char', 'none'
text.insert('1.0 + 2 lines', "Inserted Message")
text.insert("1.0 + 2 lines lineend", " and\nmore and\nmore...")
text.get('1.0', "end")
text.get('1.0', "1.end")
text.delete("1.0") #beginning index
text.delete('1.0', '1.0 lineend') #still have newline character
text.delete('1.0', '3.0 lineend + 1 chars') #include new line character
text.replace('1.0', '1.0 lineend', 'This is the first line')
text.config(state='disabled') # no longer able to type in text
text.delete('1.0', 'end')
text.config(state='normal')

text.tag_add('my_tag', '1.0', '1.0 wordend')
text.tag_configure('my_tag', background='yellow')
text.tag_remove('my_tag', '1.1', '1.3')
print(text.tag_ranges('my_tag'))
print(text.tag_names())
text.tag_names('1.0')
text.replace('my_tag.first', 'my_tag.last', 'That') # replace text by tag
text.tag_delete('my_tag')
text.mark_names()
text.insert('insert', '_')
text.mark_set('my_mark', 'end')
text.mark_gravity('my_mark', 'right')

text.mark_unset('my_mark')
image=PhotoImage(file="python_logo.gif")
text.image_create('insert', image=image)
btn = Button(text, text="Click Me")
text.window_create('insert', window=btn)


root.mainloop()
