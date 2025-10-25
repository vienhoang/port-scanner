#!/usr/bin/env python3
"""
Network Scanner Project
Students: Björn, Daniel, Mattias.K, Lukas.S, Vien
Date: 251021
"""
# Importing modules
import socket
import sys
import time
#from tqdm import tqdm
#from colorama import init, Fore

# Init colors

"""To do: Reinstate all extra
open <sys.argv> as text
Maybe set port range in txt aswell
"""

with open ("ip_list.txt") as r:
    targets = []
    for line in r.readlines():
        row = line.removesuffix("\n")
        targets.append(row)    
# Global list to save ports
open_ports = []
r.close()

# Set range ports, including the max port
def start_multiscan(targets, start_port, max_port, timeout=0.2, file_name="port_results.txt"):
    try:
        with open(file_name, "w") as f:    

            for target in targets:
                open_ports = []  # Reset for each target
                target = socket.gethostbyname(target)
                f.write(f"{'='*60}\nScanning target IP {target}\n")
                # Calculation for progress bar
            #   total_ports = max_port - start_port + 1
            #    with tqdm(total=total_ports, desc=f"Scanning {target} from [{start_port}] to [{max_port}]", unit="port") as progress_bar:

                # Set range ports, including the max port
                for port in range(start_port, max_port + 1):
                    #AF_INET = IPv4, SOCK_STREAM = constant, create a TCP socket
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    # Try to connect port with time out
                    try:
                        s.settimeout(timeout)
                        # Returns to 0 if a port is open
                        result = s.connect_ex((target, port))
                        # If a port is open, add the open port to the open_ports list
                        if result == 0:

                            # Try to identify the port service
                            try:
                                # For HTTP-ports
                                if port in (80, 8080):
                                    # Sends an HTTP HEAD request to the connected server, asking for only HTTP headers without a body
                                    s.sendall(b"HEAD / HTTP/1.0\r\nHost: %b\r\n\r\n" % target.encode())
                                # Read max 1024 bytes from the opened socket
                                data = s.recv(1024)
                                # Convert the data and do split and strip empy spaces, and get the first part
                                banner = data.decode(errors="ignore").splitlines()[0].strip()
                                
                                # If the banner exists
                                if banner:
                                    # Add open port to the open_ports list
                                    open_ports.append(f"Port {port} : Banner {banner}")
                                    f.write(f"Port {port} : Banner {banner}\n")
                                    #progress_bar.write(f"\nBanner for {target}:{port} -> {banner}")
                                else:
                                    open_ports.append(f"Port {port} : No banner received")
                                    f.write(f"Port {port} : No banner received\n")
                                    #progress_bar.write(f"\nNo banner received for {target}:{port}")

                            # Socket timed out error
                            except socket.timeout:
                                open_ports.append(f"Port {port} : No banner (timeout)")
                                f.write(f"Port {port} : No banner (timeout)\n")
                                #progress_bar.write(f"\nNo banner (timeout) for {target}:{port}")
                            # Catch other errors
                            except Exception as e:                                
                                open_ports.append(f"Port {port} : Error reading banner {e}")
                                f.write(f"Port {port} : Error reading banner {e}\n")
                                #progress_bar.write(f"\nError reading banner for {target}:{port}: {e}")
                        else:
                            f.write(f"No ports are open for {target}\n")                    
                    # DNS lookup failed error
                    except socket.gaierror as e:
                        f.write(f"{target} Hostname could not be resolved. {e}\n")
                        return open_ports
                    # Socket error
                    except socket.error as e:
                        f.write(f"{target} Could not connect to server. {e}\n")
                        return open_ports
                    # Close socket
                    finally:
                        s.close()
            #               progress_bar.update(1)


    except FileNotFoundError:
        print("File not found.")
    # Writing to file errors
    except IOError:
        print("An I/O error occurred.")
    # Other errors
    except Exception as e:
        print("Something went wrong...", e)
    # Close file
    f.close()


# Run the program
if __name__ == "__main__":

    # Scan the give url with start and end ports
    start_multiscan(targets, 31337, 31337, 1)