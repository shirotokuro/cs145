import pyglet, math
from pyglet.window import key
import resources

class Player(pyglet.sprite.Sprite):
	"""A sprite with physical properties such as velocity"""
	
	def __init__( self, *args, **kwargs):
		super(Player, self).__init__(img=resources.player1_image, *args, **kwargs)
		
		self.right1, self.right2, self.right3 = resources.right(1)
		
		self.anim_right = pyglet.image.Animation.from_image_sequence([
        	self.right1, self.right2, self.right3], 0.1, True)
		self.right_sprite = pyglet.sprite.Sprite(img=self.anim_right, *args, **kwargs)
		self.right_sprite.x = self.x
		self.right_sprite.y = self.y
		self.right_sprite.visible = False
		self.scale = 0.5
		self.right_sprite.scale = 0.5

		self.left1, self.left2, self.left3 = resources.left(1)
		
		self.anim_left = pyglet.image.Animation.from_image_sequence([
        	self.left1, self.left2, self.left3], 0.1, True)
		self.left_sprite = pyglet.sprite.Sprite(img=self.anim_left, *args, **kwargs)
		self.left_sprite.x = self.x
		self.left_sprite.y = self.y
		self.left_sprite.visible = False
		
		# Velocity
		
		self.left_sprite.scale = 0.5
		self.thrust = 300.0
		self.velocity_x,self.velocity_y = 0.0,0.0
		self.key_handler = key.KeyStateHandler()

	def set(self, ptype=1):
		if ptype != 1:
			self.image = resources.player2_image
			self.image.x = self.x
			self.image.y = self.y
			self.right1, self.right2, self.right3 = resources.right(ptype)
			self.anim_right = pyglet.image.Animation.from_image_sequence([
        	self.right1, self.right2, self.right3], 0.1, True)
			self.right_sprite = pyglet.sprite.Sprite(img=self.anim_right, x=self.x, y=self.y, batch=self.batch)
			self.right_sprite.x = self.x
			self.right_sprite.y = self.y
			self.right_sprite.visible = False
			self.scale = 0.5
			self.right_sprite.scale = 0.5
			
			self.left1, self.left2, self.left3 = resources.left(ptype)
		
			self.anim_left = pyglet.image.Animation.from_image_sequence([
	        	self.left1, self.left2, self.left3], 0.1, True)
			self.left_sprite = pyglet.sprite.Sprite(img=self.anim_left, x=self.x, y=self.y, batch=self.batch)
			self.left_sprite.x = self.x
			self.left_sprite.y = self.y
			self.left_sprite.visible = False
			
			# Velocity
			self.scale = 0.5
			self.right_sprite.scale = 0.5
			self.left_sprite.scale = 0.5

	def move_right(self):
		self.right_sprite.x = self.x
		self.visible = False
		self.right_sprite.visible = True
		self.left_sprite.visible = False

	def move_left(self):
		self.left_sprite.x = self.x
		self.visible = False
		self.right_sprite.visible = False
		self.left_sprite.visible = True
	
	def check_bounds(self):
		min_x = -self.image.width/2
		min_y = -self.image.height/2
		max_x = 1024 + self.image.width/2
		max_y = 600 + self.image.height/2
		if self.x < min_x:
			self.x = max_x
		if self.y < min_y:
			self.y = max_y
		if self.x > max_x:
			self.x = min_x
		if self.y > max_y:
			self.y = min_y

	def update(self, dt):
		"""This method should be called every frame."""

		if self.key_handler[key.RIGHT]:
			# Note: pyglet's rotation attributes are in "negative degrees"
			force_x = self.thrust * dt
			force_y = self.thrust * dt
			self.x += force_x
			#self.y += force_y
			self.move_right()
			self.check_bounds()
			return key.RIGHT

		elif self.key_handler[key.LEFT]:
			# Note: pyglet's rotation attributes are in "negative degrees"
			force_x = self.thrust * dt
			force_y = self.thrust * dt
			self.x -= force_x
			#self.velocity_y -= force_y
			self.move_left()
			self.check_bounds()
			return key.LEFT

		else:
			self.visible = True
			self.right_sprite.visible = False
			self.left_sprite.visible = False
			return ''
	
	def remote_update(self, keys, dt):
		if keys == key.RIGHT:
			# Note: pyglet's rotation attributes are in "negative degrees"
			force_x = self.thrust * dt
			force_y = self.thrust * dt
			self.x += force_x
			#self.y += force_y
			self.move_right()
			self.check_bounds()

		elif keys == key.LEFT:
			# Note: pyglet's rotation attributes are in "negative degrees"
			force_x = self.thrust * dt
			force_y = self.thrust * dt
			self.x -= force_x
			#self.velocity_y -= force_y
			self.move_left()
			self.check_bounds()

		else:
			self.visible = True
			self.right_sprite.visible = False
			self.left_sprite.visible = False	