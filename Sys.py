import psutil
import time

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