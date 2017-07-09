from bottle import error
from bottle import route, run, template

@route('/hello')
def hello():
	 return "Hello World!"
@route('/')
@route('/hello/<name>')
def greate(name):
		return template('Hello {{a}}, how are you?',a=name)

@route('/login')
def login():
		return '''
			<form action='/login' method='post'>
				Username: <input name='username' type='text' />
				Password: <input name='password' type='password' />
			</form>
		'''

@route('/login', method='POST')
def do_login():
	username= request.forms.get('username')
	password=request.forms.get('password')
	if check_login(username,password):
			return "<p>Your login information was correct.</p>"
	else:
			return "<p>Login failed.</p>"

@error(404)
def error404(error):
		return ''' <div style='color:black'>
		<h2>YOU SHALL NOT PASS!<h2>
		<p>  -----gandalf</p>
		</div>
				'''

run(host='localhost',port=8080,debug=True)

