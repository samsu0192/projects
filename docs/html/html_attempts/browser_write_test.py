#This is a practice about how to display python message in a new browser page
def browser_display(program,url,body):
		import datetime
		from webbrowser import open_new_tab

		now=datetime.datetime.today().strftime('%d/%m/%Y-%H%M%S')
		filename='output_testingtext.html'
		f=open(filename,'w')
		
		wrapper="""<html>
		<head>
		<title>%s output -%s</title>
		</head>
		<body><p>URL: <a href=\"%"\">%s</a></p><p>%s</p></body>
		</html>"""

		whole=wrapper%(program,now,url,url,body)
		f.write(whole)
		f.close()

		open_new_tab(filename)

