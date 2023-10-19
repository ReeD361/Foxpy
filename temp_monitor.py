import sys
import os
import time
from time import sleep


sn = sys.argv[1]
ip = sys.argv[2]
sleeping = sys.argv[3]
fix = sys.argv[4]
ruta = '/home/red361/Roms'
rutascript = '%s/tool/Nitro' % ruta
rutafix = '%s/testgui/Fix/%s/%s' % (ruta, fix, sn)
exits = os.path.isdir('%s' % rutafix)
sleeping = int(sleeping)
pid = os.getpid()
os.system('echo "%s" >> %s/pid_temp.txt' % (pid, rutafix))

while True and sn != '' and exits:
    time.sleep(sleeping)
    temp = os.popen('date +%D').read().rstrip()
    timer = os.popen('date +%H').read().rstrip()
    res = temp + timer
    print(res)
    os.system('echo "%s" >> %s/temp.txt' % (res, rutafix))
    os.system('sleep 3')




