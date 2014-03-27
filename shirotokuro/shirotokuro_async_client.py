import pyglet, random, math, socket, connection, time, message, traceback, asyncore, threading, thread
from game import player, resources, lvl1
import gamewindow
from pyglet.window import key
from pyglet.window import mouse
from pyglet.gl import *

OK = 200
ERR = 666
QUIT = 69
WAIT = 55
PAIR = 22
UPDATE = 20
ORPHAN = 1

window = pyglet.window.Window(1000, 600)


game_window = gamewindow.GameWindow()
game_menu_label = pyglet.text.Label(text="CLICK ANYWHERE TO START!",
                                    x=500, y=300, anchor_x='center', 
                                    font_size=40, bold= True, color=(236, 188, 175, 255))

menu = True

@window.event
def on_mouse_press(x, y, button, modifiers):
	global menu, conn
	if button == mouse.LEFT:
		print 'The left mouse button was pressed.'
		if menu:

			game_start()
			
			
			pyglet.clock.schedule_interval(update, 1/120.0)
			e.set()
			menu = False

			@window.event
			def on_close():
				print 'Bye!'
				try:
					e.clear()
					conn.sendMessage([QUIT,playerid, player2id, [], ''])
					s.close()
					pyglet.clock.unschedule(update)
				except Exception,err:
					print err
					e.clear()
					pyglet.clock.unschedule(update)
		else:
			menu = True

@window.event
def on_draw():
	global menu

	try:
		if menu:
			window.clear()
			game_menu_label.draw()
		else:
			window.clear()
			glEnable(GL_BLEND)
			glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
			lvl1.lvl1_bg()
			game_window.main_batch.draw()
	except Exception, e:
		print e
		fuck_given = 0

def p2_update(conn,s,e):
	global menu
	while True:
		e.wait()
		print 'dasdsa'
		try:
			msg = conn.getMessage()
			if msg == QUIT:
				e.clear()
				conn.sendMessage([ORPHAN,playerid, player2id, [], ''])
				print "Sorry your partner quit."
				pyglet.clock.unschedule(update)
				reset()
				menu = True
			else:
				if len(game_window.game_objects) > 0:
					if playertype == 1:
						game_window.player2.remote_update(msg, 0)
					else:
						game_window.player1.remote_update(msg, 0)
				
				player_dead = False
				
				for obj in game_window.game_objects:
					if obj.dead:
						player_dead= True
				
				if msg=='G.O.':
					game_window.game_over()

		except Exception, err:
			print err
			e.clear()

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

	host = '127.0.0.1'
	port = 7667
	s = socket.socket()

	print "Client tries to connect to server..."
	s.connect((host, port)) 

	print "Client connected!"

	conn = connection.connection(s) 

def reset():
	global conn,s
	global playerid, player2id, game_window, playertype

	playerid = -1
	player2id = -1
	playertype = -1

def game_start():
	global conn,s
	global playerid, player2id, game_window, playertype 

	playerid = -1
	player2id = -1
	playertype = -1

	playerid = confirm(conn, playerid)
	player2id,playertype = pair(conn, playerid, player2id)

	game_window = gamewindow.GameWindow()

	if playertype == 1:
		window.push_handlers(game_window.player1.key_handler)
	else:
		window.push_handlers(game_window.player2.key_handler)

def update(dt):
	
	if len(game_window.game_objects) > 0:
		
		if playertype == 1:
			keys = game_window.player1.update(dt)
			conn.sendMessage([UPDATE, playerid, player2id, [], keys])
		else:
			keys = game_window.player2.update(dt)
			conn.sendMessage([UPDATE, playerid, player2id, [], keys])
	
	player_dead = False
	for obj in game_window.game_objects:
		if obj.dead:
			player_dead= True
	
	if player_dead:
		conn.sendMessage([UPDATE,playerid, player2id, [], 'G.O.'])
		game_window.game_over()

if __name__ == "__main__":
	global conn,s
	
	init()

	e = threading.Event()
			
	updater = threading.Thread(target=p2_update, args=(conn,s,e,))
	updater.daemon =True
	updater.start()

	e.clear()

	try:	
		pyglet.app.run()
	
	except (KeyboardInterrupt, SystemExit):
		try:	
			conn.sendMessage([QUIT,playerid, player2id, [], ''])
			s.close()
		except Exception, e:
			print 'Connection not made.'
	
	except socket.error as error:
		traceback.print_exc()
		print 'Socket error!'
	
	except Exception as e:
		#conn.sendMessage([QUIT,playerid, player2id, [], ''])
		#s.close()
		traceback.print_exc()
		print 'Other error!'