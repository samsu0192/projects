#!/usr/bin/python
from pymodbus.client.sync import ModbusSerialClient
import time
#import bottle

#@route('/modbus')

#port parameter settings
totalport=8
monitor_port=[1,3,5]
modport='/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AI04UGGP-if00-port0'
mymodbus=ModbusSerialClient(method='rtu',port=modport,baudrate=9600)
mymodbus.read_coils(0,count=totalport,unit=1)
mymodbus.socket.timeout=.1
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
        self.status_all=mymodbus.read_coils(0,count=totalport,unit=1)
        for i in range(0,totalport):
            self.status[i]=self.status_all.bits[i]
di=DI()

#run(host='localhost',port=8080,debug=True)

while(1):
    di.read()
	for i in range(0,totalport):
		if di.status[i]==True:
			if di.status[i]!=di.prestatus[i]:
				di.counter[i]+=1
				for i in monitor_port:
					counter_all+='port'+str(i)+':'+str(di.counter[i])+' '
				print 'LED%d is on,Total: '+counter_all
	for i in range(0,totalport):
		di.prestatus[i]=di.status[i]

