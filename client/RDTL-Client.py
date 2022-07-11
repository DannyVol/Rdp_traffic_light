import time
import modules
import socket
import sys
import threading


### global state ###
hostName = socket.gethostname()
print(hostName)
inHostAddr = modules.getHostAddr()
print(inHostAddr)
print(modules.getOutHostAddr())
srv_addr = ('localhost', 12345)


### 
###
### need to build tuple for data sending over TCP ###
def mainLogic():
    while True:
        if (modules.getActivePort(3389) == True):
            rHost = modules.getRhost(modules.getRhostADDR())
            sock.sendall(str.encode('True'))            
        else:
            con_user = modules.consolUser()
            sock.sendall(str.encode(con_user))
        time.sleep(2)

def outConn():    
    while True:
        d = modules.getOutHostAddr()
        if (d == 'None'):
            sock.sendall(str.encode("outbound connection"))
            print("outbound connection")
        else:
            print('no outbound connection')
            sock.sendall(str.encode("no outbound connection"))
        time.sleep(2)


### TCP connaction ###
######################

def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(2048)
            print(str(data.decode("utf-8")))
        except:
            print("You have been disconnected from the server")
            signal = False
            break

#Attempt connection to server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(srv_addr)        
except:
    print("Could not make a connection to the server")
    sys.exit(0)

#Create new thread to wait for data
def reci():
    receiveThread = threading.Thread(target = receive, args = (sock, True))
    receiveThread.start()

#Send data to server
#str.encode is used to turn the string message into bytes so it can be sent across the network

reci()
modules.sTarter(mainLogic)
modules.sTarter(outConn)

