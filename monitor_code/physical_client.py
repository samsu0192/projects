from autobahn.twisted.websocket import WebSocketClientProtocol,\
		WebSocketClientFactory
from serialmonitor2 import DI
import time
di=DI()
class MyClientProtocol(WebSocketClientProtocol):
	def onConnect(self,response):
		print('Server connected: {0}'.format(response.peer))
	
	def onOpen(self):
		print('WebSocket connection open.')
		di.init()
		self.sendMessage(di.message.encode('utf8'))
		def monitor():
			di.read()
			di.write()
			if di.onTrigger==True:
				self.sendMessage(di.message.encode('utf8'))
			self.factory.reactor.callLater(0.01,monitor)
		monitor()

	def onMessage(self,payload,isBinary):
		if isBinary:
			print('Binary message received: {0} bytes'.format(len(payload)))

		else:
			print('Text message received: {0}'.format(payload.decode('utf8')))
	
	def onClose(self,wasClean,code,reason):
		print('WebSocket connection closed: {0}'.format(reason))

if __name__=='__main__':
	
	import sys
	from twisted.python import log
	from twisted.internet import reactor

	log.startLogging(sys.stdout)

	factory=WebSocketClientFactory(u"ws://127.0.0.1:9000")
	factory.protocol=MyClientProtocol

	reactor.connectTCP('127.0.0.1',9000,factory)
	reactor.run()
