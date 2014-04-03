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

wave_pink1= pyglet.resource.image("imgs/lvl1/pink_wave.png")
wave_pink1.width= wave_pink1.height= 40

wave_pink2= pyglet.resource.image("imgs/lvl1/pink_wave2.png")
wave_pink2.width= wave_pink2.height= 40

wave_green1 = pyglet.resource.image("imgs/lvl1/green_wave.png")
wave_green1.width = wave_green1.height= 40

wave_green2 = pyglet.resource.image("imgs/lvl1/green_wave2.png")
wave_green2.width = wave_green2.height= 40

wave_blue1 = pyglet.resource.image("imgs/lvl1/blue_wave.png")
wave_blue1.width = wave_blue1.height= 40

wave_blue2 = pyglet.resource.image("imgs/lvl1/blue_wave2.png")
wave_blue2.width = wave_blue2.height= 40

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