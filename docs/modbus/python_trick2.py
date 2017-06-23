#!/usr/bin/python
import time
from bottle import route 
from bottle import run 
@route('/trick')
def routeprint():		
	print("this is sam")
	i=0
	while(i<10):
		print("hello,world")
		print("can you here me?")
		time.sleep(1)
		i+=1

run(host='localhost',port=8000,debug=True)
