import pyglet
from game import player, resources


class GameWindow(pyglet.window.Window):
	"""docstring for GameWindow"""
	def __init__(self):
		super(GameWindow, self).__init__(1024,600)
		#Initial window states
		self.label = pyglet.text.Label('Shirotokuro')
		self.main_batch = pyglet.graphics.Batch()

		#Initialize players
		self.player1 = player.Player(x=30, y=50, batch=self.main_batch)
		self.player2 = player.Player(x=30, y=150, batch=self.main_batch)
		self.player2.set(2)

	def on_draw(self):
		pyglet.gl.glClearColor(0.16, 0.50, 0.72,1.0)
		self.clear()
		self.label.draw()
		self.main_batch.draw()

if __name__ == '__main__':
	window = GameWindow()
	pyglet.app.run()
		
