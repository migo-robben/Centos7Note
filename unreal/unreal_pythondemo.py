
class MyScopedDemoStructLock(object):
	def __init__(self, inst):
		self._inst = inst
	def __enter__(self):
		self._inst.lock()
	def __exit__(self, type, value, traceback):
		self._inst.unlock()