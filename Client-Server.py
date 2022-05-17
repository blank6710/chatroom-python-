#!/usr/bin/python
from socket import *
from threading import Thread
import sys

serverName="127.0.0.1"
serverPort=int(sys.argv[1])
user=sys.argv[2]

clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

def f(chat,clientSocket,user):
	clientSocket.send(user.encode())
	while True:
			if chat!="q":
				try:
					msg=clientSocket.recv(2048).decode()
					print(msg)
				
				except (KeyboardInterrupt, SystemExit):
  					print ("quitting")
			else:
				break
chat="HI"
t=Thread(target=f,args=(chat,clientSocket,user))
t.start()

while True:
	chat=input()
	if chat!="q":
		msg=user+" : "+chat
		clientSocket.send(msg.encode())
	else:
		clientSocket.send(chat.encode())
		break
clientSocket.close()






	
