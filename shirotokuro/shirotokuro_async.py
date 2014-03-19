import pyglet, random, math, socket, connection, time, message, traceback, asyncore
from game import player, resources
import Tkinter
import tkSimpleDialog

#root = Tkinter.Tk()
#root.withdraw()
#username = tkSimpleDialog.askstring('Username', 'Enter your username')

game_window = pyglet.window.Window(1024, 600)

main_batch = pyglet.graphics.Batch()

# Initialize the player sprite
player1 = player.Player(x=30, y=50, batch=main_batch)
player2 = player.Player(x=30, y=150, batch=main_batch)
player2.set(2)

game_objects = [player1, player2]

# Tell the main window that the player object responds to events

pyglet.gl.glClearColor(0.16, 0.50, 0.72,1.0)

game_window.set_visible(False)

OK = 200
ERR = 666
QUIT = 69
WAIT = 55
PAIR = 22
UPDATE = 20

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
        print m
        player2id = m[1]
        if player2id == -1:
            time.sleep(0.1)
    print "Your partner is ", player2id
    return player2id

def init():
	global conn,s
	global playerid, player2id

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
		player2id = pair(conn, playerid, player2id)

		if playerid == 1:
			game_window.push_handlers(player1.key_handler)
		else:
			game_window.push_handlers(player2.key_handler)
	#senderthread = threading.Thread(target = sender, args = (conn, playerid, player2id,))
	#senderthread.start()

	#while True:
	#    response = conn.getMessage().replace("\\n","\n\t")
	#    print "Server: " + response
	#    if response.strip() == "":
	#        break
	#s.close()

	#headers = [1, 'Hi']
	#message = headers + ['con']
	#conn.sendMessage(message)
	#conn.sendMessage(message)
	except Exception as e:
		print "Client: Error happened! ", e
		traceback.print_exc()
		s.close()

	game_window.set_visible(True)

@game_window.event
def on_draw():
	game_window.clear()
	main_batch.draw()

def update(dt):
	if playerid == 1:
		#player2.remote_update(conn.getMessage(), dt)
		#conn.getMessage()
		keys = player1.update(dt)
		if keys != '':
			msg = [UPDATE, playerid, player2id, [], keys]
			conn.sendMessage(msg)
	else:
		#player1.remote_update(conn.getMessage(), dt)
		keys = player2.update(dt)
		if keys != '':
			msg = [UPDATE, playerid, player2id, [], keys]
			conn.sendMessage(msg)

if __name__ == "__main__":
	init()
	# Update the game 120 times per second
	pyglet.clock.schedule_interval(update, 1/120.0)
	# Tell pyglet to do its thing
	try:
		pyglet.app.run()
	except Exception as e:
		s.close()
		print e