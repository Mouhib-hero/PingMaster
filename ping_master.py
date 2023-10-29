# coding: utf-8
 
from tkinter import * 
import tkinter.messagebox
import time
import schedule
import tkinter.font as font
from tkcalendar import DateEntry
from tkinter import messagebox
import pycron
import sqlite3
from  tkinter import ttk
import io
import os.path
import json


from PIL import ImageTk, Image  

import subprocess, sys 

from threading import *

import datetime
#from mailer import Mailer
import smtplib

from win32api import GetMonitorInfo, MonitorFromPoint

from apscheduler.schedulers.background import BlockingScheduler


conn = sqlite3.connect(r'Database\testpython.db')

c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS results(Time text, IP text, State text)")


############________functions

def clear1():
	T.delete("1.0","end")

def refresh():
	global temps
	#formattingDateOptions
	temps = str(datetime.datetime.now().strftime('%A %d/%m/%Y %H:%M:%S'))

	labeltime = Label(fenetre,text = "Last refresh : " + temps,bg="#ede3ff")
	labeltime_canvas = canvas1.create_window(220,490,  anchor = "nw", window = labeltime)

	T.delete("1.0","end")
	f = open(r'IP_addresses\AdresseIP.txt','r')
	data = f.read()
	T.insert(END,data)
	tkinter.messagebox.showinfo("Refresh",  "Done Refreshing.")
	f.flush()
	f.close()
def save():
	f = open(r'IP_addresses\AdresseIP.txt','r')
	f.write(T.get("1.0","end"))
	tkinter.messagebox.showinfo("Save Modifications",  "File modified successfully.")
	f.flush()
	f.close()
	
###_______________SECOND_WINDOW_________#####
def clear2():
	T2.delete("1.0","end")

def refresh2():
	global temps2
	#formattingDateOptions
	temps2 = str(datetime.datetime.now().strftime('%A %d/%m/%Y %H:%M:%S'))

	labeltime2 = Label(fenetre,text = "Last refresh : " + temps2,bg='#e8ccff')
	labeltime_canvas2 = canvas1.create_window(826,542,  anchor = "nw", window = labeltime2)


	T2.delete("1.0","end")
	f = open(r'Results\PingResults.txt','r')
	data = f.read()
	f.flush()
	f.close()
	T2.insert(END,data)
	T2.see(END)
	if (cb.get()):
		tkinter.messagebox.showinfo("Refresh",  "Done Refreshing.")
def save2():
	if (testIsRunning == False):
		f = open(r'Results\PingResults.txt','w+')
		f.write(T2.get("1.0","end"))
		tkinter.messagebox.showinfo("Save Modifications",  "File modified successfully.")
		f.flush()
		f.close()
	elif (testIsRunning == True):
		tkinter.messagebox.showerror("Save File Error",  "Error: Cannot save file while connection test is running.\nMake sur that connection test is stopped.")
		

def rate():
	global stopIsClicked	
	global task
	global refState
	refState = False
	global refRate
	refRate=T3.get("1.0","end")
	if(refRate.strip().isdigit()):
		if (cb.get()):
			tkinter.messagebox.showinfo("Auto Refresh Rate",  "The Connection test results\n will be refreshed every "+refRate+" seconds.")
		refState = True
		
		stopIsClicked = False
		task = fenetre.after(int(refRate)*1000,job)
	else:
		if (cb.get()):
			tkinter.messagebox.showerror("Auto Refresh Rate",  "Error: Please set a correct value.")
		refState = None
stopIsClicked = False	
#checkBoxClicked
def stopRef():
	global checkBoxClicked
	global stopIsClicked	
	global refState	
	if (refState):
		stopIsClicked = True
		refState = False
		if (cb.get()):
			tkinter.messagebox.showinfo("Save Modifications",  "Auto refresh stopped successfully.")
	elif (stopIsClicked == True or refState == False):
		if (cb.get()):
			tkinter.messagebox.showinfo("Stop Auto Refresh",  "Auto refresh is already stopped.")
	elif (refState == None):
		if (cb.get()):
			tkinter.messagebox.showerror("Stop Auto Refresh",  "Auto refresh isn't enabled yet.")


	
def job():
	global stopIsClicked	
	if (stopIsClicked == False):
		refresh2()
		task = fenetre.after(int(refRate)*1000,job)


############################
#Create Object
fenetre = Tk()

#Title
fenetre.title("PingMaster")

#Adjust size
#fenetre.geometry("1000x500")
fenetre.resizable(0, 0) #Don't allow resizing in the x or y direction

#To center the window

window_height = 600 
window_width = 1100 

screen_width = fenetre.winfo_screenwidth()
screen_height = fenetre.winfo_screenheight()

##  Task Bar Height
monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
monitor_area = monitor_info.get("Monitor")
work_area = monitor_info.get("Work")
taskBarHeight = monitor_area[3]-work_area[3]
##

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int(((screen_height-taskBarHeight)/2) - (window_height/2))

fenetre.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
#Add image file
bg = PhotoImage(file = "images\imgtest2.gif")

#create canvas
canvas1 = Canvas(fenetre, width = 1100, height = 600)
canvas1.pack(fill = "both", expand = True)

#Display image
canvas1.create_image(0,0,image=bg,anchor="nw")





##############____MENU_____########################


menu = Menu(fenetre)
fenetre.config(menu=menu)

def exitProgram():
	exit()

img4 =Image.open('images\email.gif')
bg6 = ImageTk.PhotoImage(img4)


