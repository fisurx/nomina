from socket import *
socket_client = socket(AF_INET, SOCK_STREAM)
socket_client.connect(("localhost",3421))
socket_client.send("hola")
