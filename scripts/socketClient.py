# -*- coding: utf-8 -*- 

# Import socket module 
import socket
import pickle
import pickle_test as pk

# ----- init obj ----- #
obj = pk.testObject()
obj.name = "Migo"
obj.setPhoneNumber("555-1234")

# ----- args list ----- #
args = [5, 5]

# Create a socket object 
s = socket.socket()
  
# Define the port on which you want to connect 
port = 12345

# connect to the server on local computer 
s.connect(('127.0.0.1', port))

# ----- pickle data ----- #
# data = pickle.dumps(obj)
# s.send(data)

# ----- string ----- #
# s.send('Hello World')

# ----- function args ----- #
data = pickle.dumps(args)
s.send(data)

# receive data from the server 
print s.recv(1024) 
# close the connection 
s.close()
