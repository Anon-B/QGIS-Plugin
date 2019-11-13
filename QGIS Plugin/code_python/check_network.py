import socket
try:
    socket.create_connection(('www.google.com',80))
    status_network = "Connected"
except socket.error as msg:
    status_network = "Not connected"
print(status_network)