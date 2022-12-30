from tkinter import *
from tkinter import ttk


window = Tk()

greeting = window.Label(text="Hello")
window.Button(text="EXIT", command=window.destroy).grid(column=1, row=10)

window.mainloop()

