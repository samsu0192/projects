<script type='text/javascript' src='https://code.jquery.com/jquery-3.2.0.min.js'></script>
<script type='text/javascript' src='jquery.simple.websocket.js'></script>
<script type='text/javascript'>
	var webSocket=$simpleWebSocket({url:'ws://127.0.0.1:3000'})

	//reconnected listening
	webSocket.listen(function(message){
		console.log(message.text);
	});

	webSocket.send({'text':'hello'}).done(function(){
		//message send
	}).fail(function(e){
		//error sending
	});
</script>
