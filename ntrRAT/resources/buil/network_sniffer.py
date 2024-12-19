
from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

if __name__ == "__main__":
    interface = input("Enter network interface (e.g., eth0): ")
    print(f"Sniffing on {interface}...")
    sniff(iface=interface, prn=packet_callback, store=False)
    