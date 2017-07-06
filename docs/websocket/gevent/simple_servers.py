from gevent.server import StreamServer
import gevent
def handle(socket,address):
		socket.send("Hello from a telnet!\n")
		for i in range(5):
			socket.send(str(i)+'\n')

server=StreamServer(('127.0.0.1',5000),handle)
server.serve_forever()

