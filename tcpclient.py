import socket

target_host = "www.google.com"
target_port = 80
# create socket object 
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connect to the client
client.connect((target_host,target_port))

# send request data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode())

response = client.recv(4096)

print(response.decode())
client.close()