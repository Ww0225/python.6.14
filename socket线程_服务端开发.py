import socket

socket_server = socket.socket()
socket_server.bind(("localhost",8888))

socket_server.listen(1)

conn,address = socket_server.accept()

print(f"客户端的信息是：{address}")

data = conn.recv(1024).decode("UTF-8")
print(f"客户端发来的消息:{data}")
msg = input("请输入你要和客户端回复的消息:").encode("UTF-8")

conn.send(msg)

conn.close()
socket_server.close()
