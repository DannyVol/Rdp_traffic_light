import time
import Sys
import socket
import threading

### global state ###
hostName = socket.gethostname()
print(hostName)
inHostAddr = Sys.getHostAddr()
print(inHostAddr)
print(Sys.getOutHostAddr())

### Multi threading starter ###
def sTarter(targetX):
    threading.Thread(target=targetX).start()

def mainLogic():
    while True:
        if (Sys.getActivePort(3389) == True):
            rHost = Sys.getRhost(Sys.getRhostADDR())
            print('True')
        else:
            Sys.consolUser()
        time.sleep(2)

def outConn():    
    while True:
        d = Sys.getOutHostAddr()
        if (d == 'None'):
            print("outbound connection")
        else:
            print('no outbound connection')
        time.sleep(2)

sTarter(mainLogic)
sTarter(outConn)

