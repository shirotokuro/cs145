import pyglet, random, math, socket, connection, time
from game import player, resources

OK = 200
ERR = 666
QUIT = 69
WAIT = 55
PAIR = 22
UPDATE = 20

game_window = pyglet.window.Window(1024, 600)

main_batch = pyglet.graphics.Batch()

# Initialize the player sprite
player1 = player.Player(x=30, y=50, batch=main_batch)
player2 = player.Player(x=30, y=150, batch=main_batch)
player2.set(2)

playerid = -1
player2id = -1

game_objects = [player1, player2]

# Tell the main window that the player object responds to events

pyglet.gl.glClearColor(0.16, 0.50, 0.72,1.0)


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
        msg = [WAIT, playerid, player2id, '']
        conn.sendMessage(msg)
        m = conn.getMessage()
        player2id = m[1]
        print m
        if player2id == -1:
            time.sleep(1)
    print "Your partner is ", player2id
    pyglet.clock.schedule_interval(update, 1/120.0)
    return player2id

def init():
	global playerid,player2id,conn

	try:
		host = '127.0.0.1'
		port = 7667
		s = socket.socket()

		print "Client tries to connect to server..."
		s.connect((host, port)) 

		print "Client connected!"

		conn = connection.connection(s) 
		playerid = confirm(conn, playerid)
		player2id = pair(conn, playerid, player2id)
		if playerid == 1:
			game_window.push_handlers(player1.key_handler)
		else:
			game_window.push_handlers(player2.key_handler)
	except Exception as e:
		print "Client: Error happened! ", e
		s.close()

@game_window.event
def on_draw():
	game_window.clear()
	main_batch.draw()

def update(dt):
	#msg = conn.getMessage
	#if msg != '##w@1t##':
	#	player1.remote_update(conn.getMessage(), dt)
	#else:
	#	print "Please wait while your partner connects"
	
	#keys = player2.update(dt)
	#conn.sendMessage(keys)
	if playerid == 1:
		player2.remote_update(conn.getMessage(), dt)
		keys = player1.update(dt)
		msg = [UPDATE, playerid, player2id, [], keys]
		conn.sendMessage(keys)
	else:
		player1.remote_update(conn.getMessage(), dt)
		keys = player2.update(dt)
		msg = [UPDATE, playerid, player2id, [], keys]
		conn.sendMessage(keys)
	print 'coco'

if __name__ == "__main__":
	init()
	# Update the game 120 times per second
	# Tell pyglet to do its thing
	try:
		pyglet.app.run()
	except Exception as e:
		clientsocket.close()
		print e
