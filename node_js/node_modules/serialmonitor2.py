#!/usr/bin/python
from pymodbus.client.sync import ModbusSerialClient
import time

#port parameter settings
totalport=8
monitor_port=[1,3,5]
modport='/dev/serial/by-id/usb-ATC_High_Speed_USB_To_RS-485_DAMWDJL-if00-port0'
sam=ModbusSerialClient(method='rtu',port=modport,baudrate=9600)
time.sleep(0.05)
sam.read_coils(0,count=8,unit=1)
time.sleep(4)
sam.socket.timeout=.1
print('test can begin')

class DI():
    status=[]
    counter=[]
    prestatus=[]
    for i in range (0,totalport):
        status.append(0)
        counter.append(0)
        prestatus.append(0)
    def read(self):
        self.status_all=sam.read_coils(0,count=totalport,unit=1)
        time.sleep(0.05)
        for i in range(0,totalport):
            self.status[i]=self.status_all.bits[i]
di=DI()
sam.read_coils(0,counter=totalport,unit=1)
sam.socket.timeout=.1

while(1):
    di.read()
    for i in range(0,totalport):
        if di.status[i]==True:
            if di.status[i]!=di.prestatus[i]:
                di.counter[i]+=1
                print("LED%d is on,Total:" %i)
                counter_all=''
                for i in monitor_port:
                    counter_all+='port'+str(i)+':'+str(di.counter[i])+' '
                print(counter_all)
    for i in range(0,totalport):
        di.prestatus[i]=di.status[i]
