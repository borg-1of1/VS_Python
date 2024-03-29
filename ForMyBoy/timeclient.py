"""
File: timeclient.py
Project 10.2
Client for obtaining the day and time. Recovers from connection
errors.
"""

from socket import *
from codecs import decode

HOST = "localhost" 
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
while True:
    try:
        server = socket(AF_INET, SOCK_STREAM) 
        server.connect(ADDRESS)                         # Connect it to a host
        dayAndTime = decode(server.recv(BUFSIZE), "ascii")  # Read a string from it  
        break
    except ConnectionRefusedError: 
        print("Connection Refuse")
        timeout(3)
    
print(dayAndTime)
server.close()      
