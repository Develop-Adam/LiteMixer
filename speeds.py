#Registers
register_speed = []
register_time = []
register_vacuum = []

#User Input
prog_name = []
stage_speed = []
stage_time = []
stage_vacuum = []

#Generate Speed Registers
x = 3012
while x < 3022:
       x = x + 1
       register_speed.append(x)

#Generate Time Registers
x = 3022
while x < 3032:
       x = x + 1
       register_time.append(x)

#Generate Vacuum Registers
x = 3032
while x < 3042:
       x = x + 1
       register_vacuum.append(x)

s0, s1, s2, s3, s4, s5, s6, s7, s8 ,s9 = register_speed
t0, t1, t2, t3, t4, t5, t6, t7, t8, t9 = register_time
v0, v1, v2, v3, v4, v5, v6, v7, v8, v9 = register_vacuum