var2 = StringVar(value="0")
var3 = StringVar(value="0")
var1 = StringVar(value="0")
def report():
	global var1
	global var2
	global var3
	win2 = Toplevel(fenetre)
	win2.title("Contact Developer")
	
	##
	win2.config(bg='yellow')
	label49 = Label(win2, image=bg6)
	label49.place(x = 0,y = 0)
	##

	win2.resizable(0, 0)
	# get screen width and height
	ws = win2.winfo_screenwidth()
	hs = win2.winfo_screenheight()
	w=626
	h=417
	# calculate position x, y
	x = (ws/2) - (w/2)    
	y = (hs/2) - (h/2)
	win2.geometry('%dx%d+%d+%d' % (w, h, x, y))
	
	win2.grab_set()
	    
    	# Change the label text
	label1 = Label(win2, text= "Your Subject :",bg='#e0a899',fg='black').place(x=5, y=5)
	
	label2 = Label(win2, text= "Your Message :",bg='#e0a899',fg='black').place(x=5, y=80)
	####
	#password = Text(win2,height=1, width=35,show="*").place(x=5,y=120)
	#email = Entry(win2,textvariable=address ,show=None, font=('Arial', 14)).place(x=5,y=40)
	#password = Entry(win2,textvariable=pass, show='*', font=('Arial', 14)).place(x=5,y=120)  
	#tkinter.messagebox.showerror("Error",  "This feature will be released in upcoming versions.")

	###########_____________SURVEY 
	
	def sel():
		selection = "You selected the option " + str(var1.get())
		label.config(text = selection)
	var1 = StringVar(value="0") #tristate problem, you should initialize the variables to the value of one of the radiobuttons so that they do not get selected all automatically
	Label(win2, text="How many stars do you rate the app?",bg="#8094EC").place(x=350,y=10)
	Radiobutton(win2, text="1/4",variable=var1,value="1/4",command=sel,bg="#EF9393").place(x=350,y=30)
	Radiobutton(win2, text="2/4",variable=var1,value="2/4",command=sel,bg="#EF9393").place(x=350,y=50)
	Radiobutton(win2, text="3/4",variable=var1,value="3/4",command=sel,bg="#EF9393").place(x=350,y=70)
	Radiobutton(win2, text="4/4",variable=var1,value="4/4",command=sel,bg="#EF9393").place(x=350,y=90)
	label = Label(win2)
	label.place(x=375,y=120)
	
	
	def sel2():
		selection = "You selected the option " + str(var2.get())
		label2.config(text = selection)
	var2 = StringVar(value="0") #tristate problem, you should initialize the variables to the value of one of the radiobuttons so that they do not get selected all automatically
	Label(win2, text="How likely are you to recommend the app?",bg="#8094EC").place(x=350,y=150)
	Radiobutton(win2, text="1/4",variable=var2,value="1/4",command=sel2,bg="#EF9393").place(x=350,y=170)
	Radiobutton(win2, text="2/4",variable=var2,value="2/4",command=sel2,bg="#EF9393").place(x=350,y=190)
	Radiobutton(win2, text="3/4",variable=var2,value="3/4",command=sel2,bg="#EF9393").place(x=350,y=210)
	Radiobutton(win2, text="4/4",variable=var2,value="4/4",command=sel2,bg="#EF9393").place(x=350,y=230)
	label2 = Label(win2)
	label2.place(x=375,y=260)



	def sel3():
		selection = "You selected the option " + str(var3.get())
		label3.config(text = selection)
	var3 = StringVar(value="0") #tristate problem, you should initialize the variables to the value of one of the radiobuttons so that they do not get selected all automatically
	Label(win2, text="Did the app help you accomplish your goal?",bg="#8094EC").place(x=350,y=285)
	Radiobutton(win2, text="Yes.",variable=var3,value="Yes",command=sel3,bg="#EF9393").place(x=350,y=305)
	Radiobutton(win2, text="Partially.",variable=var3,value="Partially",command=sel3,bg="#EF9393").place(x=350,y=325)
	Radiobutton(win2, text="No but it was useful.",variable=var3,value="No but it was useful.",command=sel3,bg="#EF9393").place(x=350,y=345)
	Radiobutton(win2, text="Not at all.",variable=var3,value="Not at all",command=sel3,bg="#EF9393").place(x=350,y=365)
	label3 = Label(win2)
	label3.place(x=375,y=395)


	####_________ EMAIL
	obj = StringVar()
	msg = StringVar()
	object = Entry(win2,textvariable=obj,show=None, font=('Arial', 12))
	object.bind('<Return>', test)
	object.place(x=5,y=40)
	message = Text(win2, show=None, width = 25, height = 5, font=('Arial', 10))
	message.place(x=5,y=120)  

	def sendMail():
		global var1
		global var2
		global var3
		def survey():
			surveyResult="No Survey."
			if not(var1.get()=="0") or not(var2.get()=="0") or not(var3.get()=="0"):
				surveyResult = "App rate : "+var1.get()+"\nRecommonding the app : "+var2.get()+"\nApp & goal accomplishment : "+var3.get()
			return(surveyResult)
		#Put your sender email in the json file (with your SMTP)
		with open("config.json", "r") as config_file:
			config = json.load(config_file)
		sender_email = config["sender_email"]
		sender_password = config["sender_password"]
		smtp_server = config["smtp_server"]
		smtp_port = config["smtp_port"]
		server = smtplib.SMTP(smtp_server, smtp_port)
		server.starttls()
		server.login(sender_email,sender_password)
		receiver_email = config["receiver_email"]
		if not (len(obj.get().strip())):
			tkinter.messagebox.showerror("Send Email Error",  "Cannot send an email with an empty subject.")
		if not (len(message.get("1.0","end").strip())):
			tkinter.messagebox.showerror("Send Email Error",  "Cannot send an email with an empty message.")
		else:
			BODY = "\r\n".join((
			"*** From: %s" % sender_email,
			"*** To: %s" % receiver_email,
			"---------------------",
			"Subject: %s" % obj.get() ,
			"---------------------",
			"",
			message.get("1.0","end"),
			"",
			"---------------------",
			survey(),
			str(datetime.datetime.now().strftime('%A %d/%m/%Y %H:%M:%S')),
			"---------------------",
	
			))
			print(BODY)
			#server.sendmail(sender_email,receiver_email,BODY) ###!!!!!!!!  ACTIVATE TO SEND MAIL  !!!!!!!!!!
	    
			object.delete(0,END)
			message.insert(END,"")
			tkinter.messagebox.showinfo("Contact Developer",  "Message sent.\nThank you for your feedback!")
	
	button5 = Button(win2,text = "Send", command=sendMail).place(x=10,y=220)
	labelplease = Label(win2, text= " - Please do our survey on the right ! ! \nIt's simple but it helps us a lot !!\nIt will only take a few seconds.",bg='#7D89EC',fg='black').place(x=5, y=270)
	labelthanks = Label(win2, text= " Thank you for using this application !\nAll rights reserved © 2022.",font=('Arial', 8),bg='#21243F',fg='white').place(x=5, y=360)
	def on_close():
		win2.grab_release()
		win2.destroy()
	win2.protocol('WM_DELETE_WINDOW',on_close)

		
