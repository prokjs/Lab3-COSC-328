from socket import * 
 
HOST = '127.0.0.1' 
PORT = 12000 
 
# set up the tcp socket 
sock = socket(AF_INET, SOCK_STREAM) 
sock.bind((HOST, PORT)) 
sock.listen() 
 
# listen for a connection 
conn, addr = sock.accept() 
print("Connected to " , addr) 
while (True): 
    data = conn.recv(1024).decode("utf-8").upper() 
    print(data) 
    conn.sendall(data.encode("utf-8")) 
    if data == "QUIT": 
        break 
conn.close() 
sock.close() 