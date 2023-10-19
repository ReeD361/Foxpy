#!/usr/bin/env python
import os
import sys
import pexpect
import time

soc = sys.argv[1]
ip = sys.argv[2]
user = 'admin'
password = 'admin'

os_user = 'root'
os_password = '123456'

cmd = sys.argv[3]

print ('Target (%s)' % (ip))
os.system('ipmitool -H %s -I lanplus -U %s -P %s sol deactivate' % (ip, user, password))
time.sleep(1)

os.system('ipmitool -H %s -I lanplus -U %s -P %s raw 0x34 0x61 %s' % (ip, user, password, soc))
time.sleep(1)

# sol retry parameters
os.system('ipmitool -H %s -I lanplus -U %s -P %s sol set retry-count 7' % (ip, user, password))
time.sleep(1)
os.system('ipmitool -H %s -I lanplus -U %s -P %s sol set retry-interval 20' % (ip, user, password))
time.sleep(1)
os.system('ipmitool -H %s -I lanplus -U %s -P %s sol set character-send-threshold 1' % (ip, user, password))
time.sleep(1)

child = pexpect.spawn('ipmitool -H %s -I lanplus -U %s -P %s sol activate' % (ip, user, password))
child.logfile_read = sys.stdout
time.sleep(1)

prompt_sol = child.expect(['[SOL Session operational.  Use ~? for help]', pexpect.EOF, pexpect.TIMEOUT], timeout = 1)
if prompt_sol == 0:
    child.sendline('\r\n')
    time.sleep(5)  #wait for session stablizing

    child.buffer=""
    while True:
        prompt = child.expect(['#', 'ALPINE_DB', 'login:', '>', pexpect.EOF, pexpect.TIMEOUT], timeout = 1)
        if prompt == 0:
            child.sendline(cmd)
            child.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
            time.sleep(1)
            break
        elif prompt == 1:
            child.sendline('\r\n')
            time.sleep(1)
            child.sendline('boot')
            child.expect(['login:', pexpect.TIMEOUT], timeout=35)
            time.sleep(1)
            continue
        elif prompt == 2:
            child.sendline('\r\n')
            time.sleep(1)
            child.sendline(os_user)
            child.expect(['Password:', pexpect.TIMEOUT], timeout=1)
            child.sendline(os_password)
            child.expect(['#', pexpect.TIMEOUT], timeout=1)
            child.sendline('\r\n')
            time.sleep(1)
            continue
        elif prompt == 3:
            child.sendline('\r')
            child.expect(['#', pexpect.TIMEOUT], timeout=1)
            time.sleep(1)
            continue
        else:
            print '\r\n\033[31mUnexpect session status!!\033[0m'
            child.close(force=True)
            sys.exit(1)
else:
    print '\r\n\033[31mSOL activate failed!!\033[0m'
    child.close(force=True)
    sys.exit(1)

print '\r\n...'
child.close(force=True)
time.sleep(2)
if child.isalive():
    print 'child session error!!'
    sys.exit(1)
else:
    print 'child session closed.'
