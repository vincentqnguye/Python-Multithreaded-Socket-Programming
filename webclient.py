#import socket module
from socket import *
import time

def clientExecute(): 
    clientSocket = socket(AF_INET, SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345   
    clientSocket.connect((host,port))

    while True: 
        print ("\n input GET filename to Http Request multiplethreading;     \
                \n input POST data to Http POST multiplethreading;          \
                \n input q to exit")

        command = input()
        httpMethod = command.split(" ")[0]
        if httpMethod == "GET":
            filename = command.split(" ")[1]
            getMessage = "GET " + filename + " HTTP/1.1\r\nHost: localhost:6789\r\n\r\n" 
            clientSocket.sendall(getMessage.encode()) 
            time.sleep(1)

            result = clientSocket.recv(1024)
            print('Received from the server :', str(result.decode('ascii'))) 

        elif httpMethod == "POST":
            data = command.split(" ")[1]         #whatever data e.g. user=ece374"

            #Fill in start
	    #Generate POST message
            postMessage = "POST " + data

	    #Fill in end

            clientSocket.sendall(postMessage.encode())
            time.sleep(1)

            #Fill in start
            # messaga received from server 
            result = clientSocket.recv(1024)

            #Fill in end 

            print("Message received from server: ", str(result.decode('ascii')))
        elif command == "q":
            break

    #Fill in start
    # close the connection 
    clientSocket.close()

    #Fill in end

clientExecute()
