#server.py

from autobahn.twisted.websocket import WebSocketServerProtocol,\
		WebSocketServerFactory
	
class MyServerProtocol(WebSocketServerProtocol):
	payload_data=''
	prepayload_data=''
	def onConnect(self,request):
		print('Client connecting: {0}'.format(request.peer))

	def onOpen(self):
		print('WebSocket connection open.')
	
	def onMessage(self,payload,isBinary):
		if isBinary:
			print('Binary message received: {0} bytes'.format(len(payload)))
		elif(payload=='trigger'):
			print 'trigger received:{0}'.format(payload)	
			print 'send message to the html'+self.payload_data
			self.sendMessage(self.payload_data)
			self.prepayload_data=self.payload_data
		else:
			self.payload_data=payload
			print 'Text message received: {0}'.format(self.payload_data)
			self.sendMessage(('new:'+self.payload_data).encode('utf8'))
			self.sendMessage(('old'+self.prepayload_data).encode('utf8'))
	def onClose(self,wasClean,code,reason):
		print('WebSocket connection closed: {0}'.format(reason))
	
if __name__=='__main__':
	
	import sys
	from twisted.python import log
	from twisted.internet import reactor

	log.startLogging(sys.stdout)
	
	factory=WebSocketServerFactory(u"ws://127.0.0.1:9000")
	factory.protocol=MyServerProtocol
#factory.setProtocolOptions(maxConnections=2)
	
	reactor.listenTCP(9000,factory)
	reactor.run()

