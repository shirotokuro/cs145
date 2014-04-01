import pyglet
from resources import center_image

background = pyglet.resource.image("imgs/lvl1/bg.png")
background.height= 600
background.width= 1000

floor_mid= pyglet.resource.image("imgs/lvl1/stoneMid.png")
floor_mid.width= floor_mid.height= 40

floor = pyglet.resource.image("imgs/lvl1/stone.png")
floor.width = floor.height= 40

floor_half= pyglet.resource.image("imgs/lvl1/stoneHalf.png")
floor_half.width = floor_half.height = 40

floor_center= pyglet.resource.image("imgs/lvl1/stoneCenter.png")
floor_center.width = floor_center.height = 40

floorHalfMid= pyglet.resource.image("imgs/lvl1/stoneHalfMid.png")
floorHalfMid.width = floorHalfMid.height = 40

floorHalfLeft= pyglet.resource.image("imgs/lvl1/stoneHalfLeft.png")
floorHalfLeft.width = floorHalfLeft.height = 40

floorHalfRight= pyglet.resource.image("imgs/lvl1/stoneHalfRight.png")
floorHalfRight.width = floorHalfRight.height = 40

wht_spc= pyglet.resource.image("imgs/lvl1/white.png")
wht_spc.width= wht_spc.height= 40

blk_spc = pyglet.resource.image("imgs/lvl1/black.png")
blk_spc.width = blk_spc.height= 40

both_spc = pyglet.resource.image("imgs/lvl1/both.png")
both_spc.width = both_spc.height= 40

blkdoortop= pyglet.resource.image("imgs/greendoortop.png")
blkdoortop.width = blkdoortop.height= 40

blkdoor= pyglet.resource.image("imgs/greendoor.png")
blkdoor.width = blkdoor.height= 40

whtdoortop= pyglet.resource.image("imgs/pinkdoortop.png")
whtdoortop.width = whtdoortop.height= 40

whtdoor= pyglet.resource.image("imgs/pinkdoor.png")
whtdoor.width = whtdoor.height= 40

gemWht= pyglet.resource.image("imgs/gemPink.png")
gemWht.width = gemWht.height = 40

gemBlk= pyglet.resource.image("imgs/gemGreen.png")
gemBlk.width = gemBlk.height = 40

button= pyglet.resource.image("imgs/lvl1/button.png")
button.width= button.height= 40

elev= pyglet.resource.image("imgs/lvl1/elev.png")
elev.width= elev.height= 40
elev.anchor_y = elev.height

fireball= pyglet.resource.image("imgs/fireball.png")
fireball.width= fireball.height= 25
center_image(fireball)

border= pyglet.resource.image("imgs/lvl1/border.png")