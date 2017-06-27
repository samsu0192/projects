from bottle import route, run, error,template
from bottle import static_file

from bottle import static_file
@route('/')
def hello():
	return ''' hello world <br>
				hello world
	<script type='text/javascript' src='/static/hello.js'>
			</script>
			<br>
			<script>
			document.write('how to write script')
			</script>
			<dir>
			<h2>hello world</h2>
			</dir>
		'''
@route('/testing')	
def testing():
	return '''
			<script>
			function startTimer(){
				setInterval(writeToScreen,3000)
			}
			function writeToScreen(){
				

			}
			</script>
		<body onload='startTimer()'>
		<p id='loadhere'></p>
		</body>
		'''
@error(404)
def error404(error):
		return '''<dir id='error' style='text-align:center'>
		<h2>404 NOT FOUND</h2>
		<p>Your SAN are dropping, please quit from this unkown place before too late...</p>
		</dir>'''

run(host='localhost',port=8080)
