import socket
import threading

bind_ip ="0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#bind ip and port
server.bind((bind_ip,bind_port))

# listen for connectivity
server.listen(5)

print("[*] Listening on %s:%d" %(bind_ip,bind_port))

 # this code handles the client connecting to the port
def handle_client(client_socket):
    # get what is sent by client
    request = client_socket.recv(1024)

    print("[*] received %s"% request)

    client_socket.send("ACK!".encode())

    client_socket.close()

while True:
    client,addr = server.accept()

    print("[*] Accepted connection from %s:%d" % (addr[0],addr[1]))

    # handle client data using threads

    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()



