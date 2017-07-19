from pymodbus.client.sync import ModbusSerialClient
import time
import sys

class DI():
	onTrigger=False
	status=[]
	counter=[]
	prestatus=[]
	message=''
	totalport=8
	monitor_port=[1,3,5]
	modport='/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AI04UGGP-if00-port0'
	mymodbus=ModbusSerialClient(method='rtu',port=modport,baudrate=9600)

	for i in range (0,totalport):
		status.append(0)
		counter.append(0)
		prestatus.append(0)

	def send(self,data):
		self.message=data
		print self.message
		sys.stdout.flush()

	def init(self):
		self.mymodbus.read_coils(0,count=self.totalport,unit=1)
		self.mymodbus.socket.timeout=.1
		self.send('test can begin')	

	def read(self):
		self.onTrigger=False
		self.status_all=self.mymodbus.read_coils(0,count=self.totalport,unit=1)
		for i in range(0,self.totalport):
			self.status[i]=self.status_all.bits[i]
	
	def write(self):
		for i in range(0,self.totalport):
			if self.status[i]==True:
				if self.status[i]!=self.prestatus[i]:
					self.onTrigger=True
					self.counter[i]+=1
					counter_all=''
					for j in self.monitor_port:
						counter_all+='port'+str(j)+':'+str(self.counter[j])+' '
					self.message= 'LED%d is on,Total: '%i + counter_all
					self.send(self.message)
		for i in range(0,self.totalport):
			self.prestatus[i]=self.status[i]

if __name__=='__main__':
	di=DI()
	di.init()
	while (1):
		di.read()
		di.write()
