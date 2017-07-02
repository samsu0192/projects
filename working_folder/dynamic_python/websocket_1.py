from websocket import create_connection
ws=create_connection('ws://localhost:8080/samsu')
print "Sending hello world"
ws.send('hello,world')
print 'sent'
print 'receiving'
result=ws.recv()
print "received '%s'" % result
ws.close()
