from socket import *

client = socket()
# ipv4 and tcp

client.connect(('localhost',9999))

name = input("Enter your name")
client.send(bytes(name,'utf-8'))
# 1024 is buffer size
print(client.recv(1024).decode())