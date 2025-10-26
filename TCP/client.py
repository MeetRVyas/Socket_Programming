import socket
import time

class Client :
    def __init__(
            self,
            ip = socket.AF_INET,
            protocol = socket.SOCK_STREAM,
            address : str = "127.0.0.1",
            port : int = 5000,
            ) :
        self.ip = ip
        self.protocol = protocol
        self.address = address
        self.port = port
    
    def _create_socket(self) -> socket.socket :
        # Made a client socket with IPv4 addressing (AF_INET)
        # and TCP protocol (SOCK_STREAM) as default
        return socket.socket(self.ip, self.protocol)

    def _connect_to_port(self) :
        # Connecting the client to server at localhost (127.0.0.1) at port 5000
        self.client_socket.connect((self.address, self.port))
        print(f"[CLIENT CONNECTED] {self.address} at port {self.port}")
    
    def establish_connection(self) :
        self.client_socket = self._create_socket()
        self._connect_to_port()
    
    def send(self, text : str) :
        # Send data to the server
        self.client_socket.sendall(text.encode())
    
    def recieve(self) :
        # Receive data from server
        data = self.client_socket.recv(1024).decode()
        print(f"Data received from server -> {data}")
        return data

    def close(self) :
        # Close the connection
        self.client_socket.close()
        print("Client closed")

def _generate_text(length = None):
    if length :
        import string, random
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(length))
    else :
        import lorem
        return lorem.paragraph()

def main() :
    text = _generate_text()
    client = Client()
    client.establish_connection()
    client.send(text)
    client.recieve()
    client.close()

if __name__ == "__main__" :
    main()