import struct
import sys

def decorator1(func):
 
    def wrapper(*args, **kwargs):
        print("Wrapper 1")
 
        func(*args, **kwargs)
 
    return wrapper

def decorator2(func):
 
    def wrapper(*args, **kwargs):
        print("Wrapper 2")
 
        func(*args, **kwargs)
 
    return wrapper

def MAINDEC():
    def decorator3(func):
 
        def wrapper(*args, **kwargs):
            print("Wrapper 3")
     
            func(*args, **kwargs)
     
        return wrapper
    return decorator3

@decorator1
@decorator2
@MAINDEC()
def add(a, b):
    print "{} + {} = {}".format(a, b, a+b)
add(5, 16)

class testObject(object):
    def __init__(self):
        self.name = "Migo"

    def getName(self):
        return self.name

tObj = testObject()
if hasattr(tObj, "getName"):
    func = getattr(tObj, "getName")
    print func()