from socket import * 
HOST = '127.0.0.1' 
PORT = 12000 

# set up the tcp socket 
sock = socket(AF_INET, SOCK_STREAM) 
sock.connect((HOST, PORT)) 

def open_connection(port):
    global sock
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((HOST, port))
    print("Connected to server on port", port)

def get_file(filename):
    sock.sendall(('GET ' + filename).encode('utf-8'))
    data = sock.recv(1024).decode('utf-8')
    if data.startswith('ERROR'):
        print(data)
    else:
        with open(filename, 'x') as f:
            f = open(filename, "w")
            f.write(data)
            f.close()
            print('Received', filename)

def put_file(filename):
    try:
        with open(filename, 'rb') as f:
            file_data = f.read()
            sock.sendall(('PUT ' + filename).encode('utf-8') + file_data)
            print('Sent', filename)
    except FileNotFoundError:
        print("File not found.")


def close_connection():
    sock.sendall('CLOSE'.encode('utf-8'))
    sock.close()
    print("Connection closed.")

def quit_client():
    sock.sendall('QUIT'.encode('utf-8'))
    sock.close()
    print("Connection closed.")
    exit()

while (True): 
    s = input("Message: ") 
    sock.sendall(s.encode("utf-8")) 
    data = sock.recv(1024).decode("utf-8") 
    if data.startswith('OPEN'):
        port = int(data[5:])
        open_connection(port)
    elif data.startswith('GET'):
        filename = data[4:]
        get_file(filename)
    elif data.startswith('PUT'):
        filename = data[4:]
        put_file(filename)
    elif data == 'CLOSE':
        close_connection()
    elif data == 'QUIT':
        quit_client()
    else:
        print("Invalid data.")
    print ("Received: ", data) 
    
sock.close()  
 

