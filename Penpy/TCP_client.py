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