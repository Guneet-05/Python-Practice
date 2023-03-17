import urllib.request

fhand = urllib.request.urlopen('http://127.0.0.1:9000/romeo.txt')
for line in fhand:
    print(line.decode().strip())

# We are now operating on HTTP level as we are communicating through URLs
# and not the sockets
