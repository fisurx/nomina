import os
from socket import *



socket_s=socket(AF_INET, SOCK_STREAM)

socket_s.bind(("localhost", 3421))

socket_s.listen(5)

socket_client, (host_client, port_client) = socket_s.accept()

while True:
	recibido = socket_client.recv(1024)

	print recibido

	socket_client.send(recibido)

socket_s.close()

