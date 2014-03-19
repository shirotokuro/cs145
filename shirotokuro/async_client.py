#!/usr/bin/python
import socket
import connection
import pickle
import traceback
import threading
import time
import message

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
        player2id = m[1]
        if player2id == -1:
            time.sleep(1)
    print "Your partner is ", player2id
    return player2id

def sender(client_connection,  playerid, player2id):
    while True:
        message = raw_input("Enter message: ")
        client_connection.sendMessage([UPDATE, playerid, player2id, [], message])
        if message.strip() == "QUIT":
            break

def main():

    global playerid

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
        
        senderthread = threading.Thread(target = sender, args = (conn, playerid, player2id,))
        senderthread.start()
       
        while True:
            response = conn.getMessage().replace("\\n","\n\t")
            print "Server: " + response
            if response.strip() == "":
                break
        s.close()

        #headers = [1, 'Hi']
        #message = headers + ['con']
        #conn.sendMessage(message)
        #conn.sendMessage(message)
    except Exception as e:
        print "Client: Error happened! ", e
        traceback.print_exc()
        s.close()

if __name__ == '__main__':
    main()
