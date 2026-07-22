import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)

sock.connect(("10.0.9.5", 21))

print(sock.recv(1024))

sock.close()
