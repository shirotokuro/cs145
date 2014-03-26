import pyglet, random, math, socket, connection, time, message, traceback, asyncore, threading, thread
from game import player, resources
import gamewindow

OK = 200
ERR = 666
QUIT = 69
WAIT = 55
PAIR = 22
UPDATE = 20

def p2_update(conn,s,e):
	while True:
		e.wait()
		try:
			msg = conn.getMessage()
			if msg == QUIT:
				e.clear()
				conn.sendMessage([QUIT,playerid, player2id, [], ''])
				print "Sorry your partner quit. Exiting..."
				game_window.close()
				pyglet.clock.unschedule(update)
				print 'Bye!'
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
	playerid = confirm(conn, playerid)
	player2id,playertype = pair(conn, playerid, player2id)
	game_window = gamewindow.GameWindow()

	if playertype == 1:
		game_window.push_handlers(game_window.player1.key_handler)
	else:
		game_window.push_handlers(game_window.player2.key_handler)

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
	
	e = threading.Event()

	try:
		init()

		updater = threading.Thread(target=p2_update, args=(conn,s,e,))
		updater.daemon =True
		updater.start()
		
		e.set()
		
		pyglet.clock.schedule_interval(update, 1/120.0)

		@game_window.event
		def on_close():
			global e
			print 'Bye!'
			#e.clear()
			try:
				e.clear()
				conn.sendMessage([QUIT,playerid, player2id, [], ''])
				s.close()
				pyglet.clock.unschedule(update)
			except Exception,e:
				e.clear()
				pyglet.clock.unschedule(update)
			
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
		conn.sendMessage([QUIT,playerid, player2id, [], ''])
		s.close()
		traceback.print_exc()
		print 'Other error!'