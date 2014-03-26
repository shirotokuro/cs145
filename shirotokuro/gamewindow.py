import pyglet
from game import player, resources, lvl1
from pyglet.gl import *

class GameWindow(pyglet.window.Window):
	"""docstring for GameWindow"""
	def __init__(self):
		super(GameWindow, self).__init__(1000,600)
		#Initial window states
		
		self.main_batch = pyglet.graphics.Batch()

		#Initialize players
		self.player1 = player.Player(lvl= lvl1.lvl1,x=105, y=105, batch=self.main_batch)
		self.player2 = player.Player(lvl= lvl1.lvl1,x=55, y=105,batch=self.main_batch)
		self.player2.set(2)

		self.game_over_label = pyglet.text.Label(text="GAME OVER",
                                    x=2000, y=300, anchor_x='center', 
                                    font_size=48, bold= True, color=(236, 188, 175, 255),batch=self.main_batch)

		self.game_objects = [self.player1, self.player2]

	def on_draw(self):
		try:
			glEnable(GL_BLEND)
			glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
			lvl1.lvl1_bg()
			self.main_batch.draw()
		except Exception, e:
			fuck_given = 0

	def game_over(self):
		self.player1.delete()
		self.player2.delete()
		self.game_over_label.x=500
		self.game_objects.remove(self.player1)
		self.game_objects.remove(self.player2)

if __name__ == '__main__':
	window = GameWindow()
	pyglet.app.run()
		
