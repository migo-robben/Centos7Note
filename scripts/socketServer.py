# first of all import the socket library 
import socket
import pickle
import pickle_test as pk
import multiprocessing
import random

def func(a, b):
	print "{} + {} = {}".format(a, b, a+b)
	return a*b

def createFile(count):
	for i in range(count):
		with open("demo/demo_"+str(i)+".txt", "w") as f:
			for j in range(600000):
				f.write(str(random.randint(0, 4294967295)) + '\n')

# next create a socket object 
s = socket.socket()
print "Socket successfully created"

# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print "socket binded to %s" %(port)
  
# put the socket into listening mode
s.listen(5)
print "socket is listening"

# a forever loop until we interrupt it or
# an error occurs
while True:

	# Establish connection with client.
	c, addr = s.accept()
	print 'Got connection from', addr

	data = c.recv(1024)

	# ----- pickle data ----- #
	# obj = pickle.loads(data)
	# print(obj.name, obj.phoneNumber)

	# ----- string ----- #
	# print data.encode('utf-8')

	# ----- function args ----- #
	args = pickle.loads(data)
	count = func(*args)

	m = multiprocessing.Process(target=createFile, args=(count, ))
	m.daemon = True
	m.start()

	# send a thank you message to the client.
	c.send('Thank you for connecting')

	# Close the connection with the client 
	c.close() 