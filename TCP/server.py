import socket
import threading

class Server :
    def __init__(
            self,
            ip : socket.AddressFamily = socket.AF_INET, # IPv4
            address : str = "127.0.0.1", # localhost
            port : int = 5000,
            listen_to : int = 5,
            MAX_CLIENTS : int = 5,
            ) :
        self.ip = ip
        self.protocol = socket.SOCK_STREAM # TCP
        self.address = address
        self.port = port
        self.listen_to = listen_to
        self.MAX_CLIENTS = MAX_CLIENTS
    
    def _create_socket(self) -> socket.socket :
        # Made a server socket with IPv4 addressing (AF_INET)
        # and TCP protocol (SOCK_STREAM) as default
        return socket.socket(self.ip, self.protocol)

    def _bind_to_port(self) :
        # Binding the server to localhost (127.0.0.1) at port 5000
        self.server_socket.bind((self.address, self.port))
        print(f"[STARTING] {self.address} at port {self.port}")

    def _start_listening(self) :
        # Server listening for exactly one connection
        self.server_socket.listen(self.listen_to)
        print(f"[STARTING] Server is listening on port {self.port}...")
    
    def start_server(self) :
        self.server_socket = self._create_socket()
        self._bind_to_port()
        self._start_listening()
        print(f"[STARTED] TCP Server is ready on port {self.port}...")
    
    def connect_to_client(self) -> tuple[socket.socket, str] :
        # Wait and accept a connection, if any
        conn, addr = self.server_socket.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        return conn, addr
    
    def handle_client(self, conn : socket.socket, addr : str) :
        # Read the data receiving from the client connection
        while True :
            try :
                data = conn.recv(1024)
                # If the client has closed the connection
                if not data :
                    break
                print(f"[{addr}] {data.decode()}")
                # Send the received data back to client
                conn.sendall(data)
            except ConnectionResetError :
                break
        print(f"[DISCONNECTED] {addr}")
        conn.close()
    
    def handle_multiple_clients(self) :
        clients : int = 0
        while clients < self.MAX_CLIENTS :
            conn, addr = self.connect_to_client()
            clients += 1
            thread = threading.Thread(target = self.handle_client, args = (conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

    def close(self) :
        # Close the connection
        self.server_socket.close()
        print("Server closed")

def main() :
    server = Server()
    server.start_server()
    server.handle_multiple_clients()
    server.close()

if __name__ == "__main__" :
    main()