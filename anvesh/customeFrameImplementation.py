import tkinter
import MyFrame

if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry("300x200")
    mycustomeframe = MyFrame.Myframe(root)
    mycustomeframe.pack()
    root.mainloop()
