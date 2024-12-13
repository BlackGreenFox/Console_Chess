import socket
import threading

class P2PNode:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.peers = []

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)
        print(f"[SERVER] Listening on {self.host}:{self.port}")

        while True:
            client_socket, client_address = server.accept()
            print(f"[NEW CONNECTION] {client_address} connected.")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"[MESSAGE RECEIVED] {message}")
                else:
                    break
            except:
                break
        client_socket.close()

    def connect_to_peer(self, peer_host, peer_port):
        peer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        peer.connect((peer_host, peer_port))
        self.peers.append(peer)
        threading.Thread(target=self.listen_for_messages, args=(peer,)).start()

    def listen_for_messages(self, peer):
        while True:
            try:
                message = peer.recv(1024).decode('utf-8')
                if message:
                    print(f"[MESSAGE FROM PEER] {message}")
            except:
                break

    def send_message(self, message):
        for peer in self.peers:
            peer.send(message.encode('utf-8'))

if __name__ == "__main__":
    host = input("Enter your IP address: ")
    port = int(input("Enter your port: "))
    
    node = P2PNode(host, port)
    
    threading.Thread(target=node.start_server).start()
    
    while True:
        command = input("[COMMAND] Type 'connect' or 'send': ").strip().lower()
        if command == "connect":
            peer_host = input("Enter peer IP: ")
            peer_port = int(input("Enter peer port: "))
            node.connect_to_peer(peer_host, peer_port)
        elif command == "send":
            message = input("Enter your message: ")
            node.send_message(message)
