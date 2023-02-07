#Options
vacuum_state    =   1   #Vacuum: 0=Off, 1=On
vent_gas        =   0   #Vent Gass: 0=Air, 1=Nitrogen/Other
vacuum_monitor  =   0   #Monitor Type: 0=Off, 1=Alarm, 2=Alarm & Stop
pressure_unit   =   2   #1=Torr, 2=mBar, 3=inHg, 4=PSIA
acceleration    =   500
deceleration    =   500
stage_speed, stage_time, stage_vacuum = [],[],[]


def read():
	global buff_speed, buff_time, buff_vacuum
	f = open("output.txt", "r")
	content =  f.readlines()
	buff_speed     =   content[0]
	buff_time      =   content[1]
	buff_vacuum    =   content[2]

	print('\nReading from file:\n------------------------------------------------------------')
	print('Speed:\t', buff_speed + 'Time:\t', buff_time + 'Vacuum:\t',buff_vacuum)
	f.close()
	return buff_speed, buff_time, buff_vacuum, spliting()

def spliting():
	global stage_time, stage_speed, stage_vacuum
	stage_speed = buff_speed.split(',')
	stage_time = buff_time.split(',')
	stage_vacuum = buff_vacuum.split(',')
	return stage_time, stage_speed, stage_vacuum
