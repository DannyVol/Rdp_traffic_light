import time
import methods.methods as methods
import socket
import threading
import configparser

# configuration
config_parser = configparser.ConfigParser()

# global state ###
host_name = socket.gethostname()
host_in_addr = methods.getHostAddr()
 
   
# need to build tuple for data sending over TCP
def mainLogic():
    while True:
        if (methods.getActivePort(3389) == True):
            remote_host = methods.getRhost(methods.getRhostADDR())            
        else:
            con_user = methods.consolUser()
            sock.sendall(str.encode(con_user))
        time.sleep(2)

def outConn():    
    while True:
        d = methods.getOutHostAddr()
        if (d == 'None'):
            sock.sendall(str.encode("outbound connection"))
            print("outbound connection")
        else:
            print('no outbound connection')
            sock.sendall(str.encode("no outbound connection"))
        time.sleep(2)

######################
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
        
# Create new thread to wait for data
def receive_starter():
    receiveThread = threading.Thread(target = receive, args = (sock, True))
    receiveThread.start()

# Initil connaction to the server   
while True:
    config_parser.read('config.cfg')
    srv_ip = config_parser['SERVER']['srvaddress']
    srv_port = int(config_parser['SERVER']['srvport'])
    #Attempt connection to server
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((srv_ip, srv_port))
    except:
        print("Could not make a connection to the server")
        time.sleep(1)
    else:
        # Start threads
        receive_starter()
        methods.sTarter(mainLogic)
        methods.sTarter(outConn)
        break


