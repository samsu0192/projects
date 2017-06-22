#!/usr/bin/python
from pymodbus.client.sync import ModbusSerialClient
import time

modport='/dev/serial/by-id/usb-ATC_High_Speed_USB_To_RS-485_DAMWDJL-if00-port0'
sam=ModbusSerialClient(method='rtu',port=modport,baudrate=9600)
counter1=counter3=counter5=0
status1=status3=status5=False
time.sleep(0.05)
led=sam.read_coils(0,count=8,unit=1)
time.sleep(4)
sam.socket.timeout=.1

while(1):
   led=sam.read_coils(0,count=8,unit=1)
   time.sleep(0.05)
   if led.bits[1]==True:
      if led.bits[1]!=status1:
         counter1+=1
         print("LED1 is on, total: led1 %d, led3 %d,led5 %d" %(counter1,counter3,counter5))
   if led.bits[3]==True:
      if led.bits[3]!=status3:
         counter3+=1
         print("LED3 is on, total: led1 %d, led3 %d,led5 %d" %(counter1,counter3,counter5))
   if led.bits[5]==True:
      if led.bits[5]!=status5:
         counter5+=1
         print("LED5 is on, total: led1 %d, led3 %d,led5 %d" %(counter1,counter3,counter5))
   status1=led.bits[1]
   status3=led.bits[3]
   status5=led.bits[5]
