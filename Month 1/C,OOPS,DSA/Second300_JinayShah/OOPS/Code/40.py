import socket
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_connections = []

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()
            self.client_connections.append((client_socket, client_handler))

    def handle_client(self, client_socket):
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            print(f"Received message: {message}")

        client_socket.close()

class Client:
    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.server_host, self.server_port))
        print(f"Connected to server at {self.server_host}:{self.server_port}")

    def send_message(self, message):
        self.client_socket.sendall(message.encode('utf-8'))

    def disconnect(self):
        self.client_socket.close()

if __name__ == "__main__":
    server = Server(host="127.0.0.1", port=8080)
    server_thread = threading.Thread(target=server.start)
    server_thread.start()
    client = Client(server_host="127.0.0.1", server_port=8080)
    try:
        client.connect()
        client.send_message("Hello, Server!")
    finally:
        client.disconnect()