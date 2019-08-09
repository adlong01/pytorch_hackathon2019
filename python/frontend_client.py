import socket

#-----------------------------------------------------------------------------------
# SETUP SOCKETS

TCP_IP_ADDRESS = "172.22.187.54"                                # LAN IP ADDRESS OF SERVER
TCP_PORT_NO = 20430
# ADDRESS = (TCP_IP_ADDRESS, PORT_NO)

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((TCP_IP_ADDRESS, TCP_PORT_NO))

#-----------------------------------------------------------------------------------

while(True):
        clientsocket.send("donut".encode())

#-----------------------------------------------------------------------------------
