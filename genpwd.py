#Python program to generate list of passwords with tkinter gui
from tkinter import *
import random

root = Tk()
root.geometry("800x200")
root.title("WPA PASSWORDS GENERATOR")
#set background with image
# Add image file
bg = PhotoImage(file = "./Icons/bulldog.png")
# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)

#function to set the length of the password
def pwdgen():
	global E
	ln = E.get()
	pwd = ""
	i = 0
	while i < int(ln):
		#You can added more characters to the choice method that will return one char in each iteration
		pwd += random.choice("abX1cX3YdefVghijklWmUnZop0qrs4tuvw2xyzABC5DEF8GHIJKLMNOPQRS9T67!=+*?#/")
		i += 1
	return pwd

#This function will generate the total list of password and save it in an external file
def pwdformat():
	root.config(bg="blue")
	global E2
	maxc = E2.get()
	c = 0
	pwd = ""
	f = open("pwdgenerated.txt","a")
	while c < int(maxc):
		pwd = pwdgen()+ "\n"
		f.write(pwd)
		c += 1
	f.close()
	E.pack_forget()
	E2.pack_forget()
	l.pack_forget()
	l2.pack_forget()
	txt = "TASK FINISHED AND "+ maxc + " PASSWORDS ARE GENERATED"
	l3.config(text=txt)
	
#Gui components and widgets
b = Button(root,text="GENERATEPWD",command=pwdformat)
b.pack()
l = Label(root,text="Enter pass length: ",fg="black", font=('Helvetica 20 bold'))
l.pack()
E = Entry(root)
E.pack()
l2 = Label(root,text="Enter maximum number of pwd: ",fg="black", font=('Helvetica 20 bold'))
l2.pack()
E2 = Entry(root)
E2.pack()
E.bind("Button-1",pwdformat)
E2.bind("Button-1",pwdformat)
l.bind("Button-1",pwdformat)
l2.bind("Button-1",pwdformat)
l3 = Label(root,text="",fg="green",font=("Helvetica 20 bold"))
l3.pack()
root.mainloop()
