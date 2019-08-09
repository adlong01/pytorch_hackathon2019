from search_query import QueryExecutor
import socket

#-----------------------------------------------------------------------------------
# SETUP SOCKETS

# CAMERA CLIENT - SERVER SOCKET
TCP_IP_ADDRESS = "172.22.187.54"                                # LAN IP ADDRESS OF SERVER
TCP_PORT_NO = 20430
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('', TCP_PORT_NO))
serversocket.listen(5)
clientsocket, address = serversocket.accept()


#-----------------------------------------------------------------------------------
# INITIALIZE / DECLARE GLOBAL VARIABLES

buf = []
bytesrecvd = 0
DATALEN = 4

#-----------------------------------------------------------------------------------

while True:
	data = clientsocket.recv(1024).decode()
	print(data)

#-----------------------------------------------------------------------------------

query_executor = QueryExecutor("donut")
query_executor.execute_search_query()