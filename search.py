from datetime import datetime

import os
import sys
import time
import select
import re
datestring = datetime.strftime(datetime.now(),'%Y-%m-%d-%H-%M')
check = sys.argv[1]
mam=1

with open(check,"r+") as f:
    new_f = f.read()
#    f.seek(0)
    for line in new_f:
#        if (line == "") and (mam%2 == 0) :
        if line == "" :
           print("ok")
#           mam+=1
#           f.write(line)
#        elif (line == "") and (mam%2 != 0):
#           mam+=1
#        else :
#           f.write(line)

    f.truncate()

