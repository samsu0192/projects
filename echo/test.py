from serialmonitor2 import DI
di=DI()
di.init()
while (1):
	di.read()
	di.write()
	if di.onTrigger==True:
		print 'testing testing 123'
