import socket
import time
from tqdm import tqdm

class Client :
    def __init__(
            self,
            ip = socket.AF_INET,
            address : str = "127.0.0.1",
            port : int = 5000,
            ) :
        self.ip = ip
        self.protocol = socket.SOCK_DGRAM
        self.address = address
        self.port = port
    
    def _create_socket(self) -> socket.socket :
        # Made a client socket with IPv4 addressing (AF_INET)
        # and TCP protocol (SOCK_STREAM) as default
        return socket.socket(self.ip, self.protocol)
    
    def establish_connection(self) :
        self.client_socket = self._create_socket()
        print(f"[CLIENT READY] Using UDP to {self.address}:{self.port}")
    
    def send(self, text : str) :
        # Send data to the server
        self.client_socket.sendto(text.encode(), (self.address, self.port))
    
    def recieve(self) :
        # Receive data from server
        data, addr = self.client_socket.recvfrom(1024)
        print(f"Data received from server -> {data.decode()}")
        return data.decode()

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

def wait(timeout : int = 20) :
    for i in tqdm(range(timeout), "Doing timepass") :
        time.sleep(1)
        print(i + 1, end = "... ")
    print("")

def main() :
    text = _generate_text()
    client = Client()
    client.establish_connection()
    client.send(text)
    client.recieve()
    wait()
    client.close()

if __name__ == "__main__" :
    main()