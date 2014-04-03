import pyglet

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

# Tell pyglet where to find the resources
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

# Load the three main resources and get them to draw centered
player1_image = pyglet.resource.image("imgs/pink.png")
center_image(player1_image)

player1_left1_image = pyglet.resource.image("imgs/pright1.png").get_transform(flip_x=True)
center_image(player1_left1_image)

player1_left2_image = pyglet.resource.image("imgs/pright2.png").get_transform(flip_x=True)
center_image(player1_left2_image)

#player1_left3_image = pyglet.resource.image("imgs/pright1.png").get_transform(flip_x=True)
#center_image(player1_left3_image)

player1_right1_image = pyglet.resource.image("imgs/pright1.png")
center_image(player1_right1_image)

player1_right2_image = pyglet.resource.image("imgs/pright2.png")
center_image(player1_right2_image)

#player1_right3_image = pyglet.resource.image("imgs/pright1.png")
#center_image(player1_right3_image)

player2_image = pyglet.resource.image("imgs/green.png")
center_image(player2_image)

player2_left1_image = pyglet.resource.image("imgs/gright1.png").get_transform(flip_x=True)
center_image(player2_left1_image)

player2_left2_image = pyglet.resource.image("imgs/gright2.png").get_transform(flip_x=True)
center_image(player2_left2_image)

player2_right1_image = pyglet.resource.image("imgs/gright1.png")
center_image(player2_right1_image)

player2_right2_image = pyglet.resource.image("imgs/gright2.png")
center_image(player2_right2_image)

greendoortop= pyglet.resource.image("imgs/greendoortop.png")
greendoortop.width = greendoortop.height= 40

greendoor= pyglet.resource.image("imgs/greendoor.png")
greendoor.width = greendoor.height= 40

pinkdoortop= pyglet.resource.image("imgs/pinkdoortop.png")
pinkdoortop.width = pinkdoortop.height= 40

pinkdoor= pyglet.resource.image("imgs/pinkdoor.png")
pinkdoor.width = pinkdoor.height= 40

def right(ptype=1):
	if ptype==1:
		return player1_right1_image, player1_right2_image
	else:
		return player2_right1_image, player2_right2_image

def left(ptype=1):
	if ptype==1:
		return player1_left1_image, player1_left2_image
	else:
		return player2_left1_image, player2_left2_image
	