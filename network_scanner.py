#!/usr/bin/env python3
"""
Network Scanner Project
Students: Mattias.K
Date: 251021
"""

#echo client and server


import socket
import sys

print("test")
def start_server(host="0.0.0.0", port=8080):
    # Create a TCP/IP socket of IPv4 family and SOCK_STREAM type
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    
    while True:
        print("Waiting for a connection...")
        client_socket, client_address = server_socket.accept()

        print(f"Connection from {client_address}")
        #1024b buffertminne för att ta emot data
        data = client_socket.recv(1024)

        if data:
            response = data.decode("utf-8")
            print(f"Raw data: {data}")
            if response == "ping":
                print("pong")

if __name__== "__main__":
    start_server



