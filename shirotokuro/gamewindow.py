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
		self.player1 = player.Player(lvl= lvl1.lvl1,x=105, y=105, batch=self.main_batch)
		self.player2 = player.Player(lvl= lvl1.lvl1,x=55, y=105,batch=self.main_batch)
		self.player2.set(2)

		game_over_label = pyglet.text.Label(text="GAME OVER",
                                    x=2000, y=300, anchor_x='center', 
                                    font_size=48, bold= True, color=(236, 188, 175, 255),batch=main_batch)


	def on_draw(self):
		pyglet.gl.glClearColor(0.16, 0.50, 0.72,1.0)
		self.clear()
		self.label.draw()
		self.main_batch.draw()

if __name__ == '__main__':
	window = GameWindow()
	pyglet.app.run()
		
