import socket 

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("0.0.0.0",5000))
server.listen(1)

ipaddr = socket.gethostname()

print(f'[*] Listening from {ipaddr}:5000')
client,addr = server.accept()
print(f'Connected from {addr[0]}:{addr[1]}')

while True:
    msg = client.recv(1029)
    print(f'{addr[0]}>> {msg.decode()}')
    