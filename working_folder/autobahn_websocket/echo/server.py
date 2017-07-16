#server.py

from autobahn.twisted.websocket import WebSocketServerProtocol,\
		WebSocketServerFactory

class MyServerProtocol(WebSocketServerProtocol):

	def onConnect(self,request):
		print('Client connecting: {0}'.format(request.peer))

	def onOpen(self):
		print('WebSocket connection open.')
	
	def onMessage(self,payload,isBinary):

