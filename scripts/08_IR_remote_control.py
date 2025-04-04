# -*- coding:utf-8 -*-
from machine import Pin
from ir_api import IR
import time


PIN = 22;
irm = IR(PIN)
print('IR Test Start ...')
while True:
    IR_re = irm.scan()
    print(IR_re)
    if(IR_re[0]==True and IR_re[1]!=None):
        print("Command: %s" %IR_re[1])
        time.sleep(0.02)
    else:
        pass
    
    time.sleep(0.1)