fileMenu = Menu(menu)
fileMenu.add_command(label="Report Bug",command = report)
fileMenu.add_command(label="Exit", command=exitProgram)
menu.add_cascade(label="File", menu=fileMenu)

def version():
	tkinter.messagebox.showinfo("Version",  "This is a beta version.\nIf you find any bugs or you have any suggestions\n please contact the developer.")

def help():
	tkinter.messagebox.showinfo("Help",  "1 - This program can ping the IP addresses that you set.\n\n2 - You can schedule this task so that you can test \nthe connection on the specified addresses.\n\n3 - The refresh results will be shown afterwards.\n\n4 - You can specify your own refresh rate!\n\n5 - If you want to know furthermore call the developer.")


aboutMenu = Menu(menu)
aboutMenu .add_command(label="Version",command = version)
aboutMenu .add_command(label="Help",command = help)
menu.add_cascade(label="About", menu=aboutMenu )
#####################################


############################
T = Text(fenetre,height=22, width=40)
T.pack()


E = Label(fenetre, text="IP addresses for Connection Test :", width=30, height=2, borderwidth=3, relief="solid",bg="#f7e4bb")
E_canvas = canvas1.create_window(190,40,  anchor = "nw", window = E)


E2 = Label(fenetre, text="Connection Test results :", width=30, height=2, borderwidth=3, relief="solid",bg="#f7e4bb")
E2_canvas = canvas1.create_window(705,40,  anchor = "nw", window = E2)


button1_canvas = canvas1.create_window( 130, 90, anchor = "nw", window = T)

############################
#Buttons
button2 = Button( fenetre, text = "Save modifications",command=save)
button2_canvas = canvas1.create_window( 270, 460, anchor = "nw", window = button2)
##############
f = open(r'IP_addresses\AdresseIP.txt','r')
data = f.read()
f.flush()
f.close()
T.insert(END,data)
############################
#Buttons
button3 = Button( fenetre, text = "Refresh", command=refresh)
button3_canvas = canvas1.create_window( 200, 460, anchor = "nw", window = button3)

temps= 'Last Refresh : Before opening the app'


labeltime = Label(fenetre,text = temps,bg="#e8ccff")
labeltime_canvas = canvas1.create_window(220,490,  anchor = "nw", window = labeltime)
##############
button4 = Button( fenetre, text = "Clear", command=clear1)
button4_canvas = canvas1.create_window( 140, 460, anchor = "nw", window = button4)




#__________[[[SECOND_WINDOW]]]_____________#
T2 = Text(fenetre,height=27, width=42,bg='black',fg='white')
T2.configure(font=('lucida console',10))
T2.see(END)
T2.pack()



text2_canvas = canvas1.create_window(630, 90, anchor = "nw", window = T2)

############################
#Buttons
button2_2 = Button( fenetre, text = "Save modifications",command=save2)
button2_2_canvas = canvas1.create_window( 770, 460, anchor = "nw", window = button2_2)
##############
f2 = open(r'Results\PingResults.txt','r')
data2 = f2.read()
f2.flush()
f2.close()
T2.insert(END,data2)
############################
#Buttons
button3_2 = Button( fenetre, text = "Refresh", command=refresh2)
button3_2_canvas = canvas1.create_window( 700, 460, anchor = "nw", window = button3_2)

button4_2 = Button( fenetre, text = "Clear", command=clear2)
button4_2_canvas = canvas1.create_window( 640, 460, anchor = "nw", window = button4_2)

button5 = Button( fenetre, text = "SetRefreshRate (Seconds)", command=rate)
button5_canvas = canvas1.create_window( 740, 500, anchor = "nw", window = button5)


def test(e):
		return 'break'

T3 = Text(fenetre,height=1, width=10,borderwidth=2)
T3.pack()
T3.bind('<Return>', test)

text3_canvas = canvas1.create_window(640, 500, anchor = "nw", window = T3)



refState = None
button6 = Button( fenetre, text = "StopAutoRefresh", command=stopRef)
button6_canvas = canvas1.create_window( 900, 500, anchor = "nw", window = button6)


#####___CHECKBOX___#########
def isChecked():
	global checkBoxClicked
	checkBoxClicked = cb.get()
	if (checkBoxClicked == False):
		tkinter.messagebox.showinfo("Notifications Parameter",  "Refresh Notifications will be hidden.")
	else:
		tkinter.messagebox.showinfo("Notifications Parameter",  "Refresh Notifications will be shown.")

cb = BooleanVar()
C1 = Checkbutton(fenetre, text = "Show refresh Notifications.", bg ="#4b86b4", variable = cb,  
	onvalue=True, offvalue=False, command=isChecked)
C1_canvas = canvas1.create_window( 640, 540, anchor = "nw", window = C1)

temps2= 'Last Refresh : Before opening the app'


labeltime2 = Label(fenetre,text = temps2,bg="#e8ccff")
labeltime_canvas2 = canvas1.create_window(826,542,  anchor = "nw", window = labeltime2)

################## TEST _ CNX _ BUTTON ###############
convertedTime = 0 #time en minutes to schedule the task comme une tache planifee
howManyTimes = 0 #How many times to execute the task (1 default)
scheduledSet = False # If scheduleSet, run with convertedTime and howManyTimes, else run normally once

