# from tkinter import *
# from PIL import Image, ImageTk
#
# top = Tk()
# top.geometry("800x700")
#
#
# def resize_image(event):
#     new_width = event.width
#     new_height = event.height
#     image = copy_of_image.resize((new_width, new_height))
#     photo = ImageTk.PhotoImage(image)
#     label.config(image=photo)
#     label.image = photo  # avoid garbage collection
#
#
# image = Image.open('/Users/nagaanveshkunuguntla/Desktop/PythonProjects/SampleProject/anvesh/img.png')
# copy_of_image = image.copy()
# # c = Canvas(top, bg="gray16", height=200, width=200)
# photo = ImageTk.PhotoImage(image)
#
# # filename = PhotoImage(file="/Users/nagaanveshkunuguntla/Desktop/PythonProjects/SampleProject/anvesh/img.png")
# label = Label(top, image=photo)
#
# # label.bind('<Configure>', resize_image)
# label.pack(fill=BOTH, expand=YES)
# label.place(x=0, y=0)
# frame1 = Frame(top, bg="#88cffa")
# frame1.pack(pady=20)
# button = Button(text="Click me")
# button1 = Button(frame1, text="Exit")
# button1.pack(pady=20)
#
# button2 = Button(frame1, text="Start")
# button2.pack(pady=20)
#
# button3 = Button(frame1, text="Reset")
# button3.pack(pady=20)
# button.pack()
# top.mainloop()
#
# # button.pack()

# Import the required libraries
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of Tkinter Frame
win = Tk()

# Set the geometry of Tkinter Frame
win.geometry("700x450")

# Open the Image File
bg = ImageTk.PhotoImage(file="/Users/nagaanveshkunuguntla/Desktop/PythonProjects/SampleProject/anvesh/img.png")

# Create a Canvas
canvas = Canvas(win, width=1000, height=3500)
canvas.pack(fill=BOTH, expand=True)

# Add Image inside the Canvas
canvas.create_image(0, 0, image=bg, anchor='nw')


# Function to resize the window
def resize_image(e):
    global image, resized, image2
    # open image to resize it
    image = Image.open("/Users/nagaanveshkunuguntla/Desktop/PythonProjects/SampleProject/anvesh/img.png")
    # resize the image with width and height of root
    resized = image.resize((e.width, e.height), Image.ANTIALIAS)

    image2 = ImageTk.PhotoImage(resized)

    canvas.create_image(0, 0, image=image2, anchor='nw')


btn = Button(canvas, text='Welcome to Tkinter!', width=20,
             height=3, bd='10', command=canvas.destroy)
btn2 = Button(canvas, text='Welcome to Tkinter!', width=20,
              height=3, bd='10', command=canvas.destroy)
bt3 = Button(canvas, text='Welcome to Tkinter!', width=20,
             height=3, bd='10', command=canvas.destroy)
win.bind("<Configure>", resize_image)

btn.place(x=100, y=150)
btn2.place(x=150, y=200)
bt3.place(x=200, y=250)

# Bind the function to configure the parent window
win.mainloop()
