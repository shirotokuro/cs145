import pyglet
import elevator
from lvl1_resources import *
from resources import greendoortop, greendoor, pinkdoor, pinkdoortop

lvl1= [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,13,0,0,11,0,0],
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,12,0,0,10,0,0],
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,1,1,1,1,1,1,1,1,1],
	  [0,0,0,0,0,0,0,0,0,0,5,7,0,0,0,0,0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,17,0,0,0,0,0,0,0,5,6,7,0,0,0,0,0,0,0,0],
	  [0,0,5,6,6,6,6,6,6,6,6,6,6,7,0,0,0,0,0,0,0,0,0,0,0],
	  [19,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],	
	  [19,0,0,0,0,17,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0],	
	  [6,6,6,6,6,6,6,7,0,0,0,5,14,14,14,6,6,6,7,0,0,3,0,0,9],	
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],	
	  [0,9,0,0,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,4],	
	  [1,1,1,1,1,1,1,1,1,15,15,15,1,1,16,16,16,1,1,1,4,4,4,4,4],		  	  
	  [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]]
	#0= empty				#5= stlvl1HalfLeft 		#10= greendoor 		#15= white_spc
	#1= floor_mid			#6= stlvl1HalfMid		#11= greendoortop 	#16= wave_green
	#2= floor 	  			#7= stlvl1HalfRight		#12= pinkdoor 		#17= button
	#3= floor_half			#8= gemBlk				#13= pinkdoortop 	#18= door
	#4= floor_center		#9= gemWht				#14= both 			#19= elev

lvl1_batch = pyglet.graphics.Batch()

lvl1.reverse()
elevator= elevator.Elevator(x= 0, y= 240, batch= lvl1_batch)

wave_panim = pyglet.image.Animation.from_image_sequence([
			wave_pink1, wave_pink2], 0.4, True)
wave_pink_sprite1 = pyglet.sprite.Sprite(img=wave_panim, x= 360, y= 40, batch= lvl1_batch)
wave_pink_sprite2 = pyglet.sprite.Sprite(img=wave_panim, x= 400, y= 40, batch= lvl1_batch)
wave_pink_sprite3 = pyglet.sprite.Sprite(img=wave_panim, x= 440, y= 40, batch= lvl1_batch)

wave_ganim = pyglet.image.Animation.from_image_sequence([
			wave_green1, wave_green2], 0.4, True)
wave_green_sprite1 = pyglet.sprite.Sprite(img=wave_ganim, x= 560, y= 40, batch= lvl1_batch)
wave_green_sprite2 = pyglet.sprite.Sprite(img=wave_ganim, x= 600, y= 40, batch= lvl1_batch)
wave_green_sprite3 = pyglet.sprite.Sprite(img=wave_ganim, x= 640, y= 40, batch= lvl1_batch)

wave_banim = pyglet.image.Animation.from_image_sequence([
			wave_blue1, wave_blue2], 0.4, True)

wave_blue_sprite1 = pyglet.sprite.Sprite(img=wave_banim, x= 480, y= 160, batch= lvl1_batch)
wave_blue_sprite2 = pyglet.sprite.Sprite(img=wave_banim, x= 520, y= 160, batch= lvl1_batch)
wave_blue_sprite3 = pyglet.sprite.Sprite(img=wave_banim, x= 560, y= 160, batch= lvl1_batch)



def lvl1_bg():

	curr_y= 0
	for i in range(0, len(lvl1)):
		curr_x= 0
		for j in range(0, len(lvl1[i])):
			if lvl1[i][j] == 1:
				floor_mid.blit(curr_x, curr_y)
			elif lvl1[i][j] == 2: 
				floor.blit(curr_x, curr_y)
			elif lvl1[i][j] == 3:
				floor_half.blit(curr_x, curr_y)
			elif lvl1[i][j] == 4:
				floor_center.blit(curr_x, curr_y)
			elif lvl1[i][j] == 5:
				floorHalfLeft.blit(curr_x, curr_y)
			elif lvl1[i][j] == 6:
				floorHalfMid.blit(curr_x, curr_y)
			elif lvl1[i][j] == 7:	
				floorHalfRight.blit(curr_x, curr_y)
			elif lvl1[i][j] == 8:	
				gemBlk.blit(curr_x, curr_y)	
			elif lvl1[i][j] == 9:	
				gemWht.blit(curr_x, curr_y)		
			elif lvl1[i][j] == 10:
				greendoor.blit(curr_x, curr_y)
			elif lvl1[i][j] == 11:
				greendoortop.blit(curr_x, curr_y)
			elif lvl1[i][j] == 12:
				pinkdoor.blit(curr_x, curr_y)
			elif lvl1[i][j] == 13:	
				pinkdoortop.blit(curr_x, curr_y)
			elif lvl1[i][j] == 17: 
				button.blit(curr_x, curr_y)
			curr_x= curr_x+ 40
		curr_y= curr_y+40
	elevator.update()
	lvl1_batch.draw()
