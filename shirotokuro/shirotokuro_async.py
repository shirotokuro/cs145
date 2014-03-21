import pyglet, random, math, socket, connection, time, message, traceback, asyncore, threading
from game import player, resources
import gamewindow

#root = Tkinter.Tk()
#root.withdraw()
#username = tkSimpleDialog.askstring('Username', 'Enter your username')

#game_window = pyglet.window.Window(1024, 600)

#main_batch = pyglet.graphics.Batch()

# Initialize the player sprite
#player1 = player.Player(x=30, y=50, batch=main_batch)
#player2 = player.Player(x=30, y=150, batch=main_batch)
#player2.set(2)

#game_objects = [player1, player2]

# Tell the main window that the player object responds to events

#pyglet.gl.glClearColor(0.16, 0.50, 0.72,1.0)

#game_window.set_visible(False)

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
			elif playertype == 1:
				game_window.player2.remote_update(msg, 0)
			else:
				game_window.player1.remote_update(msg, 0)
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
	global playerid, player2id, game_window, playertype

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
		game_window = gamewindow.GameWindow()

		if playertype == 1:
			game_window.push_handlers(game_window.player1.key_handler)
		else:
			game_window.push_handlers(game_window.player2.key_handler)
	except (KeyboardInterrupt, SystemExit):
		conn.sendMessage([QUIT,playerid, player2id, [], ''])
		s.close()
		print 'dasda'
	except Exception as e:
		print "Client: Error happened! ", e
		traceback.print_exc()
		conn.sendMessage([QUIT,playerid, player2id, [], keys])
		s.close()
def update(dt):

	if playertype == 1:
		keys = game_window.player1.update(dt)
	else:
		keys = game_window.player2.update(dt)

	conn.sendMessage([UPDATE, playerid, player2id, [], keys])

if __name__ == "__main__":
	global conn,s
	init()
	# Update the game 120 times per second
	pyglet.clock.schedule_interval(update, 1/120.0)
	updater = threading.Thread(target=p2_update, args=(conn,s,))
	updater.daemon =True
	updater.start()
	# Tell pyglet to do its thing
	try:
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
			print 'Server error!'
		except Exception, e:
			sher = 1