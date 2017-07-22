# briefly introduce usage, function, and possible improvement about monitor_code

//introduction of needed module
'''
autobahn,twisted,pymodbus
#install method
pip install <module name>
#due to the constraint of pi, twisted might need to be degraded to a lower version before the code can be run
'''

//introduction of using method
'''
1. wiring up the unibeat test device and power up
2. run server.py
3. run physical_client.py
4. open soft_client and listener_client in browser
5. in listenser_client press trigger to start request message
6. press physical led botton, signal will be count in left column
7. press aux1 and aux2 botton, signal will be count in right column 
'''

//introduction of function
'''
1.serialmonitor2.py is a core monitoring code for DIO, can be directly run to monitor DIO trigger status
2.physical_client.py is a client based on serialmonitor2.py, will send trigger message to server
3.soft_client.html is a soft client which will send button push message to server
4.server.py is to create server which will collect all message from client and send all of them to listener.html
5.listen.py is to continue request to receive message from server after trigger button push,and distribute the received message according to  the agreed key word
'''

//breifly introduction about key word system and local data base system
'''
1.server.py contain a local data_base sytem and key word system
2.local data_base system only can store one message,(related to varible prepayload_data and payload_data),and only will send the message to client who push key word 'trigger' to server
3. the message will only be send out once until a new message was stored in the local data_base
4. listener.html contain key_word system, will receive all message from server and arrange them according to keyword
5. after trigger button pushed, listener.html will continue send keyword 'trigger' to server every 0.1 second to request for message
'''

//possible improvement about monitor_code
1. improve on error check part for easier troubleshooting
2. improve on keyword(also can called self_made protocol) to support communicate between two client, or subscribe system.
3. use python flask module to create an index for all client for easier use
4. improve on the local database so that it can support multiple message storage, think out better  algorithm to go over data_base quickly
5. rewrite core function (ex. local_database) in C will highly improve the perfomance, coz C can deal with data based on address.Also only key function rewrite will not be a big workload, third_party data_base is good, but sometime it is over developed for the real situation  application.
6. have fun :)
