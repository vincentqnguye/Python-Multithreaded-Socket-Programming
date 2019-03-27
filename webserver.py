from pathlib import Path
#import socket module
from socket import *
# import thread module 
from _thread import *
#from threading import Thread
from threading import Lock
plock = Lock() 

# thread fuction 
def threadOperation(connectionSocket): 
    '''
    Please implement this function. You might refer to the implementation: https://www.geeksforgeeks.org/socket-programming-multi-threading-python/
    This functions does the following work:

      (1)Keep receive message from client and parse the messsage header as GET or POST
      (2) Judge if it's GET and POST and act accordingly
      (3) If it's GET, it gets filename requested, 
           (a)  if successfully reads a message from the client; then it will read the content from the file. 
                and then reply back HTTP OK with the content together to the client
           (b) if not, it will reply HTTP 404 NOT FOUND to the client
      (4) If it's POST, it just will parse it and store it in a file, and then reply HTTP OK back to the client
    
    '''
    #Fill in start

    while True:
        data = connectionSocket.recv(1024).decode()
        if not data: 
           print('Bye') 
           # lock released on exit 
           plock.release() 
           break
        #data = connectionSocket.recv(1024).decode()
        mylist = data.split(" ")
        mylist2 = data.split(" ", 1)[1]
        
        if mylist[0] == "GET":
             print("Received data from a client: " + mylist[1])
             fname = mylist[1]
             my_file = Path(fname)
             try:
                  my_abs_path = my_file.resolve(strict=True)
             except FileNotFoundError:
                  # doesn't exist
                  message = "HTTP/1.1 404 Not Found \n"
                  connectionSocket.send(message.encode())
             else:
                  # file exists
                  f = open(fname, "r")
                  message = "HTTP/1.1 200 OK \n" + f.readline()
                  connectionSocket.send(message.encode())
                  f.close()
        elif mylist[0] == "POST":
             print("Received data from a client: " + mylist2)
             print("\nStored in client_message.html")
             f = open('client_message.html', "w")
             f.write(mylist2)
             f.close()
             message = "HTTP/1.1 200 OK \n"
             connectionSocket.send(message.encode())
    connectionSocket.close()
    #Fill in end


def executeFunction(connectionSocket):
    '''
    start a new thread function
    '''
    # lock acquired by client 
    plock.acquire() 

    #Fill in start
    # Start a new thread using Thread library, the thread function is threadOperation above
    start_new_thread(threadOperation, (connectionSocket,)) 
   # threadOperation(connectionSocket)

    #Fill in end

    print("new_thread done. ") 
   

def serverExecute(): 
    '''
    main entry function for a server
    '''
    serverSocket = socket(AF_INET, SOCK_STREAM)
    #Prepare a sever socket
    #Fill in start
    # bind the socket to a public host, and a well-known port
    host = ""
    port = 12345
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    serverSocket.bind((host, port)) 
    print("socket binded to post", port) 

    #Fill in end

    # become a server socket and in listening mode
    serverSocket.listen(5)

    while True:
        #serverSocket.listen(5)
        print("Ready to serve...")
        #Establish the connection
        connectionSocket, addr = serverSocket.accept()
        executeFunction(connectionSocket)

    #Fill in start
    #Close client socket
    #connectionSocket.close()

    #Fill in end
    serverSocket.close()

serverExecute() 