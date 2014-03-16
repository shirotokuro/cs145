import pyglet

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

# Tell pyglet where to find the resources
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

# Load the three main resources and get them to draw centered
player1_image = pyglet.resource.image("imgs/white.png")
center_image(player1_image)

player1_left1_image = pyglet.resource.image("imgs/wleft1.png")
center_image(player1_left1_image)

player1_left2_image = pyglet.resource.image("imgs/wleft2.png")
center_image(player1_left2_image)

player1_left3_image = pyglet.resource.image("imgs/wleft3.png")
center_image(player1_left3_image)

player1_right1_image = pyglet.resource.image("imgs/wright1.png")
center_image(player1_right1_image)

player1_right2_image = pyglet.resource.image("imgs/wright2.png")
center_image(player1_right2_image)

player1_right3_image = pyglet.resource.image("imgs/wright3.png")
center_image(player1_right3_image)

player2_image = pyglet.resource.image("imgs/black.png")
center_image(player2_image)

player2_left1_image = pyglet.resource.image("imgs/bleft1.png")
center_image(player2_left1_image)

player2_left2_image = pyglet.resource.image("imgs/bleft2.png")
center_image(player2_left2_image)

player2_left3_image = pyglet.resource.image("imgs/bleft3.png")
center_image(player2_left3_image)

player2_right1_image = pyglet.resource.image("imgs/bright1.png")
center_image(player2_right1_image)

player2_right2_image = pyglet.resource.image("imgs/bright2.png")
center_image(player2_right2_image)

player2_right3_image = pyglet.resource.image("imgs/bright3.png")
center_image(player2_right3_image)

def right(ptype=1):
	if ptype==1:
		return player1_right1_image, player1_right2_image, player1_right3_image
	else:
		return player2_right1_image, player2_right2_image, player2_right3_image

def left(ptype=1):
	if ptype==1:
		return player1_left1_image, player1_left2_image, player1_left3_image
	else:
		return player2_left1_image, player2_left2_image, player2_left3_image
	