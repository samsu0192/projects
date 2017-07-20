#server.py

from autobahn.twisted.websocket import WebSocketServerProtocol,\
		WebSocketServerFactory
payload_data=''
prepayload_data=''

class MyServerProtocol(WebSocketServerProtocol):
	def onConnect(self,request):
		print('Client connecting: {0}'.format(request.peer))

	def onOpen(self):
		print('WebSocket connection open.')
	
	def onMessage(self,payload,isBinary):
		global payload_data,prepayload_data
		if isBinary:
			print('Binary message received: {0} bytes'.format(len(payload)))
		elif(payload=='trigger'):
			if prepayload_data!=payload_data:
				print 'trigger received'
				print 'send message to html: '+payload_data
				self.sendMessage(payload_data)
				prepayload_data=payload_data
		else:
			payload_data=payload
			print 'Text message received: {0}'.format(payload_data)
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

