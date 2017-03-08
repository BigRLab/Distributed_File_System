import socket 
from threading import Thread 
from SocketServer import ThreadingMixIn 
import sys
import os
import signal
import glob
import subprocess
import shutil
 



#navigation for client
root_path = "root"
current_dir = "root"

data=""
kill= 0
path_depth = 0
prev_dir = ""

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread): 
 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print "[+] New server socket thread started for " + ip + ":" + str(port) 
 
    def run(self): 
        #initial = 0
        while True: 
            global prev_dir
            global data
            data = conn.recv(BUFFER_SIZE)
            global path_depth
            print "Client sent : ",data 
            #navigation message handling
            str_arr = data.split(" ")
            if data=="cmds":
                list_of_cmds = "show : shows contents of current directory\n back : takes you back one directory if not in root \n "
                conn.send(list_of_cmds)
            #go to directory    
            elif str_arr[0] == "go":
                try:
                    if os.path.exists(str_arr[1]):
                        path_depth=path_depth+1
                        dir_path = os.path.dirname(os.path.realpath(__file__)) 
                        prev_dir = dir_path
                        os.chdir(dir_path+"/" + str_arr[1])
                        conn.send("Inside "+str_arr[1])  
                    else:
                        conn.send("ERROR! File or directory doesn't exist")
                except:
                    print "File or directory doesn't exist"

                
                

            elif data == "show":
                #show contents of current directory

                dir_path = os.path.dirname(os.path.realpath(__file__))
                if path_depth==0:
                    root_msg = "This is the root directory"
                    conn.send("Showing current directory contents.. \n" +subprocess.check_output(['ls','-l'])+"\n"+ dir_path +"\n"+root_msg)
                else:
                    conn.send("Showing current directory contents.. \n" +subprocess.check_output(['ls','-l'])+"\n"+ dir_path )
                print dir_path

                print subprocess.check_output(['ls','-l'])
            #make a new directory
            elif str_arr[0] == "makedir":
                if os.path.exists(str_arr[1]):
                    conn.send("ERROR! Directory name already exists")
                else:
                    os.makedirs(str_arr[1])
                    print subprocess.check_output(['ls','-l'])
                    dir_path = os.path.dirname(os.path.realpath(__file__))
                    conn.send("Directory Successfully Created! \n Showing current directory contents of.. \n" + dir_path +subprocess.check_output(['ls','-l']) +"\n")
            #go back a directory
            elif data == "goback":
                if path_depth>0:
                    path_depth = path_depth-1
                    os.chdir(prev_dir)
                    dir_path = os.path.dirname(os.path.realpath(__file__)) 
                    conn.send("Switched to "+ dir_path + "\nContents are "+subprocess.check_output(['ls','-l']))
                else:
                    conn.send("ERROR! Can't go back further than root directory")

            #delete file or directory
            elif str_arr[0]=="delete":
                shutil.rmtree(str_arr[1])
                print "Deleted"
                print subprocess.check_output(['ls','-l'])
                conn.send("Successfully deleted "+str_arr[1]+"\n"+subprocess.check_output(['ls','-l']))
            else:
                conn.send("Error! Command not recognised!") 
            #TO DO: STILL NEED TO IMPLEMENT FILE READ/WRITE
                

TCP_IP = '0.0.0.0' 
TCP_PORT = 8000 
BUFFER_SIZE = 1024  
 
tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 
 
while kill!=1: 
    tcpServer.listen(4) 
    print "Multithreaded Python server : Waiting for connections from TCP clients..." 
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads.append(newthread) 

 
for t in threads: 
    t.join() 