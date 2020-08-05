from tkinter import *
from tkinter import ttk

root = Tk()

label = ttk.Label(root, text = "Hello, Tkinter")
label.pack()
label.config(text = "Howdy, Tkinter!")
label.config(text = "Howdy, Tkinter! It\'s been a while since we last met. Great to see you again")
label.config(wraplength = 150) #150 px width
label.config(justify = CENTER) #left, right center in all caps
label.config(foreground = 'blue', background= 'yellow') #text color, background color
label.config(font = ('Courier', 18, 'bold')) #font, size, style
label.config(text = "Howdy, Tkinter!")
logo = PhotoImage(file = "python_logo.gif") #open the file save into logo
label.config(image = logo)
label.config(compound= 'text')
label.config(compound= 'center')
label.config(compound= 'left')
label.img = logo # reference to logo so that it will not be garbage collected
label.config(image=label.img)



root.mainloop()