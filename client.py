import socket
import time

# Made a client socket with
# IPv4 addressing (AF_INET) and TCP protocol (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the port of server
client_socket.connect(("127.0.0.1", 5000))

text = \
"""
Kem Cho Majhama
Hello how are
Khana khake jana
Shu chale party
"""

# Send data to the server
client_socket.sendall(text.encode())

time.sleep(2)

# Receive data from server
data = client_socket.recv(1024)
print(f"Data received from server -> {data.decode()}")

# Close the socket connection
client_socket.close()