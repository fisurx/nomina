from socket import *
socket_client = socket(AF_INET, SOCK_STREAM)
socket_client.connect(("localhost",3421))
enviar=[]

user=raw_input("Ingrese nombre de usuario: ")
enviar.append(user)
message=""


while message!="out":
	enviar=[user,": "]
	print ""
	message=raw_input("send: ")
	enviar.append(message)
	enviar=" ".join(enviar)	
	socket_client.send(enviar)
