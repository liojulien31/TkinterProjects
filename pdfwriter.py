#All in one pdf reader typewriter, paint app using tkinter and python3
from tkinter import * 
import PyPDF2
from pathlib import Path  # for directory listing
from time import sleep
from tkinter import scrolledtext
from pygame import mixer
from tkinter.filedialog import askopenfilename

#pdffile = location
root = Tk()
root.geometry('1000x200')
root['bg'] = "#ffb3ff"
root.title("PDF READER WITH TKINTER AND PYTHON3")
#use withdraw to hide filedialog window
root.withdraw()
location = askopenfilename()
root.deiconify()


#Setting the pdf file for reading and typing on the canvas 
reader = PyPDF2.PdfFileReader(location)
total_pages = reader.numPages   #for total number of pages
content = ""
for pages in range(total_pages):
    next_page = reader.getPage(pages)
    content += next_page.extractText()
    pages += 1

#reader class 
class Reader:
    def __init__(self,pdffile_content,canvas):
        self.c = canvas
        self.pdf =  pdffile_content
        
        self.b1 = Button(root, text='START',width="10",bg="#766FDA",command=self.nextpage)
        self.b1.place(x=0,y=10)
        self.b2 = Button(root, text='Nmod',width="10", bg="#766FDA",command=self.theme_change)
        self.b2.place(x=0,y=40)
        self.b3 = Button(root, text='Font+',width="10",bg="#766FDA", command=self.font_change)
        self.b3.place(x=0,y=70)
        self.b4 = Button(root, text='Quit ',width="10",bg="#766FDA", command=self.Quit)
        self.b4.place(x=0,y=100)
        self.b5 = Button(root, text='Pause',width="10",bg="#766FDA", command=self.pause)
        self.b5.place(x=0,y=130)
        #Colors palet and buttons for picker function
        self.l = Label(root,text="pick a color : ",bg="#ffb3ff")
        self.l.place(x=10,y=190)
        colors = ['red','blue','yellow','purple','green','black','white']
        for i in range(len(colors)):
            self.b = Button(root,bg=[colors[i]],text=' ',command=self.pick_color)
            self.b.place(x=20,y=(220+i*30))
    
        #default colors
        global color
        color = "red"
        self.color = color
        self.count = 0

        # draw lines to underline text and for other user staffs!
        self.c.bind( "<B1-Motion>", self.draw ) 
        #self.c.configure(scrollregion = self.c.bbox("all"))
        #self.c.bind("<1>",     lambda event: self.c.focus_set())
        #self.c.bind("<Left>",  lambda event: self.c.xview_scroll(-1, "units"))
        #self.c.bind("<Right>", lambda event: self.c.xview_scroll( 1, "units"))
        self.c.bind("<Up>",    lambda event: self.c.yview_scroll(-1, "units"))
        self.c.bind("<Down>",  lambda event: self.c.yview_scroll( 1, "units"))

        self.c.focus_set()
        #create an entry just to take some notes.
        self.text_area = Text(root,width=20, height=10,font=("Times New Roman", 15))
        #global text_a
        #text_a = self.c.create_window(10, 50, window=self.text_area,tags="tag")
        # Make the bounding-box around text
        #self.bbox=self.c.bbox(text_a)
        self.page_text = self.c.create_text(10,0,text=" TKINTER GUI APP DEVELOPPMENT IN PYTHON3",fill="black",anchor='nw' ,width=900,font=('Helvetica 10 bold'))
     
    def music(self):
        mixer.init()
        mixer.music.load("winer.wav")
        mixer.music.play()
    def pick_color(self):
        color = self.b.cget("bg")
        self.color = color
        self.text_area['fg'] = color
        self.music()
    # Function to draw on the screen canvas!
    def draw(self,event):
        # Coordinates x and y 
        x1, y1, x2, y2 = ( event.x  ),( event.y ), ( event.x +1),( event.y +1)
        # drawing a line every time user clicks on mouse 
        self.c.create_line( x1, y1, x2, y2, fill = self.color ,width="5",tags="lines")
        if self.color == "white":
            self.c.delete("lines")
       
    def nextpage(self,count=1):
        #page_text = self.c.create_text(0,0,text="PDF FILE READER AND TYPE WRITER USING TKINTER PYTHON3 ",fill="black",anchor='nw' ,width=1000,font=('Helvetica 10 bold'))
        self.c.itemconfigure(self.page_text,text=self.pdf[:count])
        if count < len(self.pdf):
            self.c.after(150,lambda:self.nextpage(count+1))

    def theme_change(self):
    
        if self.count %2 == 0:
            self.music()
            self.c['bg']= "black"
            self.c.itemconfigure(self.page_text,fill="white")
            self.count += 1
        else:
            self.music()
            self.c['bg'] == "white"
            self.c.itemconfigure(self.page_text,fill="black")
            self.count = 0
        
    def font_change(self):
        
        if self.count %2 == 0:
            self.c.itemconfigure(self.page_text,font=('Comic Sans MS', 14))
            self.count += 1 
        else:
            self.c.itemconfigure(self.page_text,font=('Helvetica 10 bold'))
            self.count = 0
        self.music()
        
    def Quit(self):
        self.music()
        root.destroy()
    def pause(self):
        self.count += 1
        if self.count %2 == 0:
            self.music()
            sleep(10)
        else:
            self.music()
            sleep(0)
    
txt = "\'WITH GREAT POWER COMES GREAT RESPONSABILITIES\' ,\nWelcome There \nThis is Hech instructor\nTkinter gui programming\nGOOD LUCK!"
#Simple type writer 
def intro(count=1):
    c.itemconfigure(splash,text=txt[:count])
    if count < len(txt)+1:
            root.after(150,lambda:intro(count+1))
    if count == len(txt)+1:
        sleep(5)
        c.delete(splash)
        btn.pack_forget()
       
btn = Button(root,text="START",font=("",25),fg="black",width="10",command=intro)
btn.pack()
c = Canvas( root, width = 1500, height = 1500,bg = "#fcffcf")
c.pack(padx=125,pady=20,expand=True,fill="both")
splash = c.create_text(100,50,text="Click the start button to start! ",fill="purple",anchor="nw",font=("",20))
root.update()
#call the Reader class 
obj = Reader(content,c)
root.mainloop()