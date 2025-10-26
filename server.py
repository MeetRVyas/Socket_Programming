import socket

# Made a server socket with
# IPv4 addressing (AF_INET) and TCP protocol (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding the server to localhost (127.0.0.1) at port 5000
server_socket.bind(("127.0.0.1", 5000))

# Server listening for exactly one connection
server_socket.listen(1)
print("Listening to port")

# Wait and accept a connection, if any
conn, addr = server_socket.accept()
print(f"Address connected to -> {addr}")

# Read the data receiving from the client connection
while True :
    data = conn.recv(1024)
    # If the client has closed the connection
    if not data :
        break
    print(f"Data received -> {data.decode()}")
    # Send the received data back to client
    conn.sendall(data)

# Close the connection
conn.close()
server_socket.close()
print("Server closed")