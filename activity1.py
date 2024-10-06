#Importing tkinter module
from tkinter import*

#creating the tkinter window
root = Tk()

#creating a button
btn = Button(root,text = "Click me!",background = "#23395B",command = root.destroy)

#position the button
btn.pack(side = "top")

root.mainloop()