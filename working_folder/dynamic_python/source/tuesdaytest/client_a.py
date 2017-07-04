from websocket import create_connection
ws=create_connection('ws://localhost:5000/echo')
print "Sending 'Hello,World'..."
ws.send("Hello,World")
print('sent')
print('receiving')
result=ws.recv()
print "received %s" %result
ws.close()
