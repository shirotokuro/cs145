import pyglet, random, math, socket, connection, time, message, traceback, asyncore, threading
from game import player, resources, lvl1
from pyglet.gl import *

#root = Tkinter.Tk()
#root.withdraw()
#username = tkSimpleDialog.askstring('Username', 'Enter your username')

game_window = pyglet.window.Window(1000, 600)

main_batch = pyglet.graphics.Batch()

# Initialize the player sprite
player1 = player.Player(lvl= lvl1.lvl1,x=105, y=105, batch=main_batch)
player2 = player.Player(lvl= lvl1.lvl1,x=55, y=105, batch=main_batch)
player2.set(2)

game_over_label = pyglet.text.Label(text="GAME OVER",
                                    x=2000, y=300, anchor_x='center', 
                                    font_size=48, bold= True, color=(236, 188, 175, 255),batch=main_batch)

game_objects = [player1, player2]

# Tell the main window that the player object responds to events

#glClearColor(0.16, 0.50, 0.72,1.0)

game_window.set_visible(False)

OK = 200
ERR = 666
QUIT = 69
WAIT = 55
PAIR = 22
UPDATE = 20

def p2_update(conn,s):
	while True:
		try:
			msg = conn.getMessage()
			if msg == QUIT:
				print "Sorry your partner quit. Exiting..."
				s.close()
			else:
				player_dead = False
				for obj in game_objects:
					#obj.update(0)
					if obj.dead:
						player_dead= True
				if player_dead:
					player1.delete()
					player2.delete()
					game_over_label.x=500
					game_objects.remove(player1)
					game_objects.remove(player2)
				if len(game_objects) > 0:
					if playertype == 1:
						player2.remote_update(msg, 0)
					else:
						player1.remote_update(msg, 0)
		except Exception, e:
			try:
				s.close()
			except Exception, e:
				'dsa'
		

def confirm(conn, playerid):
    while playerid == -1:
        message = conn.getMessage()
        if message[0] == 0:
            playerid = message[1]
            print "Your playerid is ", playerid
    return playerid

def pair(conn, playerid, player2id):
    print 'waiting...'
    while player2id == -1:
        msg = [WAIT, playerid, player2id, [], '']
        conn.sendMessage(msg)
        m = conn.getMessage()
        player2id = m[1]
        if player2id == -1:
            time.sleep(0.01)
    print "Your partner is ", player2id
    print "Your playertype is ", m[2]

    return player2id, m[2]

def init():
	global conn,s
	global playerid, player2id, playertype

	playerid = -1
	player2id = -1

	try:
		host = '127.0.0.1'
		port = 7667
		s = socket.socket()

		print "Client tries to connect to server..."
		s.connect((host, port)) 

		print "Client connected!"

		conn = connection.connection(s) 
		playerid = confirm(conn, playerid)
		player2id,playertype = pair(conn, playerid, player2id)

		if playertype == 1:
			game_window.push_handlers(player1.key_handler)
		else:
			game_window.push_handlers(player2.key_handler)
	except (KeyboardInterrupt, SystemExit):
		conn.sendMessage([QUIT,playerid, player2id, [], ''])
		s.close()
		print 'dasda'
	except Exception as e:
		print "Client: Error happened! ", e
		traceback.print_exc()
		conn.sendMessage([QUIT,playerid, player2id, [], keys])
		s.close()

	game_window.set_visible(True)

@game_window.event
def on_draw():
	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	lvl1.lvl1_bg()
	main_batch.draw()

def update(dt):
	player_dead = False
	for obj in game_objects:
		#obj.update(dt)
		if obj.dead:
			player_dead= True
	if player_dead:
		player1.delete()
		player2.delete()
		game_over_label.x=500
		game_objects.remove(player1)
		game_objects.remove(player2)
	if len(game_objects) > 0:
		if playertype == 1:
			keys = player1.update(dt)
			conn.sendMessage([UPDATE, playerid, player2id, [], keys])
		else:
			keys = player2.update(dt)
			conn.sendMessage([UPDATE, playerid, player2id, [], keys])

if __name__ == "__main__":
	global conn,s
	
	# Tell pyglet to do its thing
	try:
		init()
		
		# Update the game 120 times per second
		pyglet.clock.schedule_interval(update, 1/120.0)
		updater = threading.Thread(target=p2_update, args=(conn,s,))
		updater.daemon =True
		updater.start()
		pyglet.app.run()
	except (KeyboardInterrupt, SystemExit):
		try:	
			conn.sendMessage([QUIT,playerid, player2id, [], ''])
			s.close()
		except Exception, e:
			print 'dasda'
	except Exception as e:
		try:
			conn.sendMessage([QUIT,playerid, player2id, [], ''])
			s.close()
		except socket.error as error:

			print error
		#	print 'Server error!'
		except Exception, e:
			sher = 1