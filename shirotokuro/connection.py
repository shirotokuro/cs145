import pickle

BUFFER_SIZE = 2048
class _myConnection(object):
	def __init__(self, s):
		self.s = s

	def sendMessage(self, msg):
		numBytes = self.s.send(pickle.dumps(msg))
		return numBytes > 0

	def getMessage(self):
		return pickle.loads(self.s.recv(BUFFER_SIZE))

def connection(s):
	return _myConnection(s)