#!/usr/bin/env python
from bottle import request, route, run, view

@route('/',method=['GET','POST'])
@view('form_template')
def index():
	return dict(parts=request.forms.sentence.split(),
		# split on whitespace
		show_form=request.method=='GET')
	#show form for get requests

run(host='localhost',port=8080)

