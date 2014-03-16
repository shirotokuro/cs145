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

game_window.push_handlers(player1.key_handler)
pyglet.gl.glClearColor(0.16, 0.50, 0.72,1.0)

def init():
	global conn

	serversocket = socket.socket()

	host = ''
	serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	serversocket.bind((host, 8888))

	print 'Server ready. . .'

	serversocket.listen(5)

	remote_socket, remote_address = serversocket.accept()
	print 'Got connection from ', remote_address

	conn = connection.connection(remote_socket)

@game_window.event
def on_draw():
	game_window.clear()
	main_batch.draw()

def update(dt):
	conn.sendMessage(player1.update(dt))
	player2.remote_update(conn.getMessage(), dt)

if __name__ == "__main__":
	init()
	# Update the game 120 times per second
	pyglet.clock.schedule_interval(update, 1/120.0)

	# Tell pyglet to do its thing
	pyglet.app.run()