stopThreadIsClicked = True
def stopThread():
	global stopThreadIsClicked
	global convertedTime
	if (stopThreadIsClicked):
		tkinter.messagebox.showerror("Stop Connection Test",  "No Connection Test running.")
	else:
		stopThreadIsClicked = True
		convertedTime = 0
		tkinter.messagebox.showinfo("Stop Connection Test",  "Connection Test Stopped.")
	

def threading(): 
    t1=Thread(target=ConnectionTest) 
    t1.daemon = True # this ensures the thread will die when the main thread dies.. can set t.daemon to False if you want it to keep running
    t1.start() 
    
    
lastExecuted = "Last Executed: No executions after opening the app this time."
labellast2 = Label(fenetre,text = lastExecuted ,bg="#8c9dbf")
labellast_canvas2 = canvas1.create_window(220,515,  anchor = "nw", window = labellast2)

clickedDay = "Every Day"
testIsRunning = False

nb = 0
def ConnectionTest():
	global nb
	global stopThreadIsClicked
	global scheduledSet
	global labellast2
	global clickedDay
	global testIsRunning
	testIsRunning = True
	
	daysDict = {"Every Day" : "*" , "Monday" : "1" , "Tuesday" : "2", "Wednesday" : "3", "Thursday" : "4" , "Friday" : "5" , "Saturday" : "6" , "Sunday" : "7"}
	if (daysDict.get(clickedDay)):
		print(clickedDay,' corresponds to ',daysDict.get(clickedDay))
	stopThreadIsClicked = False
	#For testing purpose
	print('convertedTime: ',convertedTime)
	print('howManyTimes: ',howManyTimes)
	print('stopThreadIsClicked ',stopThreadIsClicked)
	def job():
		global nb
		#global stopThreadIsClicked
		#p = subprocess.Popen('powershell.exe -ExecutionPolicy Bypass -file "powershell_script\PingComputerList.ps1"', stdout=sys.stdout)
		# Get the current script's directory
		script_directory = os.path.dirname(os.path.abspath("powershell_script\\PingComputerList.ps1"))

		# Split the PowerShell command and arguments into separate list elements
		command = 'powershell.exe'
		arguments = '-ExecutionPolicy', 'Bypass', '-File', 'powershell_script\\PingComputerList.ps1', script_directory

		# Run the PowerShell script with the working directory passed as an argument
		p = subprocess.Popen([command] + list(arguments), stdout=sys.stdout)
		p.communicate()
		nb=nb+1
		# Print the execution results - how many tests and at what time
		print('executed : ',nb, 'at : ',str(datetime.datetime.now().strftime('%A %d/%m/%Y %H:%M:%S')))	
		labellast2['text'] = 'Last executed : ' + str(nb) + 'at : ' + str(datetime.datetime.now().strftime('%A %d/%m/%Y %H:%M:%S'))
	job()
	if (scheduledSet == True) and not(howManyTimes == 1):
		print('convertedTime is',convertedTime)
		while True:
			if (stopThreadIsClicked == True) or (closedMainWindow == True):
				print('stopped')
				break
			if pycron.is_now('* * * * daysDict.get(clickedDay)'):   # True Every Min Every Sunday
				print('executing')
				time.sleep(5.5)               # The process should take at least 5.5 sec
		                                     # to avoid running twice in one minute (durée du pcus=> script pwshl)
		else:
			time.sleep(ConvertedTime)               # Check again in 15 seconds (run every ConvertedTime)
	elif (scheduledSet == False):
		tkinter.messagebox.showinfo("Connection Test State",  "No schedule found for connection test, that's why it will run once.\nIf you want to run a scheduled test, please make sure that you already specified it.")
	elif (howManyTimes == 1):
		tkinter.messagebox.showinfo("Connection Test State",  "Connection test done once.")
			

button7 = Button( fenetre, text = "Run Connection Test ! !", bg = "#2a4d69",fg="#ffffff", command=threading)
button7['font'] = font.Font(family='Helvetica', size=15, weight='bold')
button7_canvas = canvas1.create_window( 60, 540, anchor = "nw", window = button7)

button9 = Button( fenetre, text = "STOP Connection Test ! !", bg = "#bc113b",fg="#ffffff", command=stopThread)
button9['font'] = font.Font(family='Helvetica', size=10, weight='bold')
button9_canvas = canvas1.create_window( 330, 545, anchor = "nw", window = button9)	

###### CALENDAR ########
img =Image.open('images\calendar.png')
bg4 = ImageTk.PhotoImage(img)

### NEW WINDOW ###
info2 = ""



