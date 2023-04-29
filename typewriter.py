#importing all required package for tkinter 
from tkinter import *
import random
#setting root window
root = Tk()
root.geometry('1000x200')
root['bg'] = "black"
root.title("TYPEWRITER WITH TKINTER AND PYTHON3")


txt = "\t Hello there and welcome in new programming course\n\t\t That is all today thanks for watching and see you later.!"
#Simple type writer 

#function called when button btn is clicked!
def intro(count=1):
  
    c.itemconfigure(splash,text=txt[:count])
    if count < len(txt)+1:
            #delete the splash text and hide the start button
            btn.pack_forget()
            root.after(250,lambda:intro(count+1))
            

btn = Button(root,text="START",font=("",25),fg="black",width="10",command=intro)
btn.pack()
c = Canvas( root, width = 500, height = 500,bg = "blue")
c.pack(padx=100,pady=100)
splash = c.create_text(100,150,text="Click the start button to start! ",fill="purple",anchor="center",font=("",20))
root.mainloop()