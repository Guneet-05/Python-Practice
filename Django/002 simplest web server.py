from socket import *

def createServer():
    serversocket = socket(AF_INET,SOCK_STREAM) # making a phone
    try:
        serversocket.bind(('localhost',9000)) #server says that it is ready on port 9000 to receive phone calls
        serversocket.listen(5) # socket asks OS to wait for the current phone call
        # meanwhile if there are other phone calls, just keep them in the queue (kind of a buffer)
        
        while(1):
            (clientsocket,addresss) = serversocket.accept()
            rd = clientsocket.recv(5000).decode()
            pieces = rd.split('\n')
            if(len(pieces) > 0): print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += '\r\n'
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print("Shutting Down...\n")
    except Exception as e:
        print("Error:\n")
        print(e)

    serversocket.close()

print('Access http://localhost:9000')
createServer()