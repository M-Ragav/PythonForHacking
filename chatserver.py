import socket
import threading

ser = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ser.bind(('0.0.0.0',5000))
ser.listen(1)

username = socket.gethostname()

list_th = []
print('Started server....')

try: 
    target,addr = ser.accept()
    print(f'[+] Client {addr[0]} joined from port {addr[1]}')
except:
     print('failed to connect!!!!')


def recv_msg():
        while True:
            try:
                msg = target.recv(1024)
                if not msg:
                    target.close()
                else:
                    print(f'{msg.decode()}')
            except:
                 pass
            
def send_msg():
        while True:
            try:
                in_msg = input('')
                if in_msg.lower() != 'exit':
                    target.send((username+'>> '+in_msg).encode())
                else: 
                    target.close()
                    for j in list_th:
                         j.join()
                    break
            except:
                 print('Error sending Message!!')

def mainfun():
    s = threading.Thread(target=send_msg)
    r = threading.Thread(target=recv_msg)
    list_th.append(s)
    list_th.append(r)
    for i in list_th:
        i.start()
    for j in list_th:
        j.join(2)
    

mainfun()

       