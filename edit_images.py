
#How to use pillow or pil libraries to edit on images
#At first we need to install pil or pillow library ,see the image 
#Then we need to import those libraries and add choose the image to work on!

#Python code:
#Edit texts on images
from tkinter import *
# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from tkinter.filedialog import askopenfilename

root = Tk()
root.geometry("500x500")
root['bg'] = "#ffdffe"
root.withdraw()
location = askopenfilename()
root.deiconify()
# Open an Image
img = Image.open(location)
# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

def edit_img():
	global txt,x,y,r,g,b
	txt = str(txt.get())
	x = int(x.get())
	y = int(y.get())
	r = int(r.get())
	g = int(g.get())
	b = int(b.get())
	# Add Text to an image
	I1.text((x, y), txt, fill=(r, g, b))
	# Display edited image
	img.show()
	# Save the edited image
	img.save("newbird.png")

txt_label = Label(root,text="Enter text value: ")
txt_label.place(x=10,y=10)
txt = Entry(root)	
txt.place(x=200,y=10)

x_label = Label(root,text="Enter x coordinate: ")
x_label.place(x=10,y=30)
x = Entry(root)	
x.place(x=200,y=30)

y_label = Label(root,text="Enter y coordinate: ")
y_label.place(x=10,y=50)
y = Entry(root)	
y.place(x=200,y=50)

r_label = Label(root,text="Enter r value: ")
r_label.place(x=10,y=70)
r = Entry(root)	
r.place(x=200,y=70)

g_label = Label(root,text="Enter g value: ")
g_label.place(x=10,y=90)
g = Entry(root)	
g.place(x=200,y=90)

b_label = Label(root,text="Enter b value: ")
b_label.place(x=10,y=110)
b = Entry(root)	
b.place(x=200,y=110)


edit = Button(root,text="Edit",command=edit_img)
edit.place(x=250,y=250)


root.mainloop()

"""
# Import tkinter and Button Widget
from tkinter import Tk
from tkinter.ttk import Button
  
  
# Demo function 1
def fun1():
    print("Function 1")
  
  
# Demo function 2
def fun2():
    print("Function 2")
  
  
if __name__ == "__main__":
    # Creating top-level window
    master = Tk()
  
    # Setting window title
    master.title("Bind multiple function to Button")
  
    # Setting window Dimensions
    master.geometry("400x250")
  
    # Creating a button with more than one command using lambda
    button = Button(master, text="Button", command=lambda: [fun1(), fun2()])
  
    # Attaching button to the top-level window
    # Always remember to attach your widgets to the top-level
    button.pack()
  
    # Mainloop that will run forever
    master.mainloop()

#splash screen
# Import module
from tkinter import *

# Create object
splash_root = Tk()

# Adjust size
splash_root.geometry("200x200")
instructions = "Click PLAY button to start the game"
def main():
	# destroy splash window
	splash_root.destroy()

	# Execute tkinter
	root = Tk()

	# Adjust size
	root.geometry("400x400")
	b = Button(root,text="ok")
	b.pack()
def write_instructions(count=1):
	splash_label.config(text=instructions[:count])
	if count < len(instructions):
		splash_root.after(150,write_instructions(count+1))
# Set Label
splash_label = Label(splash_root, text="Splash Screen", font=18)
splash_label.pack()

# main window function

# Set Interval
splash_root.after(6000, main)

# Execute tkinter
mainloop()

from tkinter import *
root = Tk()
root.minsize(200,200)

def onClick(event):
	btn = event.widget #event.widget is the widget that called the event
	whichbtn = btn.cget("bg") #Print the text for the slected button
	print(whichbtn)
lst = ['red','blue','white','green','yellow','black','purple','orange','brown','gold']
for i in range(10):
	b = Button(root,text='B%s'%i)
	b.grid(row = i,column=0)
	b['bg'] = lst[i]
	#Bint to left click which generates an event object
	b.bind("<Button-1>",onClick)


------------------------------------------------------------------------------------------
#Get entry value with bind on return key from the keyboard
# Import the required libraries
from tkinter import *
from PIL import Image, ImageTk

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the window
win.geometry("700x350")

def show_msg(event):
   label["text"]="Sale Up to 50% Off!"

# Create a label widget
label=Label(win, text="Press Enter Key" ,font="TkMenuFont 20")
label.pack(pady=30)

# Bind the Enter Key to the window
win.bind('<Return>', show_msg)

win.mainloop()

----------------------------------------------------------------------------------------------------
from tkinter import *
import random
from time import sleep

def click_handler(event):
    event.widget.itemconfigure("current", fill="white")
    time.sleep(5)
    event.widget.delete("current")

def onClick(event):
	btn = event.widget #event.widget is the widget that called the event
	whichbtn = btn.cget("bg") #Print the text for the slected button
	print(whichbtn)

root = Tk()
canvas = Canvas(root, bg="bisque", width=600, height=600)
canvas.pack(fill="both", expand=True)

canvas.bind("<1>", click_handler)
color = random.choice(("red", "orange", "green", "blue","purple","black","yellow"))
for i in range(1000):
    x = random.randint(0, 350)
    y = random.randint(0, 350)
    width = random.randint(25, 50)
    height = random.randint(25, 50)
    canvas.create_rectangle(x, y, x+width, y+height, fill=color)

score = 0
for i in range(10):
	xpos = random.randint(0,450)
	ypos = random.randint(0,450)
	b = Button(root,text='X')
	b.place(x= xpos,y=ypos)
	b['bg'] = color
	score += 10
	#Bint to left click which generates an event object
	b.bind("<Button-1>",onClick)
	canvas.create_text(root,text="Your score is:%s"%score,font=("",10))

root.mainloop()
"""

