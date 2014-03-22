import pyglet, random, math, socket, connection, time, message, traceback, asyncore, threading
from game import player, resources
import gamewindow

OK = 200
ERR = 666
QUIT = 69
WAIT = 55
PAIR = 22
UPDATE = 20

class GameClient():
	def __init__(self):
		#super(GameClient, self).__init__()
		#self.arg = arg
		self.playerid = -1
		self.player2id = -1
		self.playertype = -1
		
		self.server_host = '127.0.0.1'
		self.server_port = 7667
		self.client_socket = socket.socket()

		print "Client tries to connect to server..."
		self.client_socket.connect((self.server_host, self.server_port))

		print "Connected!"

		self.conn = connection.connection(self.client_socket)
		
		self.confirm()
		self.pair()
		self.game_window = gamewindow.GameWindow()

		if self.playerid == 1:
			self.game_window.push_handlers(self.game_window.player1.key_handler)
		else:
			self.game_window.push_handlers(self.game_window.player2.key_handler)

		self.updater = threading.Thread(target=self.p2_update, args=())
		self.updater.daemon =True
		pyglet.clock.schedule_interval(self.update, 1/120.0)
		self.updater.start()

	def confirm(self):
		while self.playerid == -1:
			message = self.conn.getMessage()
			if message[0] == 0:
				self.playerid = message[1]
				print "Your playerid is ", self.playerid

	def pair(self):
		print 'waiting...'
		while self.player2id == -1:
			msg = [WAIT, self.playerid, self.player2id, [], '']
			self.conn.sendMessage(msg)
			m = self.conn.getMessage()
			self.player2id = m[1]
			if self.player2id == -1:
				time.sleep(0.01)
		self.playertype = m[2]
	

	def update(self,dt):
		if self.playertype == 1:
			keys = self.game_window.player1.update(dt)
		else:
			keys = self.game_window.player2.update(dt)

		self.conn.sendMessage([UPDATE, self.playerid, self.player2id, [], keys])

	def p2_update(self):
		while True:
			try:
				msg = self.conn.getMessage()
				if msg == QUIT:
					print "Sorry your partner quit. Exiting..."
					s.close()
				elif self.playertype == 1:
					self.game_window.player2.remote_update(msg, 0)
				else:
					self.game_window.player1.remote_update(msg, 0)
			except Exception, e:
				try:
					s.close()
				except Exception, e:
					'dsa'

if __name__ == '__main__':
	client = GameClient()
	pyglet.app.run()