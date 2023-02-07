#Registers
register_speed  = []
register_time   = []
register_vacuum = []

#Generate Registers
x = [3013, 3023, 3033]
y = 0
while y < 10:
    register_speed.append(x[0])
    register_time.append(x[1])
    register_vacuum.append(x[2])
    y = y + 1
    x[0] = x[0] + 1
    x[1] = x[1] + 1
    x[2] = x[2] + 1
     
vacuum_state   = 3046    #Vacuum: 0=Off, 1=On
vent_gas       = 3048    #Vent Gass: 0=Air, 1=Nitrogen/Other
vacuum_monitor = 3049    #Monitor Type: 0=Off, 1=Alarm, 2=Alarm & Stop
pressure_unit  = 3050    #1=Torr, 2=mBar, 3=inHg, 4=PSIA
acceleration   = 3043    #Max Acceleration
deceleration   = 3044    #Mac Deceleration