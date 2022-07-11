import psutil
import time
import socket

### No RDP inbound connaction logic ###
def consolUser():
    x = psutil.users()
    for i in x:
        if (i.host == 'localhost' or 'none'):
            return print(i.name)


#### Find if getPort is in ESTABLISHED status ####
def getActivePort(getPort):
    d = psutil.net_connections()
    activPorts = [x.laddr.port for x in d if x.status == 'ESTABLISHED']
    for port in activPorts:
        try:
            if (port == getPort):
                return True
        except AttributeError:
            pass
    return False

### Find remote host ###
def getRhostADDR():
    try:
        d = psutil.net_connections()
        rHostaddr = [x.raddr.ip for x in d if x.status == 'ESTABLISHED' and x.laddr.port == 3389]
        return rHostaddr
    except IndexError:
        return None

### Find RDP inbound connaction if_adddres ###
def getHostAddr():
    try:
        d = psutil.net_connections()
        hostAddr = [x.laddr.ip for x in d if x.status == 'ESTABLISHED' and x.laddr.port == 3389]
        return hostAddr[0]
    except IndexError:
        return None

### Find RDP outbound connaction if_adddres ###
def getOutHostAddr():
    try:
        d = psutil.net_connections()
        hostAddr = [x.laddr.ip for x in d if x.status == 'ESTABLISHED' and x.raddr.port == 3389]
        return hostAddr[0]
    except IndexError:
        return None
    
### DNS query to get hostname by ip ###
def getRhost(addr):
    hostName = socket.gethostbyaddr(addr)
    return hostName[0]