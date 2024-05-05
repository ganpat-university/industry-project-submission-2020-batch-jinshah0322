import socket
import threading
import pickle

class DistributedCache:
    def __init__(self, node_id, port):
        self.node_id = node_id
        self.port = port
        self.data = {}
        self.lock = threading.Lock()

    def run_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', self.port))
        server_socket.listen(5)
        print(f"Node {self.node_id} is listening on port {self.port}")

        while True:
            client_socket, addr = server_socket.accept()
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        data = client_socket.recv(1024)
        request = pickle.loads(data)
        response = self.process_request(request)
        client_socket.send(pickle.dumps(response))
        client_socket.close()

    def process_request(self, request):
        command = request['command']
        key = request['key']
        value = request.get('value')

        if command == 'GET':
            return {'result': self.get(key)}
        elif command == 'SET':
            return {'result': self.set(key, value)}
        elif command == 'DELETE':
            return {'result': self.delete(key)}
        else:
            return {'error': 'Invalid command'}

    def get(self, key):
        with self.lock:
            return self.data.get(key)

    def set(self, key, value):
        with self.lock:
            self.data[key] = value
            return True

    def delete(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]
                return True
            else:
                return False

def main():
    node1 = DistributedCache(node_id=1, port=5001)
    node2 = DistributedCache(node_id=2, port=5002)

    threading.Thread(target=node1.run_server).start()
    threading.Thread(target=node2.run_server).start()

    # Example usage
    node1.set('key1', 'value1')
    node2.set('key2', 'value2')

    result1 = node1.get('key1')
    result2 = node2.get('key2')

    print(f"Node 1 - key1: {result1}")
    print(f"Node 2 - key2: {result2}")

if __name__ == "__main__":
    main()
