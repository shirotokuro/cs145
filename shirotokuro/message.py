class Message(object):
	"""docstring for Message"""
	def __init__(self, data):
		self.type = data[0]
		self.pid = data[1]
		self.p2id = data[2]
		self.head = data[3]
		self.msg = data[4]
		