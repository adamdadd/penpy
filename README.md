# penpy - Python Scripts for Networking and Pen Tests
A collection of useful python networking examples that can be used for pen testing.

## TCP_client.py
![TCP_client](https://github.com/adamdadd/penpy/blob/master/img/TCP_client.png)

Now to write a simple TCP client.
```python
import socket

target_host = ""
target_port = 9999

# Creating a socket object...
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connecting the client...
client.connect((target_host, target_port))
# Sending some data...
client.send(str.encode("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"))
# Getting the reponse...
response = client.recv(4096)

print(response)
```
<i>AF_INET:</i> Using IPv4 address/hostname.\
<i>SOCK_STREAM:</i> This is a TCP client.

### Socket Assumptions
<ol>
<li> The connection will always succeed.
<li> Server expects data from client first (rather than response).
<li> Data from server will be sent at an appropriate time. 
</ol>

## UDP_client.py
A simple UDP client.

UDP is much like it's TCP counterpart but UDP is a connectionless protocol so some changes need to be made...
```python
import socket

target_host = "0.0.0.0"
target_port = 9999

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto(str.encode("AAABBBCCC"),(target_host,target_port))

# receive some data
data, addr = client.recvfrom(4096)

print(data)
```
<i>SOCK_DGRAM:</i>  

## TCP_server.py
![TCP_server](https://github.com/adamdadd/penpy/blob/master/img/TCP_server.png)
A simple TCP server. Works with TCP_client.py 
```python
import socket
import threading

bind_ip   = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print("[*] Listening on %s:%d" % (bind_ip, bind_port))

def handle_client(client_socket):
    # print out what the client sends
    request = client_socket.recv(1024)

    print("[*] recieved %s" % request)

    # send a packet back...
    client_socket.send(str.encode("ACK!"))

    client_socket.close()

while True:
    client, addr = server.accept()
    
    print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
    
    # spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
```
## Netkitten.py
A netcat clone written in python. Useful when unable to use netcat in system that it has been disabled.

## TCP_proxy.py
