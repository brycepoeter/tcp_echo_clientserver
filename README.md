# tcp_echo_clientserver
Simple TCP socket that echos requests. Can run on same machine or different machines. 

tcp_client takes IP address as argv[1] and port as argv[2]   
tcp_server takes port as argv[1]   
  
You'll need to run the programs in different terminal windows/tabs   

in one, run something like
python tcp_server.py 5555  
where 5555 is a large port number of your choice 

in the other, run  
python tcp_client.py IP.ADD.DDR.ESS 5555  
where IP address is your IP address  
(on mac, you can find at System Preferences -> Network)    

messages entered into the client terminal will echo  
in the server terminal and return the message  

TCP socket 
