from __future__ import print_function
from netmiko import ConnectHandler
from datetime import datetime

import os
import sys
import time
import select
import paramiko
import re
datestring = datetime.strftime(datetime.now(),'%Y-%m-%d-%H-%M')
os.chdir(r'/applis/dcs/x171610/')
#print('Merci de rentrer la date : ')
#my_date=input()
check = sys.argv[3]
fd = open(check, 'w')
old_stdout = sys.stdout
sys.stdout = fd
platform = 'cisco_ios'
username = 'bt-tooling'
password = 'Cisco123!'
bad_words = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
rm = sys.stdout
host = sys.argv[1]
cmd_file = sys.argv[2]
command_file = open(cmd_file)
command_file.seek(0)
device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
output = device.send_command('terminal length 0')
for each_lines in command_file:
    each_lines = each_lines.strip()
    output = device.send_command(each_lines + '\n')
    print(output)
command_file.close()
fd.close()
with open(check,"r+") as f:
    new_f = f.readlines()
    f.seek(0)
    for line in new_f:
        if bad_words not in line:
           f.write(line)
    f.truncate()

