import pyglet, math
from pyglet.window import key
import resources

class Player(pyglet.sprite.Sprite):
	"""A sprite with physical properties such as velocity"""
	
	def __init__( self, *args, **kwargs):
		super(Player, self).__init__(img=resources.player1_image, *args, **kwargs)
		
		self.right1, self.right2, self.right3 = resources.right(1)
		
		self.anim_right = pyglet.image.Animation.from_image_sequence([
        	#self.right1, self.right2, self.right3], 0.1, True)
			self.right1, self.right2], 0.1, True)
		self.right_sprite = pyglet.sprite.Sprite(img=self.anim_right, *args, **kwargs)
		self.right_sprite.x = self.x
		self.right_sprite.y = self.y
		self.right_sprite.visible = False

		self.left1, self.left2, self.left3 = resources.left(1)
		
		self.anim_left = pyglet.image.Animation.from_image_sequence([
        	self.left1, self.left2, self.left3], 0.1, True)
		self.left_sprite = pyglet.sprite.Sprite(img=self.anim_left, *args, **kwargs)
		self.left_sprite.x = self.x
		self.left_sprite.y = self.y
		self.left_sprite.visible = False
		
		# Scale
		
		#self.scale = 0.5
		#self.right_sprite.scale = 0.5
		#self.left_sprite.scale = 0.5
		self.velocity_x,self.velocity_y = 0.0,0.0
		self.key_handler = key.KeyStateHandler()

		self.floor = self.y
		self.ceiling = self.y + self.height
		self.min_wall = self.image.width/2
		self.max_wall = 1024 - self.image.width/2
		self.jumping = False
		self.gravity = 0.068
		self.thrust = 60 * self.gravity


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
			
			self.left1, self.left2, self.left3 = resources.left(ptype)
		
			self.anim_left = pyglet.image.Animation.from_image_sequence([
	        	self.left1, self.left2, self.left3], 0.1, True)
			self.left_sprite = pyglet.sprite.Sprite(img=self.anim_left, x=self.x, y=self.y, batch=self.batch)
			self.left_sprite.x = self.x
			self.left_sprite.y = self.y
			self.left_sprite.visible = False
			
			# Scale
			#self.scale = 0.5
			#self.right_sprite.scale = 0.5
			#self.left_sprite.scale = 0.5

	def move_right(self):
		self.check_bounds()
		self.right_sprite.x = self.x
		self.right_sprite.y = self.y
		self.visible = False
		self.right_sprite.visible = True
		self.left_sprite.visible = False

	def move_left(self):
		self.check_bounds()
		self.left_sprite.x = self.x
		self.left_sprite.y = self.y
		self.visible = False
		self.right_sprite.visible = False
		self.left_sprite.visible = True

	def move_up(self, dt):
		self.check_bounds()	
		if self.jumping == False:
			self.velocity_y = 60 * self.gravity
			sound = pyglet.resource.media('sounds/jump.wav')
			sound.play()
		self.jumping = True
		
	
	def check_bounds(self):
		min_x = self.min_wall
		min_y = self.floor
		max_x = self.max_wall
		max_y = self.ceiling

		if self.x < min_x:
			self.x = min_x
		if self.y < min_y:
			self.y = min_y
		if self.x > max_x:
			self.x = max_x
		if self.y > max_y:
			self.y = max_y

	def update(self, dt):
		"""This method should be called every frame."""
		if self.jumping == True:
			self.velocity_y -= self.gravity * 2
			self.y += self.velocity_y
			
			if self.y < self.floor:
				self.velocity_y = 0
				self.y = self.floor
				self.jumping = False
			
			self.check_bounds()
		else:
			if self.key_handler[key.UP]:
				self.move_up(dt)
				return key.UP

		if self.key_handler[key.RIGHT]:
			self.velocity_x = self.thrust
			self.x += self.velocity_x
			self.move_right()
			
			if self.key_handler[key.UP]:
				self.move_up(dt)
				return 'jumping_right'
			
			return key.RIGHT

		elif self.key_handler[key.LEFT]:
			self.velocity_x = self.thrust 
			self.x -= self.velocity_x
			self.move_left()

			if self.key_handler[key.UP]:
				self.move_up(dt)
				return 'jumping_left'
			return key.LEFT

		else:
			self.visible = True
			self.right_sprite.visible = False
			self.left_sprite.visible = False
			return ''
	
	def remote_update(self, keys, dt):
		if self.jumping == True:
			self.velocity_y -= self.gravity * 2
			self.y += self.velocity_y
			if self.y < self.floor:
				self.velocity_y = 0
				self.y = self.floor
				self.jumping = False
			elif self.y > self.ceiling:
				self.y = self.ceiling
		else:
			if keys == key.UP:
				self.move_up(dt)

		if keys == key.RIGHT or keys == 'jumping_right':
			self.velocity_x = self.thrust
			self.x += self.velocity_x
			self.move_right()

			if keys == 'jumping_right':
				self.move_up(dt)
			

		elif keys == key.LEFT or keys == 'jumping_left':
			self.velocity_x = self.thrust
		
			self.x -= self.velocity_x
			self.move_left()
			
			if keys == 'jumping_left':
				self.move_up(dt)
		

		else:
			self.visible = True
			self.right_sprite.visible = False
			self.left_sprite.visible = False	