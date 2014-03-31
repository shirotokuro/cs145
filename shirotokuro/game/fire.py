import pyglet
import math

class Fire(pyglet.sprite.Sprite):
	def __init__( self, *args, **kwargs):
		super(Fire, self).__init__(*args, **kwargs)
		self.rotation= 45
		self.rotate_speed= 5
		self.velocity_x= 5

	def check_bounds(self):
		max_x= 1000 + self.image.width/2
		if self.x > max_x:
			self.x= -self.image.width/2

	def update(self):
		self.rotation += self.rotate_speed
		self.x += self.velocity_x
		self.check_bounds()

	def distance(self, point_1=(0, 0), point_2=(0, 0)):
		"""Returns the distance between two points"""
		return math.sqrt((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)

	def collides_with(self, other_object):

		collision_distance = self.image.width*0.5*self.scale \
                                + other_object.image.width*0.5*other_object.scale
        
		actual_distance = self.distance(self.position, other_object.position)
        
		return (actual_distance <= collision_distance)
