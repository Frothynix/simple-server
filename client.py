#!/usr/bin/env python3
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = "192.168.1.187"
PORT = 1247

s.connect((HOST,PORT))
print("Starting Connection on " + HOST + ":" + PORT)

def send_message(msg):
    s.send(msg.encode())

send_message("Test!")


