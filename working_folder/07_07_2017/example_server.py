from bottle import request,Bottle,abort
app=Bottle()
@app.route('/websocket')
def handle_websocket():
	wsock=request.environ.get('wsgi.websocket')
	if not wsock:
		abort(400,'Expected WebSocket request.')

	while True:
		try:
			message=wsock.receive()
			wsock.send('Your message was: %r' % message)
		except WebSocketError:
			break

from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.error import WebSocketError
server=WSGIServer(('127.0.0.1',8080),app,handler_class=WebSocketHandler)
server.serve_forever()
