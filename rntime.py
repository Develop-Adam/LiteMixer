#Libraries
import os
import time
from pyModbusTCP.client import ModbusClient
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

#Modules
import registers as r
import user_input as i

#Initiate modbus communications with machine
c = ModbusClient(host='10.10.1.2', port=503, auto_open=True, debug=False)

def setpoints():
    x = 0
    s = 0
    colorama_init()
    print(f'Setpoints:\t {Fore.YELLOW}[Loading]{Style.RESET_ALL}')
    while x < 10:
        s_register = int(r.register_speed[s])
        t_register = int(r.register_time[s])
        v_register = int(r.register_vacuum[s])
        s_value = int(i.stage_speed[s])
        t_value = int(i.stage_time[s])
        v_value = int(i.stage_vacuum[s])
        x = x + 1
        s = s + 1
        c.write_single_register(s_register,s_value)
        c.write_single_register(t_register,t_value)
        c.write_single_register(v_register,v_value)

      
def write():
    c.write_single_register(3056, 0)    #Select program to write to
    c.write_single_register(3053, 1)    #Send load command
    c.write_single_register(3053, 0)    #Reset load command
    colorama_init()
    print(f'Write:\t\t {Fore.CYAN}[Completed]{Style.RESET_ALL}')
    
def options():
	c.write_single_register(r.vacuum_state,i.vacuum_state)      #Vacuum: 0=Off, 1=On
	c.write_single_register(r.vent_gas,i.vent_gas)              #Vent Gass: 0=Air, 1=Nitrogen/Other
	c.write_single_register(r.vacuum_monitor,i.vacuum_monitor)  #Monitor Type: 0=Off, 1=Alarm, 2=Alarm & Stop
	c.write_single_register(r.pressure_unit,i.pressure_unit)    #1=Torr, 2=mBar, 3=inHg, 4=PSIA
	c.write_single_register(r.acceleration,i.acceleration)      #Max Acceleration
	c.write_single_register(r.deceleration,i.deceleration)      #Mac Deceleration
	colorama_init()

	print(f'\nProgram Options: {Fore.YELLOW}[Loading]{Style.RESET_ALL}\n----------------------------------------------------')
	print('Vacuum State:\t',r.vacuum_state,i.vacuum_state)
	print('Venting Gas:\t',r.vent_gas,i.vent_gas)
	print('Vacuum Monitor:\t',r.vacuum_monitor,i.vacuum_monitor)
	print('Pressure Unit:\t',r.pressure_unit,i.pressure_unit)
	print('Acceleration:\t',r.acceleration,i.acceleration)
	print('Deceleration:\t',r.deceleration,i.deceleration)
	print(f'----------------------------------------------------\nProgram Options: {Fore.GREEN}[Loaded]{Style.RESET_ALL}\n')
    
def run_mix():
    c.write_single_register(3053, 100)  #Run program
    
def keep_alive():
    status = 99
    while status == 99:
        print(c.read_holding_registers(3100))
        os.system('cls')
        
def start_mix():
    run_mix()
    keep_alive()

def system_ready():
	print('\n------------------SYSTEM READY! STARTING CYCLE------------------')
	options()
	write()
	setpoints()
	write()
#	start_mix()
#	write()


