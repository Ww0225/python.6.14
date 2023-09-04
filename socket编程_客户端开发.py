import socket

socket_client = socket.socket()

socket_client.connect(("localhost",8888))

socket_client.send("hi".encode("UTF-8"))

recv_data = socket_client.recv(1024)
print(recv_data.decode("UTF-8"))

socket_client.close()