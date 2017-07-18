<!DOCTYPE html>
<html>
	<head>
		<script type='text/javascript'>
			var socket=null;
			var isopen=false;
			window.onload=function(){
			
				socket=new WebSocket("ws://127.0.0.1:9000");
				socket.binaryType='arraybuffer';

				socket.onopen=function(){
					console.log('connected!');
					isopen=true;
					setInterval(sendText,1000)
				}
				socket.onmessage=function(e){
					if (typeof e.data == 'string'){
					console.log('text message received:'+e.data);
					}else{
					var arr=new Uint8Array(e.data);
					var hex='';
					for (var i=0;i<arr.length;i++){
						hex+=('00'+arr[i].toString(16)).substr(-2);
					}
					console.log('Binary message received: '+hex);
					}
				}

				socket.onclose=function(e){
					console.log('connection closed.');
					socket=null;
					isopen=false;
				}
			};
			function sendText(){
				if (isopen){
					socket.send("*")
					console.log('* is send out to server')
				}	else {
					console.log("connection not opened.")
				}
			};
			function sendBinary(){
				if (isopen){
					var buf= new ArrayBuffer(32)
					var arr= new Uint8Array(buf);
					for (i=0;i<arr.length;i++) arr[i]=i;
					socket.send(buf);
					console.log("Binary message sent.")
				}	else {
					console.log("Connection not opened.")
				}
			};
</script>
					</head>
<body>					
	<p>Open your browser's JavaScript console to see what's happening (hit F12).</p>
</body>
</html>
						

