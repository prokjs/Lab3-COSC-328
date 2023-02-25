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
    if data.startswith("OPEN"):
        conn.sendall(data.encode("utf-8"))
    elif data.startswith("GET"):
        try:
            filename = data[4:]
            print("getting file: ", filename)
            file = open(filename)
            conn.sendall(file.encode("utf-8"))
            conn.recv(1024).decode("utf-8").upper()
            contents = file.read()
            conn.sendall(contents.encode("utf-8"))
            file.close()
        except:
                conn.sendall("Could not find file.".encode("utf-8"))
    elif data.startswith("PUT"):
        filename = data[4:]
        print("putting file: ", filename)
        conn.sendall(file.encode("utf-8"))
        fileData = conn.recv(1024).decode("utf-8")
        createFile = open(filename, "x")
        print("data: ", fileData)
        createFile.close()
        createFile = open(filename, "w")
        createFile.write(fileData)
        createFile.close()
        print("written")
conn.close() 
sock.close() 