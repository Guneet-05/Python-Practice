from socket import *

mysock = socket(AF_INET,SOCK_STREAM)
mysock.connect(('127.0.0.1',9000))
cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data  = mysock.recv(512)
    if len(data)<1:
        break
    print(data.encode(),end=" ")

mysock.close()