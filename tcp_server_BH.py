import socket
import threading

IP = "0.0.0.0"
PORT = 5000

def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((IP,PORT))
    server.listen(5)
    print(f'[*] Listening on {IP} : {PORT}')
    while True:
        client, addr = server.accept()
        print(f'[*] Accepted Connection from {addr[0]}:{addr[1]}')

        client_res = threading.Thread(target=client_recv,args=(client,))
        client_res.start()

def client_recv(client):
    with client as cl:
        response = cl.recv(1024)
        print(f'[*] Received: {response.decode()}')
        cl.send(b'ACK')

if __name__ == '__main__':
    main()
