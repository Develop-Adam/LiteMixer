import os
import time
from pyModbusTCP.client import ModbusClient
import main as m

c = ModbusClient(host='10.10.1.2', port=503, auto_open=True, debug=False)

def check_status():

    #Variables
    x = 0
    l = 0
    n = 0
    l = c.read_holding_registers(3100)  #pull status from MI 3100
    m = l[0]                            #pull status from string
    n = format(m, "08b")

    #flipped bit order
    bit0 = 'Ready to Run:\t' + n[7]
    bit1 = 'Mixer Running:\t' + n[6]
    bit2 = 'Mixer Error:\t' + n[5]
    bit3 = 'Lid Open:\t' + n[4]
    bit4 = 'Lid Closed:\t' + n[3]
    bit5 = 'Safety OK:\t' + n[2]
    bit6 = 'Connected:\t' + n[1]
    bit7 = 'Robot at Home:\t' + n[0]

    return bit0 ,bit1, bit2, bit3, bit4, bit5, bit6, bit7
check_status()