import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message, _ = client_socket.recvfrom(1024)
            if not message:
                print("Connection closed by the server.")
                break
            print(f"> {message.decode()}")
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def main():
    host_ip = input("Enter host IP: ")
    host_port = int(input("Enter host Port: "))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Підключаємося до сервера
        client_socket.sendto("Hello from client".encode(), (host_ip, host_port))
        print(f"Connected to host at {host_ip}:{host_port}\n")

        # Запускаємо потік для отримання повідомлень
        threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

        while True:
            message = input("Enter command (/exit to quit): ")
            if message.lower() == "/exit":
                print("Disconnecting from server...")
                client_socket.close()
                break
            client_socket.sendto(message.encode(), (host_ip, host_port))

    except ConnectionRefusedError:
        print("Unable to connect to the host. Please check the IP and port.")

if __name__ == "__main__":
    main()
