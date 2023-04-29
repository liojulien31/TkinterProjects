from tkinter import *
import random
#from tkinter.font import *

root = Tk()
root.geometry("600x300")

def repeat():
    global timer
    rand = random.choice(["Hello","FROM","TOWN","DOG","CAT","FREE","Call","Small"])
    # configuring the tag, to overcome over writing of text.
    cv.itemconfigure('rand', text=rand)
    # asking to repeat it, you can change the interval.
    timer = root.after(10000, repeat)

def stop():
    root.after_cancel(timer)

def check(event):
    global score
    s = entry.get()
    if s != "":
        if str(s) == cv.itemcget(txt,"text"):
            score += 10
            score_label.configure(text=str(score))
        else:
            score += -1
            score_label.configure(text=str(score))

global score
score = 0
entry_label = Label(root, text="Click Enter to submit your typing",font=("calibri", 20, "bold"),fg="black")
entry_label.place(x=200,y=5)
entry = Entry(root)
entry.place(x=200,y=30)
cv = Canvas(root, width=200, height=200, bg="blue")
cv.place(x=310,y=50)
txt = cv.create_text(100, 100, font=("calibri", 20, "bold"),fill="lightblue", tag='rand')  # added a tag
score_label = Label(root, text="0.0",font=("calibri", 20, "bold"),fg="black") 
score_label.place(x=20,y=20)
b_start = Button(root, text='Start', command=repeat,width=10)
b_start.place(x=200,y=70)
root.bind("<Return>",check)
b_stop = Button(root, text='Stop', command=stop,width=10)
b_stop.place(x=200,y=220)
root.mainloop()