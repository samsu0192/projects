from bottle import route,run,error,template
from bottle import static_file
import os
import time
from websocket import create_connection


@route('/samsu')
def hello():
		return '''
		<h2 style='text-align:center;'>Hello World</h2>
		'''

run(host='localhost',port=8080)
time.sleep(10)


ws=create_connection('ws://localhost:8080/samsu')
print 'sending hello world'
ws.send('i dont want to send hello world')
print 'receiving'
result=ws.recv()
print 'received %s' %result
