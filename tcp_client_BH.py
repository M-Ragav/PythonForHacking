import socket

target = 'www.google.com'
port = 80

client_packet = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_packet.connect((target,port))

client_packet.send(b'GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n')

response = client_packet.recv(4096)

print(response.decode())
client_packet.close()
