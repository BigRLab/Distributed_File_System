import socket 
from threading import Thread 
from SocketServer import ThreadingMixIn 
 



#navigation for client
root_path = "root"
current_dir = "root"




# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread): 
 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print "[+] New server socket thread started for " + ip + ":" + str(port) 
 
    def messages(self): 
        initial = 0
        while True : 
            
            if initial==0:
                conn.send("Connected to server. To see list of interactive commands,please type cmds. Current Directory: "+root_path)
                initial = 1

            
            data=""
            data = conn.recv(2048) 
            #navigation message handling
            if data == "show":
                #show contents of current directory
            if data == "back":
                #go back one directory and show contents of it
                if current_dir!="root":

                else:
                    conn.send("Error! Can't go back further than root directory")
            if data[:5] == "go to":
                #extract name of directory to navigate to

               #if user wants to download/open a file
            if data[:4] == "open"    
            
            #if user wants to upload a file
            if data[:6] == "upload"


            #if user wants to see list of commands
            if data[:4] == "cmds":
                list_of_cmds = "show : shows contents of current directory\n back : takes you back one directory if not in root \n "
                        

            
TCP_IP = '0.0.0.0' 
TCP_PORT = 8000 
BUFFER_SIZE = 1024  
 
tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 
 
while data[:12]!="KILL_SERVICE" : 
    tcpServer.listen(4) 
    print "Multithreaded Python server : Waiting for connections from TCP clients..." 
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads.append(newthread) 

 
for t in threads: 
    t.join() 