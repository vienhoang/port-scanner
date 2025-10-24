#!/usr/bin/env python3
"""
Network Scanner Project
Students: Björn, Daniel, Mattias.K, Lukas.S, Vien
Date: 251021
"""

#echo client and server


import socket
import sys

# start_server(str, int) the default host is 127.0.0.1 and the default port is 8080
def start_server(host="127.0.0.1", port=8080):
    # Create a TCP/IP socket of IPv4 family and SOCK_STREAM type
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # To avoid getting the "Address already in use" error
    # Allows the server to restart and bind to the same port immediately, even if it has recently been shut down
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Listen to the address and port defined above
    server_socket.bind((host, port))

    # Listen to the address and port defined above
    server_socket.listen()

    # Try to listen to a client socket
    try:
        while True:
            print("Waiting for a connection...")
            # Get the client socket and set the as variables
            client_socket, client_address = server_socket.accept()

            # Try to receive data from client after an establish connection
            try:
                # Return a socket with 1024 bytes
                print(f"Connection from {client_address}")
                # Receive client data up to 1024 bytes
                data = client_socket.recv(1024)

                # If there is data sent from client
                if data:
                    # Decode data from utf-8 format
                    response = data.decode("utf-8")
                    
                    # Strip away any white space and newline and if the response is ping
                    if response.strip() == "ping":
                        # Send back message to client in the form of a byteobject
                        client_socket.sendall(b"pong")

            # Close socket for client
            finally:
                client_socket.close()
                
    # catches an interrupt from the keyboard, usually when you press Ctrl + C in the terminal
    except KeyboardInterrupt:
        print("Keyboard interupt.")
        sys.exit(1)
    # catch other errors
    except Exception as e:
        print(f"Something went wrong!\nError: {e}")
    # Close socket for server
    finally:
        server_socket.close()

# Start the program and run the start_server()
if __name__ == "__main__":
    start_server()
