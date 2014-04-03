import pyglet, fire
from lvl2_resources import *
from resources import greendoortop, greendoor, pinkdoor, pinkdoortop

lvl2= [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],	
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	  [5,6,4,5,6,6,5,4,5,6,4,5,6,6,4,4,4,6,5,5,5,4,5,0,0],
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],	
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	  [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1]]
'''
		1= pink_floor		4= pink_half
	  	2= green_floor		5= green_half
	  	3= blue_floor 		6= blue_half
'''

lvl2.reverse()

def lvl2_bg():

	curr_y= 0
	for i in range(0, len(lvl2)):
		curr_x= 0
		for j in range(0, len(lvl2[i])):
			if lvl2[i][j] == 1:
				pink_floor.blit(curr_x, curr_y)
			elif lvl2[i][j] == 2: 
				green_floor.blit(curr_x, curr_y)
			elif lvl2[i][j] == 3:
				blue_floor.blit(curr_x, curr_y)
			elif lvl2[i][j] == 4:
				pink_half.blit(curr_x, curr_y)
			elif lvl2[i][j] == 5:
				green_half.blit(curr_x, curr_y)
			elif lvl2[i][j] == 6:
				blue_half.blit(curr_x, curr_y)
			curr_x= curr_x+ 40
		curr_y= curr_y+40