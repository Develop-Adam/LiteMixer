from tkinter import *
from tkinter import ttk
import user_input as i
import rntime as r
import os
import time
#import colorama
#from colorama import Fore

#prog_name = []

#Build Info-------------------------------------------------------------
name = 'Light Mixer'
vrs = '0.0.0'
sys_ready = False

#ACTIONS----------------------------------------------------------------
def run():
	global speeds, times, vacuums, sys_ready
#	prog_name = [prog_name1.get(), prog_name2.get(), prog_name3.get(), prog_name4.get(), prog_name5.get(), prog_name6.get(), prog_name7.get(), prog_name8.get(), prog_name9.get(), prog_name10.get()] 
	speeds = [speed1.get(), speed2.get(), speed3.get(), speed4.get(), speed5.get(), speed6.get(), speed7.get(), speed8.get(), speed9.get(), speed10.get()]
	times = [time1.get(), time2.get(), time3.get(), time4.get(), time5.get(), time6.get(), time7.get(), time8.get(), time9.get(), time10.get()]
	vacuums = [vacuum1.get(), vacuum2.get(), vacuum3.get(), vacuum4.get(), vacuum5.get(), vacuum6.get(), vacuum7.get(), vacuum8.get(), vacuum9.get(), vacuum10.get()]
	sys_ready = True
	print('Writing to file:\n------------------------------------------------------------')
	print(speeds)
	print(times)
	print(vacuums)
	return speeds, times, vacuums, writef()

def writef():
	f = open("data.txt", "w")
	f.writelines(str(speeds)+'\n')
	f.writelines(str(times)+'\n')
	f.writelines(str(vacuums))
	f.close()
	return clean()

def clean():
	with open('data.txt', 'r') as f, open('output.txt', 'w') as fo:
		for line in f:
			fo.write(line.replace('"', '').replace("'", "").replace("[", "").replace("]", ""))
	return i.read(), r.system_ready()
	
#Window Configuration---------------------------------------------------
root = Tk()
root.title(name)
#root.wm_attributes('-toolwindow', 'True')
root.iconbitmap(r'Swirl.ico')

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
	
#LABELS-----------------------------------------------------------------
#Stage Labels
ttk.Label(mainframe, text="Stage 1").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="Stage 2").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Stage 3").grid(column=4, row=1, sticky=W)
ttk.Label(mainframe, text="Stage 4").grid(column=5, row=1, sticky=W)
ttk.Label(mainframe, text="Stage 5").grid(column=6, row=1, sticky=W)

ttk.Label(mainframe, text="Stage 6").grid(column=7, row=1, sticky=W)
ttk.Label(mainframe, text="Stage 7").grid(column=8, row=1, sticky=W)
ttk.Label(mainframe, text="Stage 8").grid(column=9, row=1, sticky=W)
ttk.Label(mainframe, text="Stage 9").grid(column=10, row=1, sticky=W)
ttk.Label(mainframe, text="Stage 10").grid(column=11, row=1, sticky=W)

#Speed, Time, Vacuum Labels
ttk.Label(mainframe, text="Speed").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Time").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="Vacuum").grid(column=1, row=4, sticky=W)

#INPUT SPEED------------------------------------------------------------
#Speed One
speed1 = StringVar()
speed1_entry = ttk.Entry(mainframe, width=7, textvariable=speed1)
speed1_entry.grid(column=2, row=2, sticky=(W, E))

#Speed Two
speed2 = StringVar()
speed2_entry = ttk.Entry(mainframe, width=7, textvariable=speed2)
speed2_entry.grid(column=3, row=2, sticky=(W, E))

#Speed Three
speed3 = StringVar()
speed3_entry = ttk.Entry(mainframe, width=7, textvariable=speed3)
speed3_entry.grid(column=4, row=2, sticky=(W, E))

#Speed Four
speed4 = StringVar()
speed4_entry = ttk.Entry(mainframe, width=7, textvariable=speed4)
speed4_entry.grid(column=5, row=2, sticky=(W, E))

#Speed Five
speed5 = StringVar()
speed5_entry = ttk.Entry(mainframe, width=7, textvariable=speed5)
speed5_entry.grid(column=6, row=2, sticky=(W, E))

#Speed Six
speed6 = StringVar()
speed6_entry = ttk.Entry(mainframe, width=7, textvariable=speed6)
speed6_entry.grid(column=7, row=2, sticky=(W, E))

#Speed Seven
speed7 = StringVar()
speed7_entry = ttk.Entry(mainframe, width=7, textvariable=speed7)
speed7_entry.grid(column=8, row=2, sticky=(W, E))

#Speed Eight
speed8 = StringVar()
speed8_entry = ttk.Entry(mainframe, width=7, textvariable=speed8)
speed8_entry.grid(column=9, row=2, sticky=(W, E))

