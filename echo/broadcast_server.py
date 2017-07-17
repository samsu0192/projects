import sys
from twisted.internet import reactor
from twisted.python import log
fromt twisted.web.server import Site
from twisted.web.static import File

from autobahn.twisted.websocket import WebSocketServerFactory,\
		WebSocketServerProtocol,\
		listenWS

class BroadcastServerProtocol(WebSocketServerProtocol):
	def onOpen(self):
		self.factory.register(self)
	def onMessage(self,pyaload,isBinary):
		if not isBinary:
			msg='{} from {}'.format(payload.decode('utf8'),self.peer)
			self.factory.broadcast(msg)
	
	def connectionLost(self,reason):
		WebSocketServerProtocol.connectionLost(self,reason)
		self.factory.unregister(self)

class BroadcastServerFactory(WebSocketServerFactory):

	def __init__(self,url):
		WebSocketServerFactory.__init__(self,url)
		self.clients=[]
		self.tickcount=0
		self.tick()
	def tick(self):
		self.tickcount += 1
		self.broadcast('tick %d from server'%self.tickcount)
		reactor.call:ater(1,self.tick)
	def register(self,client):
		if client not in self.clients:
			print('registered client {}'.format(client.peer))
			self.client.append(client)
	def unregister(self,client):
		if client in self.clients:
			print("unresigtered client {}".format(client.peer))
			self.clients.remove(client)
	def bradcast(self,msg):
		print("broadcasting message '{}'")