def create():
	global bg4
	global info2
	global scheduledSet
	
	global clickedDay
	global convertedTime
	global howManyTimes
	
	win = Toplevel(fenetre)
	win.title("Set Schedule Time")
	
	##
	win.config(bg='yellow')
	label47 = Label(win, image=bg4)
	label47.place(x = 0,y = 0)
	##

	win.resizable(0, 0)
	# get screen width and height
	ws = win.winfo_screenwidth()
	hs = win.winfo_screenheight()
	w=300
	h=350
	# calculate position x, y
	x = (ws/2) - (w/2)    
	y = (hs/2) - (h/2)
	win.geometry('%dx%d+%d+%d' % (w, h, x, y))
	
	
	win.grab_set()
	    
    	# Change the label text
	label1 = Label(win, text= "Set your own parameters to run\n the test at the scheduled time :",bg='#e0a899',fg='black')
	label1.pack()
	
	

	def show():
		global info2
		
		global convertedTime
		global howManyTimes
		global clickedDay
		global scheduledSet
		
		hoursValue = hours.get("1.0","end")	
		minutesValue = minutes.get("1.0","end")
		secondsValue = seconds.get("1.0","end")
		
		
		if (times.get("1.0","end").strip().isdigit()):
			timesValue = times.get("1.0","end")
		else:
			timesValue = "1"	
		
		howManyTimes = timesValue

		if (hours.get("1.0","end").strip().isdigit()) or (minutes.get("1.0","end").strip().isdigit()) or (seconds.get("1.0","end").strip().isdigit()) or (times.get("1.0","end").strip().isdigit()):
			convertedTime = int(hoursValue)*60+(int(minutesValue)*60)+int(secondsValue)
			def displayText(hours,minutes,seconds):
				chaine=''
				if not(hours == 0):
					chaine = ' every ' + hours.strip() + ' hour(s) '
				if not(minutes == 0):
					chaine += minutes.strip() + ' minute(s) '
					
					if (hours == 0):
						chaine += ' every ' + minutes.strip() + ' minute(s) '
				if not(seconds == 0):
					chaine += seconds.strip() + ' second(s) '
					if (hours == 0) and (minutes == 0):
						chaine += ' every ' + seconds.strip() + ' second(s) '
				return(chaine)
			info = str(timesValue).strip() + ' time(s) ' + clicked.get() + displayText(hoursValue, minutesValue, secondsValue)
			info2 = info
			answer = messagebox.askyesno('Confirm Schedule settings','Connection Test will be done '+ info +'\nConfirm settings?') 
			label.config(text = 'Settings :' + info)
			if (answer):
				scheduledSet = True
				win.destroy()
			info2 = info
			clickedDay = clicked.get()
			print('show : ',clickedDay)

		else:
			tkinter.messagebox.showerror("Wrong Schedule Parameters",  "An entry is wrong.\nPlease verify the parameters that you entered and try again.")
	options = [
		"Every Day",
		"Monday",
		"Tuesday",
		"Wednesday",
		"Thursday",
		"Friday",
		"Saturday",
		"Sunday"
	]
	# datatype of menu text
	clicked = StringVar()
  
	# initial menu text
	clicked.set("Every Day")
	
	# Create Dropdown menu
	drop = OptionMenu( win , clicked , *options )
	drop.pack()
	  
	
	label2 = Label(win, text= "Hours :",bg='#6497b1')
	label2.pack()


	hours = Text(win,height=1, width=5)
	hours.pack()
	hours.bind('<Return>', test) #Prevents returning to line (block 'enter' key)
	
	label3 = Label(win, text= "Minutes :",bg='#6497b1')
	label3.pack()

	minutes = Text(win,height=1, width=5)
	minutes.pack() 	
	minutes.bind('<Return>', test)
	
	label4 = Label(win, text= "Seconds :",bg='#6497b1')
	label4.pack()

	seconds = Text(win,height=1, width=5)
	seconds.pack() 
	seconds.bind('<Return>', test)
	
	label4 = Label(win, text= "How many times (1 by default) ? :",bg='#6497b1')
	label4.pack()

	times = Text(win,height=1, width=5)
	times.pack() 
	times.bind('<Return>', test)
	
	# Create button, it will change label text
	frame2 = Frame(win, width= 120, height= 20)
	frame2.place(x=100,y=240)
	button = Button( frame2 , text = "Save Parameters" , command = show,bg='#ebf4f6',fg='black' ).pack()
	
	
	# Create Label
	frame = Frame(win, width= 120, height= 20)
	frame.place(x=30,y=280)
	label = Label( frame , text = " " , wraplengt=250)
	label.pack()

	if (len(info2)>1):
		label.config(text = 'Settings :' + info2)
	else:
		label.config(text = 'No parameters set.')
	print('create : ',clickedDay)
	
	def on_close():
		win.grab_release()
		win.destroy()
	win.protocol('WM_DELETE_WINDOW',on_close)
	

	
####################


button8 = Button(fenetre, text="Specify Scheduling Time", command = create , bg='#e2e7c2',fg='black')
button8_canvas = canvas1.create_window( 60, 500, anchor = "nw", window = button8)
####
def saveIntoDataBase():
	num_lines = sum(1 for line in open(r'Results\PingResults.txt'))
	f=open(r'Results\PingResults.txt')
	lines=f.readlines()
	i=1
	date = ""
	while True:
		time = (lines[i])
		if ('--' in time):
			date = time
		else:
			if not(len(time) == 1):
				
				ipadd=time.split(":",2)[0].strip()
				stateip=time.split(":",2)[1].strip()
				c.execute("""INSERT INTO results (Time, IP, State) VALUES (?,?,?)""",(date,ipadd,stateip))
	
		conn.commit()
		i+=1
		if i == num_lines:
			break
	
	conn.close()
	f.flush()
	f.close()
with open(r"IP_addresses\config.txt", 'r') as fp:
	# read line 8
	StartupSaveIntoDb = fp.readlines()[1]
#StartupSaveIntoDb = False ## executes whenever you run the app if set to True
if (StartupSaveIntoDb.strip() == "True"):
	print('boucle passed')
	saveIntoDataBase() ## saves connection test result file into Results DB when app starts
	tkinter.messagebox.showinfo("On start Backup",  "All the data of connection tests have been saved into\nthe database 'testpython.db'. This was done because you enabled auto save whenever the app starts.")
########################"
img14 =Image.open('images\server_1200x627px.jpg')

bg14 = ImageTk.PhotoImage(img14)

backupWithDB = False
backupWithQuery = False		

