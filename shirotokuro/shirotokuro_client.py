import pyglet, random, math, socket, connection
from game import player, resources

game_window = pyglet.window.Window(1024, 600)

main_batch = pyglet.graphics.Batch()

# Initialize the player sprite
player1 = player.Player(x=30, y=50, batch=main_batch)
player2 = player.Player(x=30, y=150, batch=main_batch)
player2.set(2)

game_objects = [player1, player2]

# Tell the main window that the player object responds to events

game_window.push_handlers(player2.key_handler)
pyglet.gl.glClearColor(0.16, 0.50, 0.72,1.0)

def init():
	global conn
	global clientsocket

	clientsocket = socket.socket()

	clientsocket.connect(('127.0.0.1', 8888))
	conn = connection.connection(clientsocket)

@game_window.event
def on_draw():
	game_window.clear()
	main_batch.draw()

def update(dt):
	keys = player2.update(dt)
	conn.sendMessage(keys)
	player1.remote_update(conn.getMessage(), dt)

if __name__ == "__main__":
	init()
	# Update the game 120 times per second
	pyglet.clock.schedule_interval(update, 1/120.0)

	# Tell pyglet to do its thing
	try:
		pyglet.app.run()
	except Exception as e:
		clientsocket.close()
		print e
