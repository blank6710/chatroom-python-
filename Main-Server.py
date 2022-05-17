#!/usr/bin/python
from socket import *
from threading import Thread
import sys

serverName="127.0.0.1"
serverPort=int(sys.argv[1])


serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(10)
clients=[]

print("Server started at IP address {} and Port number {}".format(serverName,serverPort))

def func(connectionSocket):
	connectionSocket.send("Welcome to my chat room".encode())
	user=connectionSocket.recv(2048).decode()
	while True:
		try:
			received=connectionSocket.recv(2048).decode()
			if received!="q":
				print(received)
				for i in clients:
					if i!=connectionSocket:
						try:
							i.send(received.encode())
						except:
							i.close()
			else:
				print(user+" is logged off...Good bye !!")
				connectionSocket.send("Bye".encode())
				break
		except (KeyboardInterrupt, SystemExit):
  			print ("quitting")
	connectionSocket.close()
	
	
while True:
	connectionSocket,addr=serverSocket.accept()
	print("Connection request from {}".format(addr))
	clients.append(connectionSocket)
	th=Thread(target=func,args=(connectionSocket,))
	th.start()
	
	


