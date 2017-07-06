import SimpleHTTPServer
import SocketServer as socketserver
import os
import threading

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	path_to_image='RGBWebcam1.png'
	img=open(path_to_img,'rb')
	statinfo.os.stat(path_to_image)
	img_size=statinfo.st_size
	print(im_size)

def do_HEAD(self):
	self.send_response(200)
	self.send_header('Content-type','image/png')
	self.send_header('Content-length',img_size);
	self.end_headers()

def do_GET(self):
	self.send_response(200)
	self.send_header('Content-type','img/png')
	self.send_header('Content-length',img_size)
	self.end_headers()
	f=open(path_to_image,'rb')
	self.wfile.write(f.read())
	f.close()

class MyServer(socketserver.ThreadingMixIn,socketserver.TCPServer):
	def __init__(self,server_address,RequestHanderClass):
		self.allow_reuse_reuse_address=True
		socketserver.TCPServer.__init__(self,server_address,RequestHanderClass,False)

if __name__ == "__main__":
	HOST,PORT ='127.0.0.1',990
	server=MyServer((HOST,PORT),MyHandler)
	server.server_bind()
	server.server_activate()
	server_thread=threading.Thread(target=server.serve_forever)
	server_thread.start()
	while(1):
		print 'test'
