import time

import Sys


while True:
    if (Sys.getActivePort(3389) == True):
        print("true")
    else:
        Sys.consolUser()
    time.sleep(2)