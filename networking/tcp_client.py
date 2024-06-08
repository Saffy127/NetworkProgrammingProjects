import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(message.decode())
            else:
                break
        except:
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('172.31.72.193', 65432)  # Use the IP address of your Linux machine
    client_socket.connect(server_address)

    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        message = input("Enter message: ")
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode())

    client_socket.close()

if __name__ == "__main__":
    main()
