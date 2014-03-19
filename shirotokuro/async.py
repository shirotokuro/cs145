import asyncore
import socket
import sys
import pickle
import message
import random

LOCAL_HOST = 'localhost'
LOCAL_PORT = 7668
REMOTE_HOST = 'localhost'
REMOTE_PORT = 7667

OK = 200
ERR = 666
QUIT = 69
WAIT = 55
PAIR = 22
UPDATE = 20



### SERVER ###

class ChatHandler(asyncore.dispatcher):
    def __init__(self, sock, map, server):
        self.server = server
        self.buffer = ''
        asyncore.dispatcher.__init__(self, sock, map)

    def writable(self):
        return len(self.buffer) > 0

    def readable(self):
        return True

    def handle_read(self):
        """Notify server of any new incoming data"""
        data = self.recv(1024)
        if data != '\n':
            self.server.newMessage(data, self)

    def handle_write(self):
        """send some amount of buffer"""
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]

class ChatServer(asyncore.dispatcher):
    """Receive and forward chat messages

    When a new connection is made we spawn a dispatcher for that
    connection.
    """
    ADDRESS_FAMILY = socket.AF_INET
    SOCKET_TYPE = socket.SOCK_STREAM
    
    def __init__(self, host=REMOTE_HOST, port=REMOTE_PORT):
        self.map = {}
        self.address = (host,port)
        self.clients = []
        self.clientids = []
        self.buffer = ''
        self.clientid = 1
       
        self.availclients = []
        self.paired = []
        asyncore.dispatcher.__init__(self, map=self.map)

    def serve(self):
        """Bind to socket and start asynchronous loop"""
        self.create_socket(self.ADDRESS_FAMILY, self.SOCKET_TYPE)
        self.bind(self.address)
        self.listen(1)
        asyncore.loop(map=self.map)

    def writable(self):
        return False

    def readable(self):
        return True

    def checkpid(self, pid):
        try:
            print self.availclients
            if len(self.availclients) != 1:
                p2 = -1
                while p2 != -1 and p2 != pid:
                    p2 = random.choice(p2)
                    print p2
                return p2
            else:
                return -1
        except Exception, e:
            print e

    def pair(self, pid):
        if self.clientid > 2:
            if pid == 1:
                return 2
            else:
                return 1
        else:
            return -1

    def newMessage(self, data, fromWho):
        """Put data in all clients' buffers"""
        self.buffer = data
        #print "#", self.buffer
        data = pickle.loads(data)
        #print data
        m = message.Message(data)
        
        if m.type == WAIT:
            #try:
             #   i = self.availclients.index(m.pid)
            #except Exception, e:
            #    self.availclients = self.availclients + [m.pid]
            
            available = self.pair(m.pid)
            if available != -1:
                self.paired = self.paired + [m.pid]
                self.paired = self.paired + [available]
            msg = [PAIR, available]
            msg = pickle.dumps(msg)
            self.clients[self.clientids.index(m.pid)].buffer += msg
        if m.type == UPDATE:
           # print m.msg
            self.clients[m.p2id - 1].buffer += pickle.dumps(m.msg)



    def handle_accept(self):
        """Deal with newly accepted connection"""
        print 'got new connection'
        
        (connSock, clientAddress) = self.accept()
        client = ChatHandler(connSock, self.map, self)
        self.clients.append(client)
        player_details = [0, self.clientid]
        client.send(pickle.dumps(player_details))
        self.clientids = self.clientids + [self.clientid]
        self.clientid += 1

c = ChatServer()
c.serve()