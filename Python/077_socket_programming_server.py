from socket import *

server = socket() # the 2 params should be either ipv4/v6
# and tcp/udp
# since we are not providing any parameter, by default it is ipv4 and tcp
print("socket created")
# ip address of the server and the port no with which we are binding it to
server.bind(('localhost',9999))

# this means we will have 3 clients
server.listen(3)
print('waiting for connections')

# continuosly keep running the connections
# means first client's request has been processed, then continue 
# with the next client, then next client and so on
while True:
    client_socket,address = server.accept()
    name = client_socket.recv(1024).decode()
    print("Connected with",address,name)
    client_socket.send(bytes("Hello World",'utf-8'))
    client_socket.close()
