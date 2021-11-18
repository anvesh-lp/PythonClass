import sys
import tkinter
import Person


class Myframe(tkinter.Frame):
    def __init__(self, root):
        tkinter.Frame.__init__(self, root)
        self.label = tkinter.Label(self, text="Hello world")
        self.button = tkinter.Button(self, text="get Data")
        self.button2 = tkinter.Button(self, text="Print doc function")
        self.label.pack()
        self.button.pack()
        self.button2.pack()
        self.button.bind("<1>", self.GetData)
        self.button2.bind("<1>", self.printdoc)
        self.person1 = Person.Person("anvesh", "Kunuguntla")

    def quit(self, event=None):
        sys.exit()

    def newButton(self, event=None):
        button = tkinter.Button(self, text="new button created")
        button.pack()

    def GetData(self,event=None):

        label = tkinter.Label(self, text=self.person1.printData())
        label.pack()

    def printdoc(self,event=None):
        label = tkinter.Label(self, text="this is the doc function")
        label2 = tkinter.Label(self, text=Person.Person.__doc__)
        label.pack()
        label2.pack()
