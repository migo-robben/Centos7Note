# -*- coding: utf-8 -*- 

import socket
import struct
import sys
import pickle
import pickle_test as pk

import threading

single_thread_test = True

# ------ single thread test ------ #
if single_thread_test:
	# ----- init obj ----- #
	obj = pk.testObject()
	obj.name = "Migo"
	obj.setPhoneNumber("555-1234")

	# ----- args list ----- #
	args = [5, 3]

	# Create a socket object 
	socket_client = socket.socket()
	  
	# Define the port on which you want to connect 
	port = 12345

	# connect to the server on local computer 
	socket_client.connect(('127.0.0.1', port))

	# ----- pickle data ----- #
	# data = pickle.dumps(obj)
	# socket_client.send(data)

	# ----- string ----- #
	socket_client.sendall(b'Hello World')

	# ----- function args ----- #
	# data = pickle.dumps(args)
	# socket_client.send(data)

	# ----- send struct package ----- #
	# msg     = "Hello World, Migo"
	# package = None
	# if sys.byteorder == 'little':
	# 	package = struct.pack('<I', len(msg))
	# else:
	# 	package = struct.pack('>I', len(msg))
	# send_msg = ''.join([package, msg])
	#  socket_client.send(send_msg)

	# receive data from the server 
	print(socket_client.recv(1024).decode("utf-8"))

	# close the connection 
	socket_client.close()

else:
	def creatSocket(threadID):
		# print(threadID)
		socket_client = socket.socket()
		port = 12345
		socket_client.connect(('127.0.0.1', port))
		sent_msg = 'Hello World_' + str(threadID)
		sent_msg = sent_msg.encode('utf-8')
		socket_client.sendall(sent_msg)
		print(socket_client.recv(1024).decode("utf-8"))
		socket_client.close()

	thread_count = 5
	threads = []
	for i in range(thread_count):
		t = threading.Thread(target=creatSocket, args=(i, ))
		t.start()
		threads.append(t)

	for thread in threads:
		thread.join()
