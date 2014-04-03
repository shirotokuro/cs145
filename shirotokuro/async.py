import asyncore
import socket
import sys
import pickle
import message
import random
from multiprocessing import Lock

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
READY = 5
ORPHAN = 1



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
        data = self.recv(2048)
        if data != '\n':
            try:
                self.server.newMessage(data, self)
            except Exception, e:
                fuck_given = 0

    def handle_write(self):
        """send some amount of buffer"""
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]

    def handle_close(self):
        self.close()


    #def handle_error(self):
        #print 'heloooo'
        #self.close()

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
        self.lock = Lock()
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
            #print len(self.availclients)
            if len(self.availclients) != 1:
                p2 = -1
                print p2
                while p2 == -1 or p2 == pid:
                    p2 = self.availclients.pop()
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
    
        m = message.Message(data)
        k = m.type
        if m.type == WAIT:
            self.lock.acquire()
            try:
                i = self.paired.index(m.pid)
                if i % 2 == 0:
                    msg = [PAIR, self.paired[i+1], 1]
                    msg = pickle.dumps(msg)
                    self.clients[self.clientids.index(m.pid)].buffer += msg
                else:
                    msg = [PAIR, self.paired[i-1], 2]
                    msg = pickle.dumps(msg)
                    self.clients[self.clientids.index(m.pid)].buffer += msg
                
                try:
                    self.availclients.remove(m.pid)
                except Exception, e:
                    self.availclients.remove(m.p2id)
                finally:
                    msg = [PAIR, self.paired.index(self.paired.index(m.pid))+1, 1]
                    msg = pickle.dumps(msg)
                    self.clients[self.clientids.index(m.pid)].buffer += msg  
               
            except Exception, e:
                try:
                   i = self.availclients.index(m.pid)
                except Exception, e:
                    self.availclients = self.availclients + [m.pid]
                
                available = self.checkpid(m.pid)

                if available != -1:
                    self.paired = self.paired + [m.pid]
                    self.paired = self.paired + [available]

                    print self.paired

                msg = [PAIR, -1, 2]
                msg = pickle.dumps(msg)
                self.clients[self.clientids.index(m.pid)].buffer += msg
            self.lock.release()

                
        elif m.type == UPDATE:
            self.clients[m.p2id - 1].buffer += pickle.dumps(m.msg)
        
        elif m.type == QUIT:
            self.lock.acquire()
            try:
                self.paired.remove(m.pid)
                self.paired.remove(m.p2id)
                self.clients[self.clientids.index(m.p2id)].buffer += pickle.dumps(QUIT)
            except Exception, e:
                fuck_given = 0
            self.lock.release()
           
            self.clients[self.clientids.index(m.pid)].close()
       
        elif m.type == READY:
            self.lock.acquire()
            try:
                self.availclients.remove(m.pid)
            except Exception, e:
                fuck_given = 0
            self.lock.release()
        
        elif m.type == ORPHAN:
            print 'ORPHANED'
            self.lock.acquire()
            try:
                self.paired.remove(m.pid)
            except Exception, e:
                fuck_given = 0
            self.lock.release()

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

try:
    c = ChatServer()
    c.serve()
except (KeyboardInterrupt, SystemExit):
        print 'sad'
except Exception, e:
    print 'err'