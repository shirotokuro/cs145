import pyglet, random, math, socket, connection
from game import player, resources
class Gamewindow(object):
	"""docstring for Gamewindow"""
	def __init__(self, arg):
		super(Gamewindow, self).__init__()
		self.arg = arg
		
