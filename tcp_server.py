import socket
import threading

def handle_client(client_socket, client_address, clients):
    print(f"Connection from {client_address} has been established.")
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"Received message from {client_address}: {message.decode()}")
                broadcast(message, client_socket, clients)
            else:
                break
        except:
            break
    print(f"Connection from {client_address} has been closed.")
    client_socket.close()
    clients.remove(client_socket)

def broadcast(message, sender_socket, clients):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.sendall(message)
            except:
                client_socket.close()
                clients.remove(client_socket)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('0.0.0.0', 65432)  # Listen on all available interfaces
    server_socket.bind(server_address)
    server_socket.listen(5)
    print(f"Server is listening on {server_address}")

    clients = []

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket, client_address, clients)).start()

if __name__ == "__main__":
    main()
