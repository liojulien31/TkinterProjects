#How to create a rectange in tkinter canvas
from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("CANVAS RECTANGLES")
c = Canvas(root,width=200,height=200,bg="black")
c.pack()
c.create_oval(10,20,200,100,fill="blue")
root.mainloop()