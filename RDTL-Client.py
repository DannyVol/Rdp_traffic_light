import time
import methods.methods as methods
import socket
import threading
#import configparser

# configuration
##config_parser = configparser.ConfigParser()
##config_parser.read('config.cfg')

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
        
#Create new thread to wait for data
def recieive_starter():
    receiveThread = threading.Thread(target = receive, args = (sock, True))
    receiveThread.start()
   
while True:
    #Attempt connection to server
    try:
#        srv_ip = config_parser['SERVER']['adrress']
#        srv_port = int(config_parser['SERVER']['Port'])
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect('localhost', 9833)
        recieive_starter()
        methods.sTarter(mainLogic)
        methods.sTarter(outConn)    

    except:
        print("Could not make a connection to the server")
        time.sleep(1)




