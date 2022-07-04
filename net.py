import psutil
import time

#### port scanning module ####
def getport(e, tm):
    while True:
        d = psutil.net_connections()
        for c in d:
            try:
                if (c.raddr.port == e):
                    print(c.raddr.port)
                    print("success!")
                else:
                    pass
            except AttributeError:
                pass
        time.sleep(tm)