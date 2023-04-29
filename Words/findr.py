
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import Tk  

root = Tk()
root.geometry('1000x200')
root['bg'] = "#ffb3ff"
root.title("FIND AND REPLACE WORDS")
#use withdraw to hide filedialog window
root.withdraw()
location = askopenfilename()
root.deiconify()

#call this function after clicking button replace   
def replace():
  # Read in the file
  with open(location, 'r') as file :
    filedata = file.read()
  # Replace the target string
  to_replace = str(e.get()) #---> old word canvas also use upper/lower method to replace word with upper case !
  new_word = str(r.get())  #---> new word c 
  if to_replace in filedata :
    filedata = filedata.replace(to_replace, new_word)
    # Write the file out again
    with open(location, 'w') as file:
      file.write(filedata)
    L = Label(root,text="DONE!All occurences of the word %s are replaced by the word %s"%(to_replace,new_word),fg="#232121").place(x=200,y=140)
  else:
    L = Label(root,text="The word %s is Not Found"%to_replace,fg="#232121").place(x=200,y=140)

L1 = Label(root,text="ENTER TEXT TO REPLACE",fg="#202121").place(x=10,y=10)
#This is an entry , or the box in which user can input or type the word to find and replace
e = Entry(root)
e.place(x=200,y=10)
L2 = Label(root,text="ENTER NEW WORD",fg="#222121").place(x=10,y=50)
#This is the second entry for user input, this is where the new word variable will be putted in!
r = Entry(root)
r.place(x=200,y=50)
button = Button(root,text='REPLACE',command=replace)
button.place(x=200,y=80)
root.mainloop()