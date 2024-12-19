
import socket

def scan_ports(target_ip):
    print(f"Scanning ports on {target_ip}...")
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open.")
        s.close()

if __name__ == "__main__":
    target = input("Enter target IP: ")
    scan_ports(target)
    