import pyglet
from lvl1_resources import *

lvl1= [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,13,0,0,11,0,0],
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,12,0,0,10,0,0],
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],	
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],	
	  [0,0,0,0,0,0,0,0,0,0,0,5,14,14,14,6,6,6,7,0,0,3,0,0,0],	
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],	
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,4],	
	  [1,1,1,1,1,1,1,1,1,15,15,15,1,1,16,16,16,1,1,1,4,4,4,4,4],		  	  
	  [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]]
	#0= empty				#5= stlvl1HalfLeft 		#10= blkdoor 		#15= white_spc
	#1= floor_mid			#6= stlvl1HalfMid		#11= blkdoortop 	#16= blk_spc
	#2= floor 	  			#7= stlvl1HalfRight		#12= whtdoor
	#3= floor_half			#8= gemBlk				#13= whtdoortop
	#4= floor_center		#9= gemWht				#14= both

lvl1.reverse()
def lvl1_bg():
	background.blit(0,0)

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
			elif lvl1[i][j] == 10:
				blkdoor.blit(curr_x, curr_y)
			elif lvl1[i][j] == 11:
				blkdoortop.blit(curr_x, curr_y)
			elif lvl1[i][j] == 12:
				whtdoor.blit(curr_x, curr_y)
			elif lvl1[i][j] == 13:	
				whtdoortop.blit(curr_x, curr_y)
			elif lvl1[i][j] == 14:
				both_spc.blit(curr_x, curr_y)
			elif lvl1[i][j] == 15:
				wht_spc.blit(curr_x, curr_y)
			elif lvl1[i][j] == 16: 
				blk_spc.blit(curr_x, curr_y)
			#border.blit(curr_x, curr_y)
			curr_x= curr_x+ 40
		curr_y= curr_y+40
	#lvl1_batch.draw()
