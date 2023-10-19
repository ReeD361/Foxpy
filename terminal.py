import os
import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from threading import Thread

#tmux = sys.argv[1]
tmux = '1'
subprocess.Popen(['tmux', 'new', '-d', '-s', tmux])
directory = '/home/red361/Roms'
#os.system('tmux -s -d 1')


class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        loadUi('console.ui', self)
        self.process = QtCore.QProcess(self)
        self.terminal = QtWidgets.QWidget(self)
        self.coo.addWidget(self.terminal)
        self.process.start('xterm', ['-into', str(int(self.winId())), '-g', '130x70', '-e', 'tmux', 'a', '-t', '%s' % tmux])
        self.bt_ipmiol.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_ipmi))
        self.bt_adv.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_adv))
        self.bt_test.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_test))
        self.bt_ipmiol.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_ipmi))
        self.bt_usbs.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_usb))
        self.bt_ip.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ipfix))
        self.bt_mc_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.mc))
        self.bt_boot.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.bootstrap))
        self.bt_linux.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Linux_adv))
        self.bt_cycle.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_usb))
        self.bt_advfru.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_fur_adv))
        self.bt_adv_sdr.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_sdr_adv))
        self.bt_sol.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_sol))
        self.bt_ipmi.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.adv_ipmi))
        self.bt_pwr_off.clicked.connect(lambda: self.thread('power off'))
        self.bt_pwr_on.clicked.connect(lambda: self.thread('power on'))
        self.bt_pwr_cyc.clicked.connect(lambda: self.thread('chassis power cycle'))
        self.bt_fru.clicked.connect(lambda: self.thread('fru'))
        self.bt_sel.clicked.connect(lambda: self.thread('sel elist'))
        self.bt_mc.clicked.connect(lambda: self.thread('mc info'))
        self.bt_sensor.clicked.connect(lambda: self.thread('sensor'))
        self.bt_sel_clr.clicked.connect(lambda: self.thread('sel clear'))
        self.bt_sdr.clicked.connect(lambda: self.thread('sdr'))
        self.bt_host_ip.clicked.connect(lambda: self.threadip("0x00"))
        self.bt_k2t_ip.clicked.connect(lambda: self.threadip("0x02"))
        self.bt_ok_fru.clicked.connect(lambda: self.hilo('fru', self.line_grep_fru))
        self.bt_ok_3.clicked.connect(lambda: self.hilo('sdr', self.line_sdrg))
        self.bt_ok_2.clicked.connect(lambda: self.hilo('sensor', self.line_grepsen))
        self.bt_okis.clicked.connect(lambda: self.thcustom(self.line_ipmi))
        self.bt_ok_sol2.clicked.connect(lambda: self.thcustom(self.line_raw))
        self.bt_ok_sol.clicked.connect(lambda: self.thcustom(self.line_com))
        self.bt_0x00.clicked.connect(lambda: self.thread("raw 0x34 0x61 0x00"))
        self.bt_0x02.clicked.connect(lambda: self.thread("raw 0x34 0x61 0x02"))
        self.bt_sola.clicked.connect(lambda: self.thread("sol activate"))
        self.bt_sold.clicked.connect(lambda: self.bgcomth("sol deactivate"))
        self.bt_cold.clicked.connect(lambda: self.thread('mc reset cold'))
        self.bt_mci.clicked.connect(lambda: self.thread('mc info'))
        self.bt_start2.clicked.connect(lambda: self.testth('apos_chk_k2v4_bootstrap.sh', self.sn1))
        self.bt_start.clicked.connect(lambda: self.testth('apos_chk_k2v4_bootstrap.sh', self.sn1_2))

        self.bt_okl.clicked.connect(lambda: self.linuxthip('arp', self.sn1_3))
        self.bt_okl2.clicked.connect(lambda: self.linuxthip('ifconfig', self.sn1_4))
        self.bt_okl3.clicked.connect(lambda: self.linuxthgp('ping', self.sn1_5))
        self.bt_okl4.clicked.connect(lambda: self.linuxthgp('ssh', self.sn1_6))
        self.bt_arp.clicked.connect(lambda: self.linuxth('arp'))
        self.bt_pwd.clicked.connect(lambda: self.linuxth('pwd'))
        self.bt_unamer.clicked.connect(lambda: self.linuxth('uname -r'))
        self.bt_ifcong.clicked.connect(lambda: self.linuxth('ifconfig'))
        self.bt_lspci.clicked.connect(lambda: self.linuxth('lspci'))

        self.bt_stop.clicked.connect(lambda: self.cancel())

        self.bt_usb0.clicked.connect(lambda: self.usbth('minicom -D /dev/ttyUSB0'))
        self.bt_usb1.clicked.connect(lambda: self.usbth('minicom -D /dev/ttyUSB1'))
        self.bt_usb2.clicked.connect(lambda: self.usbth('minicom -D /dev/ttyUSB2'))
        self.bt_usb3.clicked.connect(lambda: self.usbth('minicom -D /dev/ttyUSB3'))
        self.bt_usb4.clicked.connect(lambda: self.usbth('minicom -D /dev/ttyUSB4'))
        self.bt_usb5.clicked.connect(lambda: self.usbth('minicom -D /dev/ttyUSB5'))
        self.bt_usb6.clicked.connect(lambda: self.usbth('minicom -D /dev/ttyUSB6'))
        self.bt_usb7.clicked.connect(lambda: self.usbth('minicom -D /dev/ttyUSB7'))
        self.bt_usb8.clicked.connect(lambda: self.usbth('minicom -D /dev/ttyUSB8'))
        self.bt_usb9.clicked.connect(lambda: self.usbth('minicom -D /dev/ttyUSB9'))

        self.Getip.clicked.connect(lambda: self.thread2(11, self.lineEdit_2, self.getip1))
        self.getip1.stateChanged.connect(lambda: self.thread2(0, 'fixture1', self.getip1))
        self.getip1_2.stateChanged.connect(lambda: self.thread2(1, 'fixture2', self.getip1_2))
        self.getip1_3.stateChanged.connect(lambda: self.thread2(2, 'fixture3', self.getip1_3))
        self.getip1_4.stateChanged.connect(lambda: self.thread2(3, 'fixture4', self.getip1_4))
        self.getip1_5.stateChanged.connect(lambda: self.thread2(4, 'fixture5', self.getip1_5))
        self.getip1_6.stateChanged.connect(lambda: self.thread2(5, 'fixture6', self.getip1_6))
        self.getip1_7.stateChanged.connect(lambda: self.thread2(6, 'fixture7', self.getip1_7))
        self.getip1_8.stateChanged.connect(lambda: self.thread2(7, 'fixture8', self.getip1_8))
        self.getip1_9.stateChanged.connect(lambda: self.thread2(8, 'fixture9', self.getip1_9))
        self.getip1_10.stateChanged.connect(lambda: self.thread2(9, 'fixture10', self.getip1_10))

    def threadw2(self):
        t1 = Thread(target=self.chk2)
        t1.start()

    def chk2(self):
        rutaip = os.path.isfile('%s/testgui/Fix/%s/bmcip.txt' % (directory, carpeta2))
        print(rutaip)
        while rutaip == False:
            rutaip = os.path.isfile('%s/testgui/Fix/%s/bmcip.txt' % (directory, carpeta2))
        file1 = open("%s/testgui/Fix/%s/bmcip.txt" % (directory, carpeta2), "r")
        ss = file1.readlines()[0]
        global ip
        ip = ss

    def threadw(self):
        t1 = Thread(target=self.chk)
        t1.start()

    def chk(self):
        rutaip = os.path.isfile('%s/testgui/Fix/%s/bmcip.txt' % (directory, carpeta))
        print(rutaip)
        while rutaip == False:
            rutaip = os.path.isfile('%s/testgui/Fix/%s/bmcip.txt' % (directory, carpeta))
        file1 = open("%s/testgui/Fix/%s/bmcip.txt" % (directory, carpeta), "r")
        ss = file1.readlines()[0]
        global ip
        ip = ss

    def thread2(self, num, carp, sts):
        t1 = Thread(target=self.ip_fix(num, carp, sts))
        t1.start()

    def ip_fix(self, num2, carp, sts):
        if sts.isChecked() == True:
            file1 = open("%s/log/golden_bmcmac.txt" % directory, "r")
            rr = file1.readlines()[num2]
            global mac
            mac = rr
            global carpeta
            carpeta = carp
            print(carpeta)
            os.system('tmux send-keys -t %s  "./scratch.sh -s %s -m %s" Enter' % (tmux, carp, rr))
            self.threadw()
        elif num2 == 11:
            global carpeta2
            carpeta2 = carp.text()
            os.system('tmux send-keys -t %s  "./scratch.sh -s %s -m %s" Enter' % (tmux, carpeta2, carpeta2))
            print(carpeta2)
            self.threadw2()
        elif sts.isChecked() == False:
            os.system('tmux send-keys -t %s  ^c' % tmux)

    def threadip(self, soc):
        t1 = Thread(target=self.solip(soc))
        t1.start()

    def solip(self, soc):
        uc = soc
        arch = "'ifconfig'"
        os.system('tmux send-keys -t %s  "/bin/python sol_cmd.py %s " %s ' % (tmux, uc, ip))
        os.system('tmux send-keys -t %s  " %s" Enter' % (tmux, arch))
