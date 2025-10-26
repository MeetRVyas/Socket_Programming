import socket
import threading

class Server :
    def __init__(
            self,
            ip : socket.AddressFamily = socket.AF_INET, # IPv4
            address : str = "127.0.0.1", # localhost
            port : int = 5000,
            MAX_CLIENTS : int = 5,
            ) :
        self.ip = ip
        self.protocol = socket.SOCK_DGRAM # UDP
        self.address = address
        self.port = port
        self.MAX_CLIENTS = MAX_CLIENTS
    
    def _create_socket(self) -> socket.socket :
        # Made a server socket with IPv4 addressing (AF_INET)
        # and TCP protocol (SOCK_STREAM) as default
        return socket.socket(self.ip, self.protocol)

    def _bind_to_port(self) :
        # Binding the server to localhost (127.0.0.1) at port 5000
        self.server_socket.bind((self.address, self.port))
        print(f"[STARTING] {self.address} at port {self.port}")

    def start_server(self) :
        self.server_socket = self._create_socket()
        self._bind_to_port()
        print(f"[STARTED] UDP Server is ready on port {self.port}...")
    
    def handle_client_message(self, data: bytes, addr: tuple):
        message = data.decode()
        print(f"[{addr}] {message}")
        # Echo the message back
        self.server_socket.sendto(data, addr)

    def handle_messages(self):
        print(f"[WAITING] Server ready to receive messages...")
        clients : int = 0
        try :
            while clients < self.MAX_CLIENTS :
                data, addr = self.server_socket.recvfrom(1024)
                clients += 1
                # Start a new thread to handle each message
                thread = threading.Thread(target=self.handle_client_message, args=(data, addr))
                thread.start()
                print(f"[ACTIVE THREADS] {threading.active_count() - 1}")
            thread.join()
        except :
            return

    def close(self) :
        # Close the connection
        self.server_socket.close()
        print("Server closed")

def main() :
    server = Server()
    server.start_server()
    server.handle_messages()
    server.close()

if __name__ == "__main__" :
    main()