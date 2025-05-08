import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

client.sendto(b'Hi, This is ragav!',('192.168.1.1',5000))

# data, addr = client.recvfrom(4096)

# print(data.decode())
client.close()
