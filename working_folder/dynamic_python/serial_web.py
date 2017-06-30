from bottle import route,run,error,template
from bottle import static_file

a_message='hello world'
def pa_message():
		return a_message

@error(404)
def error404(error):
		return '''<dir id='sam_error' sytle='text-align:center'>
		<h2>404 NOT FOUND</h2>
		<p>Your SAN are dropping, please quit from this unknown place before too late ... </p>
		</dir>
		'''

@route('/samsu')
	pa_message()










run(host='localhost',port=3030)
