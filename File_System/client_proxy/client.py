
import socket 
 
host = socket.gethostname() 
port = 8000
BUFFER_SIZE = 1024 
MESSAGE = raw_input("Enter command or type exit: ") 

clientConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientConnection.connect((host,port))

while MESSAGE != 'exit':
    clientConnection.send(MESSAGE)  
    data = clientConnection.recv(BUFFER_SIZE)
    print " Client received data:\n", data
    MESSAGE = raw_input("Enter command or type exit: ")
 
clientConnection.close() 
