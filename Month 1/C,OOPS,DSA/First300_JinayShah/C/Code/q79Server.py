import socket

host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((host, port))

server_socket.listen()

print(f"Server listening on {host}:{port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received data from client: {data}")

    response = "Hello from the server!"
    client_socket.send(response.encode('utf-8'))

    client_socket.close()