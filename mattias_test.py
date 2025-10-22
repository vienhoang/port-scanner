"""import socket

def scan_ports(host_port, start_port, end_port):
    print(f"Scanning ports on {host_port}...")
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set connection timout
        
        result = sock.connect_ex((host_port, port))
        
        if_result == 0
        
        
from my_util("Hello")
if __name__== "__main__":
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(F"The hostname is: {hostname}")
    print(f"The IP is: {ip}")
    pass

Testade server.py mot följande IP:
start_server(host="45.33.32.156", port=80):
line 12:     server_socket.bind((host, port))

Felkod:
Traceback (most recent call last):
  File "/mnt/c/Users/kossa/Documents/GitHub/port-scanner/examples/server.py", line 54, in <module>
    start_server()
  File "/mnt/c/Users/kossa/Documents/GitHub/port-scanner/examples/server.py", line 12, in start_server     
    server_socket.bind((host, port))
OSError: [Errno 99] Cannot assign requested address
"""
#import pyfiglet
import sys
import socket
from datetime import datetime
 
#ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
#print(ascii_banner)
 
# Defining a target
if len(sys.argv) == 2:
    print(sys.argv)
    # translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1]) 
else:
    print("Invalid amount of Argument")
    print(sys.argv)
# Add Banner 
print("-" * 50)
print("Scanning Target: " + "45.33.32.156")
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)
 
try:
    
    # will scan ports between 1 to 65,535
    for port in range(1,1000):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        # returns an error indicator
        result = client_socket.connect_ex(("45.33.32.156",port))
        if result ==0:
            print("Port {} is open".format(port))
        client_socket.close()
        
except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()