def database():
	global backupWithDB
	global backupWithQuery 
	global C1
	global cb
	global cb2
	win = Toplevel(fenetre)
	win.title("Manage DataBase Settings")
	
	##
	win.config(bg='yellow')
	label47 = Label(win, image=bg14)
	label47.place(x = 0,y = 0)
	##

	win.resizable(0, 0)
	# get screen width and height
	ws = win.winfo_screenwidth()
	hs = win.winfo_screenheight()
	w=900
	h=600
	# calculate position x, y
	x = (ws/2) - (w/2)    
	y = (hs/2) - (h/2)
	win.geometry('%dx%d+%d+%d' % (w, h, x, y))
	
	
	win.grab_set()
	### Affichage de la base de données ###
	conn = sqlite3.connect(r'Database\testpython.db')
	c = conn.cursor()
	
	db_frame = Frame(win)
	db_frame.place(x=25,y=55)
	#scrollbar
	db_scroll = Scrollbar(db_frame)
	db_scroll.pack(side=RIGHT, fill=Y)
	
	db_scroll = Scrollbar(db_frame,orient='horizontal')
	db_scroll.pack(side= BOTTOM,fill=X)
	
	my_db = ttk.Treeview(db_frame,yscrollcommand=db_scroll.set, xscrollcommand =db_scroll.set)
	
	my_db.pack()
	db_scroll.config(command=my_db.yview)
	db_scroll.config(command=my_db.xview)
	
	#define our column
	my_db['columns'] = ('Time', 'IP', 'State')
	
	# format our column
	my_db.column("#0", width=0,  stretch=NO)
	my_db.column("Time",anchor=CENTER, width=80)
	my_db.column("IP",anchor=CENTER,width=80)
	my_db.column("State",anchor=CENTER,width=80)
	
	#Create Headings 
	my_db.heading("#0",text="",anchor=CENTER)
	my_db.heading("Time",text="Date & Time",anchor=CENTER)
	my_db.heading("IP",text="Destination IP",anchor=CENTER)
	my_db.heading("State",text="State",anchor=CENTER)
	
	r_set=c.execute('''SELECT * from results LIMIT 0,20''')
	
	i=0 # row value inside the loop 
	t={}
	for result in r_set: 
		t[i] = my_db.insert('',i,text='',values=(result[0],result[1],result[2]))
		i = i+1
		
	labelview =  Label(win, text= "A brief view of the first few lines from the database table : ",bg='#9ec1e2',fg='black').place(x=15,y=15)
	my_db.pack()
	
	
	
    	# Change the label text
	label1 = Label(win, text= "Parametrize your own database settings with\n these buttons :",bg='#e0a899',fg='black').place(x=35,y=315)
	
	def backup():
		global backupWithDB
		global backupWithQuery 
		win2 = Toplevel(win)
		win2.title("Manage Backups")
		
		##
		win2.config(bg='yellow')
		label47 = Label(win2, image=bg14)
		label47.place(x = 0,y = 0)
		##
	
		win2.resizable(0, 0)
		# get screen width and height
		ws = win2.winfo_screenwidth()
		hs = win2.winfo_screenheight()
		w=420
		h=320
		# calculate position x, y
		x = (ws/2) - (w/2)    
		y = (hs/2) - (h/2)
		win2.geometry('%dx%d+%d+%d' % (w, h, x, y))
		win2.grab_set()
		labeltimeBD = Label(win2,text = 'Last backup : Loading' ,bg="#ede3ff")
		labeltimeBD.place(x=30, y= 240)
		labeltimeBD2 = Label(win2,text = 'Last backup : Loading' ,bg="#ede3ff")
		labeltimeBD2.place(x=30, y= 280)

		try:
			labeltimeBD.config(text ="Last backup into database: %s" % time.ctime(os.path.getmtime(r'Database\backup.db')))
			labeltimeBD2.config(text ="Last backup into SQL query: %s" % time.ctime(os.path.getmtime(r'Database\backupdatabase_dump.sql')))
		except Exception as e:
			labeltimeBD.config(text ="Last backup into database: an error occured, database backup file might not exist")
			labeltimeBD.config(text ="Last backup into SQL query: an error occured, SQL query backup file might not exist")

				
						
		def backupDB():
			global backupWithDB

			backupWithDB = True
			conn=sqlite3.connect(r'Database\testpython.db')
			conn_backup = sqlite3.connect(r'Database\backup.db')
			conn.backup(conn_backup )
			conn.close()
			tkinter.messagebox.showinfo("Backup State",  "Backup done into another DataBase\n called 'backup.db' in same folder.")

			
		def backupQuery():
			global backupWithQuery 			

			backupWithQuery = True
			conn=sqlite3.connect(r'Database\testpython.db')
			##backup
			# Open() function 
			with io.open(r'Database\backupdatabase_dump.sql', 'w') as p:   
				# iterdump() function
				for line in conn.iterdump(): 
					p.write('%s\n' % line)
			tkinter.messagebox.showinfo("Backup State",  "Backup done into an SQL query\n called 'backupdatabase_dump.sql' in same folder.")

		label1 = Label(win2, text= "Choose the type of Backup that you want:",bg='#90b3d5',fg='black')
		label1.place(x=20,y=30)
		label2 = Label(win2, text= "1- Backup the database in another database (same type as SQLite).",bg='#e0a899',fg='black')
		label2.place(x=60,y=80)
		label3 = Label(win2, text= "2- Backup the database in an SQL query with which you\n can reconstruct it (it can be run in SQL server too).",bg='#e0a899',fg='black')
		label3.place(x=60,y=120)
		button1 = Button(win2, text = "Backup into another DB", command = backupDB, bg = '#ffeae8',fg='black')
		button1.place(x=30, y=180)
		button2 = Button(win2, text = "Backup into SQL Query", command = backupQuery, bg = '#ffeae8',fg='black')
		button2.place(x=250, y=180)
		def on_close():
			win2.grab_release()
			win2.destroy()
		win2.protocol('WM_DELETE_WINDOW',on_close)

	win.grab_set()
			
	def restore():
		global backupWithDB
		global backupWithQuery 
		win2 = Toplevel(win)
		win2.title("Manage Restores")
		
		#win['bg']='black'
		##
		win2.config(bg='yellow')
		label47 = Label(win2, image=bg14)
		label47.place(x = 0,y = 0)
		##
	
		win2.resizable(0, 0)
		# get screen width and height
		ws = win2.winfo_screenwidth()
		hs = win2.winfo_screenheight()
		w=420
		h=320
		# calculate position x, y
		x = (ws/2) - (w/2)    
		y = (hs/2) - (h/2)
		win2.geometry('%dx%d+%d+%d' % (w, h, x, y))
		win2.grab_set()
		
		def replace_line(file_name, line_num, text):
			lines = open(file_name, 'r').readlines()
			lines[line_num] = text
			out = open(file_name, 'w')
			out.writelines(lines)
			out.close()

		
		
				
		labeltimeRestore = Label(win2,text = 'Last Restore : Loading' ,bg="#ede3ff")
		labeltimeRestore.place(x=30, y= 240)
		
		
		def restoreHistoryClean():
			try:
				with open('Database\\restore.txt','w') as file:
					pass
				with open('Database\\restore.txt', "a") as file_object:
					# Append 'hello' at the end of file
					file_object.write("None\n")
				tkinter.messagebox.showinfo("Restore History",  "Restore History Cleared.")
			except Exception as e:
				tkinter.messagebox.showerror("Restore History",  "Error. Couldn't clear Restore History.\nPlease verify your settings.")


		restoreHistoryClear = Button(win2, text="Clear Restore History",command= restoreHistoryClean, bg="#ede3ff",fg="black")
		restoreHistoryClear.place(x=150, y= 280)
		
		
		#Find the Last Line of a Large File in Python
		with open('Database\\restore.txt', "rb") as file:
			try:
				file.seek(-2, os.SEEK_END)
				while file.read(1) != b'\n':
					file.seek(-2, os.SEEK_CUR)
			except OSError:
				file.seek(0)
			last_line = file.readline().decode() #The last line of restore.txt file
		labeltimeRestore.config(text ="Last Restore : "+last_line.replace("\n", ""))
		
		
		####If the file contains a vast number of lines (like file size in GB), you should use the generator for speed.
		####Getting how many lines in restore.txt file
		#def _count_generator(reader):
			#b = reader(1024 * 1024)
			#while b:
				#yield b
				#b = reader(1024 * 1024)
	
		#with open('restore.txt', 'rb') as fp:
			#c_generator = _count_generator(fp.raw.read)
			# count each \n
			#count = sum(buffer.count(b'\n') for buffer in c_generator)
			#print('Total lines:', count + 1)
		#####
		
		def restoreDB():
			global backupWithDB
			if (os.path.exists(r'Database\backup.db') == True):
				conn_backup = sqlite3.connect(r'Database\testpython.db')
				c= conn_backup.cursor()
				c.execute('DELETE FROM results;',)
				
				conn_backup.commit()
				c.execute("""ATTACH DATABASE ? AS backup""",('Database\\backup.db',))
				c.execute("""ATTACH DATABASE ? AS testpython""",('Database\\testpython.db',))
				c.execute("""INSERT INTO testpython.results SELECT * FROM backup.results""")
				conn_backup.commit()
				conn_backup.close()
				tkinter.messagebox.showinfo("Restore State",  "Restore done.")
				with open('Database\\restore.txt', "a") as file_object:
					# Append 'hello' at the end of file
					file_object.write("\n"+str(datetime.datetime.now().strftime('%A %d/%m/%Y %H:%M:%S')))
				labeltimeRestore.config(text ="Last Restore : "+ str(datetime.datetime.now().strftime('%A %d/%m/%Y %H:%M:%S')))
			else:
				tkinter.messagebox.showerror("Restore Error",  "Backup file does not exist.")


			
		def restoreQuery():
			global backupWithQuery 			
			if (os.path.exists(r'Database\backupdatabase_dump.sql') == True): #if the file exists
				conn=sqlite3.connect(r'Database\testpython.db')
				##restore
				f=open(r'Database\backupdatabase_dump.sql')
				qry=f.read( )
				f.close ( )
				cur=conn.cursor ( )
				cur.execute('DELETE FROM results;',)
				cur.execute('DROP TABLE results')
				conn.commit()
				cur.executescript(qry)
				conn.close ( )
			
				tkinter.messagebox.showinfo("Restore State",  "Restore done with an SQL query")
				with open('Database\\restore.txt', "a") as file_object:
					# Append 'hello' at the end of file
					file_object.write("\n"+str(datetime.datetime.now().strftime('%A %d/%m/%Y %H:%M:%S')))
				labeltimeRestore.config(text ="Last Restore : "+ str(datetime.datetime.now().strftime('%A %d/%m/%Y %H:%M:%S')))

			else:
				tkinter.messagebox.showerror("Restore Error",  "SQL query does not exist.")
		label1 = Label(win2, text= "Choose the type of Restore that you want:",bg='#90b3d5',fg='black')
		label1.place(x=20,y=30)
		label2 = Label(win2, text= "1- Restore from another database (same type as SQLite).",bg='#e0a899',fg='black')
		label2.place(x=60,y=80)
		label3 = Label(win2, text= "2- Restore from an SQL query (it can be run in SQL server too).",bg='#e0a899',fg='black')
		label3.place(x=60,y=120)
		button1 = Button(win2, text = "Restore from another DB", command = restoreDB, bg = '#ffeae8',fg='black')
		button1.place(x=30, y=180)
		button2 = Button(win2, text = "Restore from SQL Query", command = restoreQuery, bg = '#ffeae8',fg='black')
		button2.place(x=250, y=180)
		def on_close():
			win2.grab_release()
			win2.destroy()
		win2.protocol('WM_DELETE_WINDOW',on_close)
	def refresh():
		### Affichage de la base de données ###
		conn = sqlite3.connect(r'Database\\testpython.db')
		c = conn.cursor()
		
		db_frame = Frame(win)
		db_frame.place(x=25,y=55)
		#scrollbar
		db_scroll = Scrollbar(db_frame)
		db_scroll.pack(side=RIGHT, fill=Y)
		
		db_scroll = Scrollbar(db_frame,orient='horizontal')
		db_scroll.pack(side= BOTTOM,fill=X)
		
		my_db = ttk.Treeview(db_frame,yscrollcommand=db_scroll.set, xscrollcommand =db_scroll.set)
		
		my_db.pack()
		db_scroll.config(command=my_db.yview)
		db_scroll.config(command=my_db.xview)
		
		#define our column
		my_db['columns'] = ('Time', 'IP', 'State')
		
		# format our column
		my_db.column("#0", width=0,  stretch=NO)
		my_db.column("Time",anchor=CENTER, width=80)
		my_db.column("IP",anchor=CENTER,width=80)
		my_db.column("State",anchor=CENTER,width=80)
		
		#Create Headings 
		my_db.heading("#0",text="",anchor=CENTER)
		my_db.heading("Time",text="Date & Time",anchor=CENTER)
		my_db.heading("IP",text="Destination IP",anchor=CENTER)
		my_db.heading("State",text="State",anchor=CENTER)
		
		r_set=c.execute('''SELECT * from results LIMIT 0,20''')
		
		i=0 # row value inside the loop 
		t={}
		for result in r_set: 
			
			t[i] = my_db.insert('',i,text='',values=(result[0],result[1],result[2]))
			i = i+1
			
		labelview =  Label(win, text= "A brief view of the first few lines from the database table : ",bg='#9ec1e2',fg='black').place(x=15,y=15)
		my_db.pack()

	def delete():
		conn = sqlite3.connect(r'Database\backup.db')
		c = conn.cursor()
		c.execute('DELETE FROM results;',);
		tkinter.messagebox.showinfo("Delete State",  'We have deleted'+ str(c.rowcount) + 'records from the table.')
		#commit the changes to db			
		conn.commit()

	def replace_line(file_name, line_num, text):
		lines = open(file_name, 'r').readlines()
		lines[line_num] = text
		out = open(file_name, 'w')
		out.writelines(lines)
		out.close()


	def isChecked():
		global C1
		global cb
		print(cb.get())
		print(type(cb.get()))
		if (cb.get() == True):
			replace_line(r"IP_addresses\config.txt",1,"True\n")
		else:
			replace_line(r"IP_addresses\config.txt",1,"False\n")
	def isChecked2():
		global cb2
		if (cb2.get() == True):
			replace_line(r"IP_addresses\config.txt",3,"True\n")
		else:
			replace_line(r"IP_addresses\config.txt",3,"False\n")

	button1 = Button(win, text = "Backup", command = backup, bg = '#e2e7ff',fg='black')
	button1.place(x=20,y=360)
	button2 = Button(win, text = "Restore", command = restore, bg = '#e2e7ff',fg='black')
	button2.place(x=80,y=360)
	button3 = Button(win, text = "Refresh", command = refresh, bg = '#e2e7ff',fg='black')
	button3.place(x=140,y=360)
	button4 = Button(win, text = "Delete Database", command = delete, bg = '#e2e7ff',fg='black')
	button4.place(x=200,y=360)
	
	
	cb = BooleanVar()
	C1 = Checkbutton(win, text = "Enable auto save in database on app opening.", bg ="#83b8ea", variable = cb,  
		onvalue=True, offvalue=False, command=isChecked)
	C1.place(x=20,y=400)
	with open(r"IP_addresses\config.txt", 'r') as fp:
		# read line 1
		AutoSaveState = fp.readlines()[1]
		print(AutoSaveState)
		print(type(AutoSaveState))
	if (AutoSaveState.strip() == "True"):
		C1.select()
	if (AutoSaveState.strip() == "False"):
		C1.deselect()

	cb2 = BooleanVar()
	C2 = Checkbutton(win, text = "Enable email notification on each action.", bg ="#bedfff", variable = cb2,  
		onvalue=True, offvalue=False, command=isChecked2)
	C2.place(x=20,y=440)
	with open(r"IP_addresses\config.txt", 'r') as fp:
		# read line 3
		AutoMailState= fp.readlines()[3]
		print(AutoMailState)
		print(type(AutoMailState))
	if (AutoMailState.strip() == "True"):
		C2.select()
	if (AutoMailState.strip() == "False"):
		C2.deselect()
	
	
	labelinfo = Label(win, text ="Top 4 Database Security Best Practices",font=('Arial', 14), bg ="#bedfff", fg='black').place(x=480,y=30)
	labelinfo2 = Label(win, text ="1. Ensure that the physical databases are secure",font=('Arial', 10), bg ="#e2bdba", fg='black').place(x=480,y=80)
	labelinfo3 = Label(win, text ="2. Separate database servers",font=('Arial', 10), bg ="#e2bdba", fg='black').place(x=480,y=130)
	labelinfo4 = Label(win, text ="3. Install a proxy server that provides HTTPS access",font=('Arial', 10), bg ="#e2bdba", fg='black').place(x=480,y=180)
	labelinfo5 = Label(win, text ="4. Implement an encryption protocol",font=('Arial', 10), bg ="#e2bdba", fg='black').place(x=480,y=230)
	labelinfo6 = Label(win, text ="You can change this if you want !",font=('Arial', 8), bg ="#99b9c5", fg='black').place(x=510,y=290)
	labelinfo7 = Label(win, text ="""!! - We recommend you to use other DB management tools if you
	really want to administrate your database.
	For this version we are using SQLite database. 
	You can either use SQLite DB management tool (opensource)
	Or you can backup your database into a query then run it in 
	SQL server (Management Studio - SSMS) to work on it - !!""",font=('Calibri', 9), bg ="#fa9e98", fg='black').place(x=480,y=410)

	conn.close()
	def on_close():
		win.grab_release()
		win.destroy()
	win.protocol('WM_DELETE_WINDOW',on_close)

button16 = Button(fenetre, text="Manage Database", command = database , bg='#aebcea',fg='black')
button16_canvas = canvas1.create_window( 890, 460, anchor = "nw", window = button16)


############"""
closedMainWindow = False
def on_close():
    global closedMainWindow
    response=messagebox.askyesno('Exit','Are you sure you want to exit?')
    if response:
        closedMainWindow = True
        fenetre.destroy()
fenetre.protocol('WM_DELETE_WINDOW',on_close)

fenetre.mainloop()


