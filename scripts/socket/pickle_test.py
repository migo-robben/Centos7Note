# -*- coding: utf-8 -*- 
import pickle

class testObject(object):
	def __init__(self, name=""):
		self.name = name
		self.phoneNumber = None
	def setPhoneNumber(self, number):
		self.phoneNumber = number

# dataList = [[1, 1, 'yes'],
# 			[1, 1, 'yes'],
# 			[1, 0, 'no'],
# 			[0, 1, 'no'],
# 			[0, 1, 'no']]

# with open('demo.pkl','wb') as in_data:
# 	pickle.dump(dataList, in_data, pickle.HIGHEST_PROTOCOL)

# with open('demo.pkl','rb') as out_data:
# 	data = pickle.load(out_data)
# 	print(data)

# tObj = testObject("Migo")
# tObj.setPhoneNumber("123456")

# tObj1 = testObject("Jimmy")
# tObj1.setPhoneNumber("555-1234")

# with open('demo.pkl','wb') as in_data:
# 	pickle.dump(tObj, in_data, pickle.HIGHEST_PROTOCOL)
# 	pickle.dump(tObj1, in_data, pickle.HIGHEST_PROTOCOL)

# with open('demo.pkl','rb') as out_data:
# 	data = pickle.load(out_data)
# 	print("Name: {}, PhoneNumber: {}".format(data.name, data.phoneNumber))
# 	data = pickle.load(out_data)
# 	print("Name: {}, PhoneNumber: {}".format(data.name, data.phoneNumber))


a = "Hello"
print(pickle.dumps(a))