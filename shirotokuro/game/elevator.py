import pyglet
from lvl1_resources import elev

class Elevator(pyglet.sprite.Sprite):
	def __init__( self, *args, **kwargs):
		super(Elevator, self).__init__(img=elev, *args, **kwargs)
		self.dir= 0		#0= stationary, 1= up, 2= down

	def update(self):
		if self.dir == 1 and self.y <= 283:
			self.y += 3
		elif self.dir == 2 and self.y >= 242:
			self.y-= 3
