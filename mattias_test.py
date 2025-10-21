import socket
"""
def scan_ports(host_port, start_port, end_port):
    print(f"Scanning ports on {host_port}...")
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set connection timout
        
        result = sock.connect_ex((host_port, port))
        
        if_result == 0
        """
        
from my_util("Hello")
if __name__== "__main__":
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(F"The hostname is: {hostname}")
    print(f"The IP is: {ip}")
    pass