import pyglet, math
from pyglet.window import key
import resources
from lvl1 import elevator, fire

class Player(pyglet.sprite.Sprite):
	"""A sprite with physical properties such as velocity"""
	
	def __init__( self, lvl, *args, **kwargs):
		super(Player, self).__init__(img=resources.player1_image, *args, **kwargs)
		
		self.right1, self.right2= resources.right(1)
		
		self.anim_right = pyglet.image.Animation.from_image_sequence([
        	#self.right1, self.right2, self.right3], 0.1, True)
			self.right1, self.right2], 0.1, True)
		self.right_sprite = pyglet.sprite.Sprite(img=self.anim_right, *args, **kwargs)
		self.right_sprite.x = self.x
		self.right_sprite.y = self.y
		self.right_sprite.visible = False

		self.left1, self.left2= resources.left(1)
		
		self.anim_left = pyglet.image.Animation.from_image_sequence([
        	self.left1, self.left2], 0.1, True)
		self.left_sprite = pyglet.sprite.Sprite(img=self.anim_left, *args, **kwargs)
		self.left_sprite.x = self.x
		self.left_sprite.y = self.y
		self.left_sprite.visible = False
		
		# Scale
		self.scale = 0.50
		self.right_sprite.scale = 0.50
		self.left_sprite.scale = 0.50

		self.velocity_x,self.velocity_y = 0.0,0.0
		self.key_handler = key.KeyStateHandler()

		self.floor = self.y
		self.ceiling = self.y + self.height
		self.min_wall = self.image.width*self.scale/2
		self.max_wall = 1000 - self.image.width*self.scale/2
		self.roof= 560 - self.image.height*self.scale/2
		self.jumping = False
		self.gravity = 0.068
		self.thrust = 60 * self.gravity
 
		self.lvl= lvl
		self.ptype= 1
		self.obj_size= 40
		self.dead = False
		self.fin= False
		self.gem_count= 3
		self.onElev= False
		self.stepper= 0
		self.counter = 0

	def set(self, ptype=1):
		if ptype != 1:
			self.image = resources.player2_image
			self.image.x = self.x
			self.image.y = self.y
			self.right1, self.right2= resources.right(ptype)
			self.anim_right = pyglet.image.Animation.from_image_sequence([
        	self.right1, self.right2], 0.1, True)
			self.right_sprite = pyglet.sprite.Sprite(img=self.anim_right, x=self.x, y=self.y, batch=self.batch)
			self.right_sprite.x = self.x
			self.right_sprite.y = self.y
			self.right_sprite.visible = False
			
			self.left1, self.left2= resources.left(ptype)
		
			self.anim_left = pyglet.image.Animation.from_image_sequence([
	        	self.left1, self.left2], 0.1, True)
			self.left_sprite = pyglet.sprite.Sprite(img=self.anim_left, x=self.x, y=self.y, batch=self.batch)
			self.left_sprite.x = self.x
			self.left_sprite.y = self.y
			self.left_sprite.visible = False
			
			# Scale
			self.scale = 0.50
			self.right_sprite.scale = 0.50
			self.left_sprite.scale = 0.50

			self.ptype = 2

	def move_right(self):
		self.check_bounds(1)
		self.right_sprite.x = self.x
		self.right_sprite.y = self.y
		self.visible = False
		self.right_sprite.visible = True
		self.left_sprite.visible = False

	def move_left(self):
		self.check_bounds(2)
		self.left_sprite.x = self.x
		self.left_sprite.y = self.y
		self.visible = False
		self.right_sprite.visible = False
		self.left_sprite.visible = True

	def move_up(self, dt):
		if self.check_bounds(3):
			if self.jumping == False:
				self.velocity_y = 60 * self.gravity
				sound = pyglet.resource.media('sounds/jump.wav')
				#sound.play()
			self.jumping = True
	
	def check_bounds(self, dir):
		min_x = self.min_wall
		min_y = self.floor
		max_x = self.max_wall
		max_y = self.ceiling

		self.fin= False

		if self.x < min_x:
			self.x = min_x
		elif self.y < min_y:
			self.y = min_y
		elif self.x > max_x:
			self.x = max_x
		elif self.y > max_y:
			self.y = max_y 
		elif self.y > self.roof:
			self.jumping= False
		elif dir == 1:
			#right
			x_index = int(math.floor((self.x+(self.image.width*self.scale)/2)/self.obj_size))
			y_index = int(math.floor(self.y/self.obj_size))
			if x_index >= 25:
				x_index = 24
			if self.lvl[y_index][x_index] >= 1 and self.lvl[y_index][x_index] <= 7: 
				self.x= x_index*self.obj_size - (self.image.width*self.scale)/2
			elif self.ptype == 1 and self.lvl[y_index][x_index] == 9 and (x_index*40 + 13) <= (self.x +(self.image.width*self.scale)/2) <= (x_index*40 +15):
				self.gem_count= self.gem_count -1
				self.lvl[y_index][x_index] = 0
			elif self.ptype == 2 and self.lvl[y_index][x_index] == 8 and (x_index*40 + 12) <= (self.x +(self.image.width*self.scale)/2) <= (x_index*40 +16):
				self.gem_count= self.gem_count -1
				self.lvl[y_index][x_index] = 0
		elif dir == 2:
			#left
			x_index = int(math.floor((self.x-(self.image.width*self.scale)/2)/self.obj_size))
			y_index = int(math.floor(self.y/self.obj_size))
			if self.lvl[y_index][x_index] >= 1 and self.lvl[y_index][x_index] <= 7: 
				self.x= (x_index+1)*self.obj_size + (self.image.width*self.scale)/2
			elif self.ptype == 1 and self.lvl[y_index][x_index] == 9 and (x_index*40 + 24) <= math.floor(self.x-(self.image.width*self.scale)/2) <= (x_index*40 + 28) :
				self.gem_count= self.gem_count -1
				self.lvl[y_index][x_index] = 0
			elif self.ptype == 2 and self.lvl[y_index][x_index] == 8 and (x_index*40 + 24) <= math.floor(self.x-(self.image.width*self.scale)/2) <= (x_index*40 + 28):
				self.gem_count= self.gem_count -1
				self.lvl[y_index][x_index] = 0
		elif dir == 3:
			#jump
			x_index = int(math.floor(self.x/self.obj_size))
			y_index = int(math.floor((self.y+(self.image.height*self.scale)/2)/self.obj_size))
			if (self.lvl[y_index][x_index] >= 1 and self.lvl[y_index][x_index] <= 7) or (self.lvl[y_index][x_index] >= 14 and self.lvl[y_index][x_index] <=16): 
				return False
			return True
		elif dir == 4:
			#fall and other things
			x_index = int(math.floor(self.x/self.obj_size))
			y_index = int(math.floor((self.y-(self.image.height*self.scale)/2)/self.obj_size))
			y_index2= int(math.ceil((self.y-(self.image.height*self.scale/2))/self.obj_size)) 
			if self.onElev and x_index != 0:
				self.onElev = False
			
			if (self.lvl[5][5]!= 17 or self.lvl[8][6] != 17) and self.stepper == self.ptype:
				if x_index != 5 and 215 <= self.y <= 255:
					self.lvl[5][5] = 17
					elevator.dir= 2
					self.stepper = 0
				elif x_index != 6 and 345 <= self.y <= 375:
					self.lvl[8][6] = 17
					elevator.dir= 2
					self.stepper = 0
			if fire.collides_with(self):
				self.dead = True
				fire.visible= False
			elif self.onElev and not self.jumping:
				self.floor= self.y = elevator.y + (self.image.height*self.scale)/2
				self.ceiling = self.floor + self.height
			elif x_index == 0 and ((240 <= elevator.y <= 243 and 260 <= self.y <= 264) or ( 280 <= elevator.y <= 286 and 301 <= self.y <= 305)):
				self.floor= self.y = elevator.y + (self.image.height*self.scale)/2
				self.ceiling = self.floor + self.height
				self.onElev = True
			elif self.lvl[y_index][x_index] >= 1 and self.lvl[y_index][x_index] <= 7:
				self.y= self.floor= (y_index+1)*self.obj_size + (self.image.height*self.scale)/2
				self.ceiling = self.y + self.height
			elif self.lvl[y_index-1][x_index] == 0 or self.lvl[y_index-1][x_index] == 15:
				self.floor= (y_index-1)*self.obj_size + (self.image.height*self.scale)/2
			elif self.ptype == 1 and (self.lvl[y_index2-1][x_index] == 16 or self.lvl[y_index2-1][x_index] == 14):
				self.dead = True
			elif self.ptype == 2 and (self.lvl[y_index2-1][x_index] == 15 or self.lvl[y_index2-1][x_index] == 14):
				self.dead = True
			elif self.gem_count == 0 and self.ptype == 1 and 775 <= self.x <= 785 and 503.0 <= self.y <= 507.0:
				self.fin= True
			elif self.gem_count == 0 and self.ptype == 2 and 895 <= self.x <= 905 and 503.0 <= self.y <= 507.0:
				self.fin= True
			elif self.ptype == 1 and self.lvl[y_index][x_index] == 9 and (y_index*40 + 23) <= (self.y-(self.image.height*self.scale)/2) <= (y_index*40 + 29):
				self.gem_count= self.gem_count -1
				self.lvl[y_index][x_index] = 0
			elif self.ptype == 2 and self.lvl[y_index][x_index] == 8 and (y_index*40 + 23) <= (self.y-(self.image.height*self.scale)/2) <= (y_index*40 + 29):
				self.gem_count= self.gem_count -1
				self.lvl[y_index][x_index] = 0
			elif self.lvl[y_index][x_index] == 17 and (235<= self.y <= 240 or 355<= self.y <= 360):
				#print 'purintu'
				self.lvl[y_index][x_index] = 0
				if elevator.dir == 0:
					elevator.dir = 1
				elif elevator.dir == 1:
					elevator.dir = 2 
				elif elevator.dir == 2:
					elevator.dir = 1
				self.stepper = self.ptype

	def delete(self):
		self.right_sprite.delete()
		self.left_sprite.delete()
		super(Player, self).delete()

	def update(self, dt):
		"""This method should be called every frame."""
		if self.jumping == True:
			self.velocity_y -= self.gravity * 2
			self.y += self.velocity_y
			
			if self.y < self.floor:
				self.velocity_y = 0
				self.y = self.floor
				self.jumping = False			
			self.check_bounds(4)
		elif self.y > self.floor:
			self.velocity_y -= self.gravity * 2
			self.y += self.velocity_y
		else:
			if self.key_handler[key.UP]:
				self.move_up(dt)
				return key.UP

		self.check_bounds(4)

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
			self.check_bounds(4)
		elif self.y > self.floor:
			self.velocity_y -= self.gravity * 2
			self.y += self.velocity_y
		else:
			if keys == key.UP:
				self.move_up(dt)

		self.check_bounds(4)

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