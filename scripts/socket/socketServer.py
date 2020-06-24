# -*- coding: utf-8 -*-

import socket
import pickle
import struct
import sys
import multiprocessing
import random

def func(a, b):
	print("{} + {} = {}".format(a, b, a+b))
	return a+b

def createFile(count):
	for i in range(count):
		with open("demo/demo_"+str(random.randint(0, 168))+".txt", "w") as f:
			for j in range(600000):
				f.write(str(random.randint(0, 4294967295)) + '\n')

if __name__ == "__main__":
	# next create a socket object
	socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	print("Socket successfully created")

	# reserve a port on your computer in our
	# case it is 12345 but it can be anything
	
	port = 12345
	# Next bind to the port
	# we have not typed any ip in the ip field
	# instead we have inputted an empty string
	# this makes the server listen to requests
	# coming from other computers on the network
	socket_server.bind(('', port))
	print("socket binded to %s" %(port))

	# put the socket into listening mode
	socket_server.listen(5)
	print("socket is listening")

	# a forever loop until we interrupt it or
	# an error occurs
	while True:

		# Establish connection with socket.
		# s is the client socket object
		s, addr = socket_server.accept()
		print('Got connection from', addr)

		# ----- pickle data ----- #
		# data = s.recv(1024)
		# obj = pickle.loads(data)
		# print(obj.name, obj.phoneNumber)

		# ----- string ----- #
		data = s.recv(1024)
		print(data.decode('utf-8'))

		# ----- function args ----- #
		# data = s.recv(1024)
		# args = pickle.loads(data)
		# count = func(*args)
		#
		# m = multiprocessing.Process(target=createFile, args=(count, ))
		# m.daemon = True
		# m.start()

		# ----- send struct package ----- #
		# raw_mslen 确认之后要受到信息的长度
		# raw_mslen = s.recv(4)
		# if sys.byteorder == 'little':
		# 	msglen = struct.unpack('<I', raw_mslen)[0]
		# else:
		# 	msglen = struct.unpack('>I', raw_mslen)[0]

		# recv_msg = s.recv(msglen)
		# print(recv_msg)

		# send a thank you message to the s.
		s.sendall(b'Thank you for connecting.')

		# Close the connection with the s
		s.close()
