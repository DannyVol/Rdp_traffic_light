import time
import Sys
import socket


### global state ###
hostName = socket.gethostname()
print(hostName)
inHostAddr = Sys.getHostAddr()
print(inHostAddr)
print(Sys.getOutHostAddr())

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

Sys.sTarter(mainLogic)
Sys.sTarter(outConn)

