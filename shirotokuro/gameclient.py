import pyglet, random, math, socket, connection, time, message, traceback, asyncore, threading
from game import player, resources
import gamewindow

class GameClient():
	def __init__(self):
		#super(GameClient, self).__init__()
		#self.arg = arg
		self.playerid = -1
		self.player2id = -1

		try:
			self.server_host = '127.0.0.1'
			self.server_port = 7667
			self.client_socket = socket.socket()

			print "Client tries to connect to server..."
			self.client_socket.connect((server_host, server_port))

			print "Connected!"

			self.conn = connection.connection(client_socket)
			
			self.confirm()
			self.pair()
			self.game_window = gamewindow.GameWindow()

			if playerid == 1:
				self.game_window.push_handlers(game_window.player1.key_handler)
			else:
				self.game_window.push_handlers(game_window.player2.key_handler)

		except Exception, e:
			conn.sendMessage([QUIT,playerid, player2id, [], ''])
			s.close()
			print 'dasda'

	def confirm(self):
		while self.playerid == -1:
			message = self.conn.getMessage()
			if message[0] == 0:
				self.playerid = message[1]
				print "Your playerid is ", self.playerid

	def pair():
		print 'waiting...'
		while self.player2id == -1:
			msg = [WAIT, self.playerid, self.player2id, [], '']
			conn.sendMessage(msg)
			m = conn.getMessage()
			self.player2id = m[1]
			if self.player2id == -1:
				time.sleep(0.01)
		print "Your partner is ", self.player2id

	def update(dt):
		if self.playerid == 1:
			keys = self.game_window.player1.update(dt)
		else:
			keys = self.game_window.player2.update(dt)

		conn.sendMessage([UPDATE, self.playerid, self.player2id, [], keys])
