#!/usr/bin/env python3
import socket
from threading import *

s = socket.socket()
HOST = socket.gethostname()
PORT = 1247
s.bind((HOST,PORT))
print("Bound on " + repr((HOST,PORT)))

class Client(Thread):
    def __init__(self,socket,address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while True:
            print('Client sent:', self.sock.recv(1024).decode())
            self.sock.send(b"Message Recieved")

s.listen(5)
print ("Server started and Listening")
while True:
    clientsocket, address = s.accept()
    Client(clientsocket, address)

