#Tkinter porgram to create a quiz from nmap commands 
from tkinter import *
from tkinter import messagebox as mb
from pygame import mixer
import json  #import json to use json file for data

class Quiz:
	def __init__(self):
		self.q_no=0        # set question number to 0
		self.display_title()  #assigns ques to display_question function to update later.
		self.display_question()
		# opt_selected holds int value which is used for selected option in a question.
		self.opt_selected=IntVar()
		self.opts=self.radio_buttons() # displays the current question and its options
		self.display_options() # displays options for the current question
		self.buttons() # displays next and exit buttons.
		self.data_size=len(question) # no of questions
		self.correct=0   # counter of correct answers

	# This method is used to display the result using the message box
	def display_result(self):
		incorrect = self.data_size - self.correct # calculates the wrong answers no
		correct = f"Correct: {self.correct}"
		wrong = f"Wrong: {incorrect}"
		score = int(self.correct / self.data_size * 100)  # calcultaes the percentage of correct answers
		avg = f"Score: {score}%"
		# Shows a message box to display the result
		mb.showinfo("Result", f"{avg}\n{correct}\n{wrong}")

	# This method checks the Answer after we click on Next.
	def check_ans(self, q_no):
		# checks for if the selected option is correct
		if self.opt_selected.get() == answer[q_no]:
			# if the option is correct it return true
			return True

	# This method is used as a switch to check correct answer and display next question
	def next_btn(self):
		# Check if the answer is correct it increments correct variable by 1
		if self.check_ans(self.q_no):
			self.correct += 1
			mixer.init()
			mixer.music.load("winer.wav")
			mixer.music.play()
		# Moves to next Question by incrementing the q_no counter
		self.q_no += 1
		# checks if the q_no size is equal to the data size
		if self.q_no==self.data_size:
			self.display_result()
			mixer.init()
			mixer.music.load("win.wav")
			mixer.music.play()   # if it is correct then it displays the score and quit
			gui.destroy()
		else:  # shows the next question
			self.display_question()
			self.display_options()

	# This method shows the two buttons on the screen.
	def buttons(self):
		nextb = Button(gui, text="Next",command=self.next_btn,width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
		nextb.place(x=200,y=380)
		quitb = Button(gui, text="Quit", command=gui.destroy,width=5,bg="black", fg="white",font=("ariel",16," bold"))
		quitb.place(x=400,y=380)

	# This method deselect the radio button on the screen by deselecting the options
	def display_options(self):
		val=0
		self.opt_selected.set(0)
		# looping over the options to be displayed for the text of the radio buttons.
		for option in options[self.q_no]:
			self.opts[val]['text']=option
			val+=1
	# This method shows the current Question on screen and set the Question properties
	def display_question(self):
		q_no = Label(gui, text=question[self.q_no], width=60,font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
		q_no.place(x=70, y=100)

	# This method is used to Display Title
	def display_title(self):
		title = Label(gui, text="NMAP FAMOUS COMMAND QUIZ",width=50, bg="black",fg="white", font=("ariel", 20, "bold"))
		title.place(x=0, y=2)

	# This method shows the radio buttons to select the Question
	def radio_buttons(self):
		q_list = []   			# initialize the list with an empty list of options
		y_pos = 150   			# position of the first option
		while len(q_list) < 5: # adding the options to the list and setting the radio button properties
			radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,value = len(q_list)+1,font = ("ariel",14))
			q_list.append(radio_btn)  			# adding the button to the list
			radio_btn.place(x = 100, y = y_pos)
			y_pos += 40 		 				# incrementing the y-axis position by 40
		return q_list

gui = Tk()
gui.geometry("800x450")
gui['bg'] = "black"
gui.title("NMAP COMMANDS REVESION")

with open('data.json') as f: data = json.load(f) # get the data from the json file
question = (data['question']) 	# set the question, options, and answer
options = (data['options'])
answer = (data[ 'answer'])
q = Quiz()
gui.mainloop()