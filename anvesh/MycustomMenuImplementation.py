# from tkinter im
import tkinter

from MyCustomMenu import MyCustomMenu
# from tkinter import *
import tkinter


def hello(event):
    print("hello")


window = tkinter.Tk()
mycustomemenu = MyCustomMenu(window)
# fileMenu = tkinter.Menu(mycustomemenu, tearoff=0)
mycustomemenu.add_cascade(label="File", menu=mycustomemenu)
window.config(menu=mycustomemenu)
window.mainloop()
