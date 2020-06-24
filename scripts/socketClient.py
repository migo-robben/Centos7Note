# -*- coding: utf-8 -*- 

import socket
import struct
import sys
import pickle
import pickle_test as pk

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
# socket_client.send('Hello World')

# ----- function args ----- #
# data = pickle.dumps(args)
# socket_client.send(data)

# ----- send struct package ----- #
msg     = "Hello World, Hello Migo"
package = None
if sys.byteorder == 'little':
	package = struct.pack('<I', len(msg))
else:
	package = struct.pack('>I', len(msg))
send_msg = ''.join([package, msg])
print send_msg
socket_client.send(send_msg)


# receive data from the server 
print socket_client.recv(1024) 

# close the connection 
socket_client.close()
