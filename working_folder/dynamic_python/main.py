from bottle import route, run, error,template
from bottle import static_file
import os

@route('/happyhero')
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
@route('/samsu')

def samsu():
		return '''

		<p id='samsu_write'></p>
		<script>
		document.write('helloworld22')
		document.getElementById('samsu_write').innerHTML='helloworld'
		</script>

<dir>
		</dir>
		'''
@route('/samsu1')
def samsu1():
		return '''
		<button id='but_samsu1' type='button'>test_but</button>
		<script>
		function samsu_alert(){
		alert('this is a test alert')
		}
		document.getElementById('but_samsu1').onclick=samsu_alert
		</script>
		'''


@route('/testing')	
def testing():
	return '''
			<script>
			function startTimer(){
				setInterval(writeToScreen,3000)
			}
			function writeToScreen(){

				var pre=document.createElement('p');
				pre.sytle.wordWrap="break-word";
				pre.innerHTML='hello world'
				output.appendChild(pre);
			}
			</script>
		<body onload='startTimer()'>
		<div id='output'>hello world</div>
		</body>
		'''

@route('/static/<filename>')
def server_static(filename):
	return static_file(filename,root=os.path.dirname(os.path.abspath(filename)))

@error(404)
def error404(error):
		return '''<dir id='error' style='text-align:center'>
		<h2>404 NOT FOUND</h2>
		<p>Your SAN are dropping, please quit from this unkown place before too late...</p>
		</dir>'''

run(host='localhost',port=8080)
