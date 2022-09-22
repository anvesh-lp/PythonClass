import tkinter
from tkinter import *


class MyCustomMenu(tkinter.Menu):
    def __init__(self, root, **a):
        tkinter.Menu.__init__(self, root, **a)