#Speed Nine
speed9 = StringVar()
speed9_entry = ttk.Entry(mainframe, width=7, textvariable=speed9)
speed9_entry.grid(column=10, row=2, sticky=(W, E))

#Speed Ten
speed10 = StringVar()
speed10_entry = ttk.Entry(mainframe, width=7, textvariable=speed10)
speed10_entry.grid(column=11, row=2, sticky=(W, E))

#INPUT TIME-------------------------------------------------------------
#Time One
time1 = StringVar()
time1_entry = ttk.Entry(mainframe, width=7, textvariable=time1)
time1_entry.grid(column=2, row=3, sticky=(W, E))

#Time Two
time2 = StringVar()
time2_entry = ttk.Entry(mainframe, width=7, textvariable=time2)
time2_entry.grid(column=3, row=3, sticky=(W, E))

#Time Three
time3 = StringVar()
time3_entry = ttk.Entry(mainframe, width=7, textvariable=time3)
time3_entry.grid(column=4, row=3, sticky=(W, E))

#Time Four
time4 = StringVar()
time4_entry = ttk.Entry(mainframe, width=7, textvariable=time4)
time4_entry.grid(column=5, row=3, sticky=(W, E))

#Time Five
time5 = StringVar()
time5_entry = ttk.Entry(mainframe, width=7, textvariable=time5)
time5_entry.grid(column=6, row=3, sticky=(W, E))

#Time Six
time6 = StringVar()
time6_entry = ttk.Entry(mainframe, width=7, textvariable=time6)
time6_entry.grid(column=7, row=3, sticky=(W, E))

#Time Seven
time7 = StringVar()
time7_entry = ttk.Entry(mainframe, width=7, textvariable=time7)
time7_entry.grid(column=8, row=3, sticky=(W, E))

#Time Eight
time8 = StringVar()
time8_entry = ttk.Entry(mainframe, width=7, textvariable=time8)
time8_entry.grid(column=9, row=3, sticky=(W, E))

#Time Nine
time9 = StringVar()
time9_entry = ttk.Entry(mainframe, width=7, textvariable=time9)
time9_entry.grid(column=10, row=3, sticky=(W, E))

#Time Ten
time10 = StringVar()
time10_entry = ttk.Entry(mainframe, width=7, textvariable=time10)
time10_entry.grid(column=11, row=3, sticky=(W, E))

#INPUT VACUUM-----------------------------------------------------------
#Vacuum Inputs
vacuum1 = StringVar()
vacuum1_entry = ttk.Entry(mainframe, width=7, textvariable=vacuum1)
vacuum1_entry.grid(column=2, row=4, sticky=(W, E))

vacuum2 = StringVar()
vacuum2_entry = ttk.Entry(mainframe, width=7, textvariable=vacuum2)
vacuum2_entry.grid(column=3, row=4, sticky=(W, E))

vacuum3 = StringVar()
vacuum3_entry = ttk.Entry(mainframe, width=7, textvariable=vacuum3)
vacuum3_entry.grid(column=4, row=4, sticky=(W, E))

vacuum4 = StringVar()
vacuum4_entry = ttk.Entry(mainframe, width=7, textvariable=vacuum4)
vacuum4_entry.grid(column=5, row=4, sticky=(W, E))

vacuum5 = StringVar()
vacuum5_entry = ttk.Entry(mainframe, width=7, textvariable=vacuum5)
vacuum5_entry.grid(column=6, row=4, sticky=(W, E))

vacuum6 = StringVar()
vacuum6_entry = ttk.Entry(mainframe, width=7, textvariable=vacuum6)
vacuum6_entry.grid(column=7, row=4, sticky=(W, E))

vacuum7 = StringVar()
vacuum7_entry = ttk.Entry(mainframe, width=7, textvariable=vacuum7)
vacuum7_entry.grid(column=8, row=4, sticky=(W, E))

vacuum8 = StringVar()
vacuum8_entry = ttk.Entry(mainframe, width=7, textvariable=vacuum8)
vacuum8_entry.grid(column=9, row=4, sticky=(W, E))

vacuum9 = StringVar()
vacuum9_entry = ttk.Entry(mainframe, width=7, textvariable=vacuum9)
vacuum9_entry.grid(column=10, row=4, sticky=(W, E))

vacuum10 = StringVar()
vacuum10_entry = ttk.Entry(mainframe, width=7, textvariable=vacuum10)
vacuum10_entry.grid(column=11, row=4, sticky=(W, E))

#BUTTONS----------------------------------------------------------------
#Start Button
ttk.Button(mainframe, text="Send", command=run).grid(column=12, row=4, sticky=W)

for child in mainframe.winfo_children(): 
	child.grid_configure(padx=5, pady=5)

#root.bind("<Return>", gui_run)
root.mainloop()
