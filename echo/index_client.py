from flask import Flask,request
app=Flask(__name__)

@app.route('/')
def index():
	return '''
	<h2>welcome to localhost:5000</h2>
	<h4>direct to physical to start physical client</br>
	direct to soft to start soft client<br>
	direct to listener to start display page<br>
	</h4>

	'''
@app.route('/soft')
def soft():
	#return app.send_static_file('soft_client.html')
	return 'hello,world'

if __name__=='__main__':
	app.run()
