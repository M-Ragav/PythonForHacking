# sender.py
import socket
from cryptography.fernet import Fernet

# Generate a key once and use it both in sender and receiver
key = Fernet.generate_key()
cipher = Fernet(key)

# Data to send
message = "Hello Venket!".encode()
encrypted_message = cipher.encrypt(message)

# Send UDP packet
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(encrypted_message, ('127.0.0.1', 12345))

print("Encrypted data sent:", encrypted_message)
print("Key (copy this to receiver):", key.decode())