#        #os.system('tmux send-keys -t %s  " %s " Enter' % ip)

    def bgcomth(self, soc):
        t1 = Thread(target=self.bgcom(soc))
        t1.start()

    def bgcom(self, soc):
        uc = soc
        arch = "'sol deactivate'"
        os.system('/bin/python3 ipymitool.py %s %s %s' % (tmux, arch, ip))

    def hilobg(self, arg):
        t1 = Thread(target=self.pytoolbg(arg))
        t1.start()

    def pytoolbg(self, arg):
        os.system('"ipmitool -I lanplus -H "%s ' % ip)
        os.system('" -U admin -P admin %s"' % arg)

    def hilo(self, arg, grep):
        t1 = Thread(target=self.pytoolgrep(arg, grep))
        t1.start()

    def pytoolgrep(self, arg, grep):
        argumento = arg
        gg = grep.text()
        os.system('tmux send-keys -t %s "ipmitool -I lanplus -H "%s ' % (tmux, ip))
        os.system('tmux send-keys -t %s " -U admin -P admin %s |grep %s" Enter' % (tmux, argumento, gg))

    def thcustom(self, carg):
        t1 = Thread(target=self.pytoolcustom(carg))
        t1.start()

    def pytoolcustom(self, carg):
        cusargumento = carg.text()
        os.system('tmux send-keys -t %s "ipmitool -I lanplus -H "%s ' % (tmux, ip))
        os.system('tmux send-keys -t %s " -U admin -P admin %s" Enter' % (tmux, cusargumento))

    def testth(self, bash, serial):
        t1 = Thread(target=self.test(bash, serial))
        t1.start()

    def test(self, bash, serial):
        seri = serial.text()
        os.chdir('%s/script' % directory)
        os.system('tmux send-keys -t %s "./%s -s %s" Enter' % (tmux, bash, seri))

    def linuxthip(self, command, grep):
        t1 = Thread(target=self.linuxip(command, grep))
        t1.start()

    def linuxip(self, command, grep):
        greep = grep.text()
        os.system('tmux send-keys -t %s "%s |grep %s" Enter' % (tmux, command, greep))

    def linuxthgp(self, command, grep):
        t1 = Thread(target=self.linuxgrp(command, grep))
        t1.start()

    def linuxgrp(self, command, grep):
        ping = grep.text()
        os.system('tmux send-keys -t %s "%s %s" Enter' % (tmux, command, ping))

    def usbth(self, ttyusb):
        t1 = Thread(target=self.usb(ttyusb))
        t1.start()

    def usb(self, ttyusb):
        os.system('tmux send-keys -t %s "%s" Enter' % (tmux, ttyusb))

    def linuxth(self, command):
        t1 = Thread(target=self.linux(command))
        t1.start()

    def linux(self, command):
        os.system('tmux send-keys -t %s "%s" Enter' % (tmux, command))

    def thread(self, arg):
        t1 = Thread(target=self.pytool(arg))
        t1.start()

    def pytool(self, arg):
        argumento = arg
        os.system('tmux send-keys -t %s "ipmitool -I lanplus -H "%s ' % (tmux, ip))
        os.system('tmux send-keys -t %s " -U admin -P admin %s" Enter' % (tmux, argumento))

    def cancel(self):
        os.system('tmux send-keys -t %s ^c' % tmux)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = window()
    my_app.show()
    sys.exit(app.exec_())
