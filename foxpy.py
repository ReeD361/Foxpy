import os
import sys
import time
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from threading import *
import os
import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QScrollArea
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
import sqlite3
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow

ruta = "/home/red361/Roms"
fix_name1 = 'DoveFBT01'
fix_name2 = 'DoveFBT02'
fix_name3 = 'DoveFBT03'
fix_name4 = 'DoveFBT04'
fix_name5 = 'DoveFBT05'
fix_name6 = 'DoveFBT06'
fix_name7 = 'DoveFBT07'
fix_name8 = 'DoveFBT08'
fix_name9 = 'DoveFBT09'
fix_name10 = 'DoveFBT10'


class EmbTerminal(QtWidgets.QWidget):
    def __init__(self, tmux, parent=None):
        super(EmbTerminal, self).__init__(parent)
        self.tmux = tmux
        self.process = QtCore.QProcess(self)
        self.terminal = QtWidgets.QWidget(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.terminal)
        self.process.start('xterm', ['-into', str(int(self.winId())), '-g', '65x50',
                                     '-fs', '25', '-e', 'tmux', 'a', '-t', '%s' % tmux])
        self.setFixedSize(400, 130)


class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        loadUi('ZZZ2.ui', self)
        '''  '''
        self.connexion = sqlite3.connect('main_data')
        self.show_menu.clicked.connect(lambda: self.resise())
        self.bt_pxe.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_pxe))
        self.bt_test.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_test))
        self.bt_help.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.widget))
        self.bt_tbc.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.mp_mb))
        self.bt_fix_op.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.opc_fix))
        self.bt_test_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_autotest))
        self.checksub.stateChanged.connect(lambda: self.thrado())
        self.checkmp.stateChanged.connect(lambda: self.thrado())
        self.checkauto.stateChanged.connect(lambda: self.thrado())
        self.lg_bt.clicked.connect(self.thread1)
#        self.bt_test_2.clicked.connect(self.hilotest)
        ''' Subcards aqui declaro lo de subcards '''
        self.bt_res.clicked.connect(lambda: self.hilo(self.sn1, "1", "y"))
        self.bt_res_2.clicked.connect(lambda: self.hilo(self.sn2, "2", "y"))
        self.bt_res_3.clicked.connect(lambda: self.hilo(self.sn3, "3", "y"))
        self.bt_res_4.clicked.connect(lambda: self.hilo(self.sn4, "4", "y"))
        self.bt_res_5.clicked.connect(lambda: self.hilo(self.sn5, "5", "y"))
        self.bt_res_6.clicked.connect(lambda: self.hilo(self.sn6, "6", "y"))
        self.bt_res_7.clicked.connect(lambda: self.hilo(self.sn7, "7", "y"))
        self.bt_res_8.clicked.connect(lambda: self.hilo(self.sn8, "8", "y"))
        self.bt_res_9.clicked.connect(lambda: self.hilo(self.sn9, "9", "y"))
        self.bt_res_10.clicked.connect(lambda: self.hilo(self.sn10, "10", "y"))
        self.bt_nres.clicked.connect(lambda: self.hilo(self.sn1, "1", "n"))
        self.bt_nres_2.clicked.connect(lambda: self.hilo(self.sn2, "2", "n"))
        self.bt_nres_3.clicked.connect(lambda: self.hilo(self.sn3, "3", "n"))
        self.bt_nres_4.clicked.connect(lambda: self.hilo(self.sn4, "4", "n"))
        self.bt_nres_5.clicked.connect(lambda: self.hilo(self.sn5, "5", "n"))
        self.bt_nres_6.clicked.connect(lambda: self.hilo(self.sn6, "6", "n"))
        self.bt_nres_7.clicked.connect(lambda: self.hilo(self.sn7, "7", "n"))
        self.bt_nres_8.clicked.connect(lambda: self.hilo(self.sn8, "8", "n"))
        self.bt_nres_9.clicked.connect(lambda: self.hilo(self.sn9, "9", "n"))
        self.bt_nres_10.clicked.connect(lambda: self.hilo(self.sn10, "10", "n"))
        ''' Midplane manual aqui declaro midplane '''
        self.bt_yes.clicked.connect(lambda: self.hilo(self.msn1, "1", "y"))
        self.bt_yes_8.clicked.connect(lambda: self.hilo(self.msn2, "2", "y"))
        self.bt_yes_9.clicked.connect(lambda: self.hilo(self.msn3, "3", "y"))
        self.bt_yes_10.clicked.connect(lambda: self.hilo(self.msn4, "4", "y"))
        self.bt_yes_11.clicked.connect(lambda: self.hilo(self.msn5, "5", "y"))
        self.bt_yes_12.clicked.connect(lambda: self.hilo(self.msn6, "6", "y"))
        self.bt_yes_13.clicked.connect(lambda: self.hilo(self.msn7, "7", "y"))
        self.bt_yes_18.clicked.connect(lambda: self.hilo(self.msn8, "8", "y"))
        self.bt_yes_16.clicked.connect(lambda: self.hilo(self.msn9, "9", "y"))
        self.bt_yes_17.clicked.connect(lambda: self.hilo(self.msn10, "10", "y"))
        self.bt_no.clicked.connect(lambda: self.hilo(self.msn1, "1", "n"))
        self.bt_no_8.clicked.connect(lambda: self.hilo(self.msn2, "2", "n"))
        self.bt_no_9.clicked.connect(lambda: self.hilo(self.msn3, "3", "n"))
        self.bt_no_10.clicked.connect(lambda: self.hilo(self.msn4, "4", "n"))
        self.bt_no_11.clicked.connect(lambda: self.hilo(self.msn5, "5", "n"))
        self.bt_no_12.clicked.connect(lambda: self.hilo(self.msn6, "6", "n"))
        self.bt_no_13.clicked.connect(lambda: self.hilo(self.msn7, "7", "n"))
        self.bt_no_18.clicked.connect(lambda: self.hilo(self.msn8, "8", "n"))
        self.bt_no_17.clicked.connect(lambda: self.hilo(self.msn9, "9", "n"))
        self.bt_no_16.clicked.connect(lambda: self.hilo(self.msn10, "10", "n"))
        ''' Towers Auto Hanuman en estat parte declaro lo  que van a hacer los botones al ser precionados '''
        self.nt_start.clicked.connect(lambda: self.start_auto('1', 'start'))
        self.nt_start_2.clicked.connect(lambda: self.start_auto('2', 'start'))
        self.nt_start_3.clicked.connect(lambda: self.start_auto('3', 'start'))
        self.nt_start_7.clicked.connect(lambda: self.start_auto('4', 'start'))
        self.nt_start_8.clicked.connect(lambda: self.start_auto('5', 'start'))
        self.nt_start_5.clicked.connect(lambda: self.start_auto('6', 'start'))
        self.nt_start_10.clicked.connect(lambda: self.start_auto('7', 'start'))
        self.nt_start_12.clicked.connect(lambda: self.start_auto('8', 'start'))
        self.nt_start_13.clicked.connect(lambda: self.start_auto('9', 'start'))
        self.nt_see.clicked.connect(lambda: self.thread('1'))
        self.nt_see_2.clicked.connect(lambda: self.thread('2'))
        self.nt_see_3.clicked.connect(lambda: self.thread('3'))
        self.nt_see_7.clicked.connect(lambda: self.thread('4'))
        self.nt_see_8.clicked.connect(lambda: self.thread('5'))
        self.nt_see_5.clicked.connect(lambda: self.thread('6'))
        self.nt_see_10.clicked.connect(lambda: self.thread('7'))
        self.nt_see_12.clicked.connect(lambda: self.thread('8'))
        self.nt_see_13.clicked.connect(lambda: self.thread('9'))
        self.nt_stop.clicked.connect(lambda: self.start_auto('1', 'stop'))
        self.nt_stop_2.clicked.connect(lambda: self.start_auto('2', 'stop'))
        self.nt_stop_3.clicked.connect(lambda: self.start_auto('3', 'stop'))
        self.nt_stop_7.clicked.connect(lambda: self.start_auto('4', 'stop'))
        self.nt_stop_8.clicked.connect(lambda: self.start_auto('5', 'stop'))
        self.nt_stop_5.clicked.connect(lambda: self.start_auto('6', 'stop'))
        self.nt_stop_10.clicked.connect(lambda: self.start_auto('7', 'stop'))
        self.nt_stop_12.clicked.connect(lambda: self.start_auto('8', 'stop'))
        self.nt_stop_13.clicked.connect(lambda: self.start_auto('9', 'stop'))
        self.chk_nt_status.stateChanged.connect(lambda: self.chk_auto('1', 'non-sfc', self.chk_nt_status))
        self.chk_nt_status_2.stateChanged.connect(lambda: self.chk_auto('2', 'non-sfc', self.chk_nt_status_2))
        self.chk_nt_status_3.stateChanged.connect(lambda: self.chk_auto('3', 'non-sfc', self.chk_nt_status_3))
        self.chk_nt_status_7.stateChanged.connect(lambda: self.chk_auto('4', 'non-sfc', self.chk_nt_status_7))
        self.chk_nt_status_8.stateChanged.connect(lambda: self.chk_auto('5', 'non-sfc', self.chk_nt_status_8))
        self.chk_nt_status_5.stateChanged.connect(lambda: self.chk_auto('6', 'non-sfc', self.chk_nt_status_5))
        self.chk_nt_status_10.stateChanged.connect(lambda: self.chk_auto('7', 'non-sfc', self.chk_nt_status_10))
        self.chk_nt_status_12.stateChanged.connect(lambda: self.chk_auto('8', 'non-sfc', self.chk_nt_status_12))
        self.chk_nt_status_13.stateChanged.connect(lambda: self.chk_auto('9', 'non-sfc', self.chk_nt_status_3))
        self.nt_stats.clicked.connect(lambda: self.thread_metrics('fixture1', 'metric.py'))
        self.nt_stats_2.clicked.connect(lambda: self.thread_metrics('fixture2', 'metric.py'))
        self.nt_stats_3.clicked.connect(lambda: self.thread_metrics('fixture3', 'metric.py'))
        self.nt_stats_7.clicked.connect(lambda: self.thread_metrics('fixture4', 'metric.py'))
        self.nt_stats_8.clicked.connect(lambda: self.thread_metrics('fixture5', 'metric.py'))
        self.nt_stats_5.clicked.connect(lambda: self.thread_metrics('fixture6', 'metric.py'))
        self.nt_stats_10.clicked.connect(lambda: self.thread_metrics('fixture7', 'metric.py'))
        self.nt_stats_12.clicked.connect(lambda: self.thread_metrics('fixture8', 'metric.py'))
        self.nt_stats_13.clicked.connect(lambda: self.thread_metrics('fixture9', 'metric.py'))
        self.nt_opc.clicked.connect(lambda: self.block_unlock(self.led_auto, 'fixture1', self.st_1))
        self.nt_opc_2.clicked.connect(lambda: self.block_unlock(self.led_auto_2, 'fixture2', self.st_2))
        self.nt_opc_3.clicked.connect(lambda: self.block_unlock(self.led_auto_3, 'fixture3', self.st_3))
        self.nt_opc_7.clicked.connect(lambda: self.block_unlock(self.led_auto_4, 'fixture4', self.st_4))
        self.nt_opc_8.clicked.connect(lambda: self.block_unlock(self.led_auto_5, 'fixture5', self.st_5))
        self.nt_opc_5.clicked.connect(lambda: self.block_unlock(self.led_auto_6, 'fixture6', self.st_6))
        self.nt_opc_10.clicked.connect(lambda: self.block_unlock(self.led_auto_7, 'fixture7', self.st_7))
        self.nt_opc_12.clicked.connect(lambda: self.block_unlock(self.led_auto_8, 'fixture8', self.st_8))
        self.nt_opc_13.clicked.connect(lambda: self.block_unlock(self.led_auto_9, 'fixture9', self.st_9))
        self.nt_fixt.clicked.connect(lambda: self.thread_metrics('fixture1', "Biti.py"))
        self.nt_fixt_2.clicked.connect(lambda: self.thread_metrics('fixture2', "Biti.py"))
        self.nt_fixt_3.clicked.connect(lambda: self.thread_metrics('fixture3', "Biti.py"))
        self.nt_fixt_7.clicked.connect(lambda: self.thread_metrics('fixture4', "Biti.py"))
        self.nt_fixt_8.clicked.connect(lambda: self.thread_metrics('fixture5', "Biti.py"))
        self.nt_fixt_5.clicked.connect(lambda: self.thread_metrics('fixture6', "Biti.py"))
        self.nt_fixt_10.clicked.connect(lambda: self.thread_metrics('fixture7', "Biti.py"))
        self.nt_fixt_12.clicked.connect(lambda: self.thread_metrics('fixture8', "Biti.py"))
        self.nt_fixt_100.clicked.connect(lambda: self.thread_metrics('fixture9', "Biti.py"))
        self.mb_unlck.clicked.connect(lambda: self.thread_metrics('fixture1', "book.py"))
        self.mb_unlck_2.clicked.connect(lambda: self.thread_metrics('fixture2', "book.py"))
        self.mb_unlck_3.clicked.connect(lambda: self.thread_metrics('fixture3', "book.py"))
        self.mb_unlck_4.clicked.connect(lambda: self.thread_metrics('fixture4', "book.py"))
        self.mb_unlck_5.clicked.connect(lambda: self.thread_metrics('fixture5', "book.py"))
        self.mb_unlck_6.clicked.connect(lambda: self.thread_metrics('fixture6', "book.py"))
        self.mb_unlck_7.clicked.connect(lambda: self.thread_metrics('fixture7', "book.py"))
        self.mb_unlck_8.clicked.connect(lambda: self.thread_metrics('fixture8', "book.py"))
        self.mb_unlck_9.clicked.connect(lambda: self.thread_metrics('fixture9', "book.py"))

        '''  '''

    def resise(self):
        if True:
            width = self.fr_opc.width()
            normal = 0
            if width == 0:
                extender = 300
            else:
                extender = normal
        self.animacion = QPropertyAnimation(self.fr_opc, b"maximumWidth")
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setDuration(500)
        self.animacion.setEasingCurve(QEasingCurve.OutInBack)
        self.animacion.start()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_1:
            self.thread("1")
        elif e.key() == Qt.Key_2:
            self.thread("2")
        elif e.key() == Qt.Key_3:
            self.thread("3")
        elif e.key() == Qt.Key_4:
            self.thread("4")
        elif e.key() == Qt.Key_5:
            self.thread("5")
        elif e.key() == Qt.Key_6:
            self.thread("6")
        elif e.key() == Qt.Key_7:
            self.thread("7")
        elif e.key() == Qt.Key_8:
            self.thread("8")
        elif e.key() == Qt.Key_9:
            self.thread("9")
        elif e.key() == Qt.Key_0:
            self.thread("10")

    def thread_metrics(self, nc2, program):
        t1 = Thread(target=self.metrics(nc2, program))
        t1.start()

    def metrics(self, nc2, program):
        os.system('gnome-terminal -- /bin/python3 %s %s' % (program, nc2))

    def thread(self, nc2):
        t1 = Thread(target=self.consola(nc2))
        t1.start()

    def consola(self, nc2):
        os.system('gnome-terminal -- tmux a -t %s' % nc2)

    def thread1(self):
        print('ok')
        t1 = Thread(target=self.test)
        t1.start()

    def hilotest(self):
        t1 = Thread(target=self.testMPMB)
        t1.start()

    def hilo(self, sn, nu, res):
        print(nu)
        kk = sn.text()
        print(kk)
        t1 = Thread(target=self.cancel(sn, nu, res))
        t1.start()

    def cancel(self, sn, tm, res):
        serial = sn.text()
        failed = os.path.isfile('%s/log/%s/fail.log' % (ruta, serial))
        led_bl = os.path.isfile("%s/log/%s/led_blue.log" % (ruta, serial))
        led_pwr = os.path.isfile("%s/log/%s/led_power.log" % (ruta, serial))
        led_gr = os.path.isfile("%s/log/%s/led_green.log" % (ruta, serial))
        usb_test = os.path.isfile("%s/log/%s/usb.log" % (ruta, serial))
        retest_dir = os.path.isfile("%s/log/%s/retest.log" % (ruta, serial))
        if serial == "":
            print("n")
        elif led_bl or led_pwr or led_gr or retest_dir and res == "y":
            os.system('tmux send-keys -t %s "y" Enter' % tm)
        elif led_bl or led_pwr or led_gr or retest_dir and res == "n":
            os.system('tmux send-keys -t %s "n" Enter' % tm)
        elif usb_test:
            os.system('tmux send-keys -t %s "y" Enter' % tm)
        elif failed and res == 'y':
            os.system('rm -rf %s/log/%s/fail.log' % (ruta, serial))
            os.system('rm -rf %s/log/%s/running.log' % (ruta, serial))
            os.system('tmux send-keys -t %s "up" Enter' % tm)
        elif sn != "" and res == "n":
            subprocess.Popen(['tmux', 'send-keys', '-t', tm, '^c', 'Enter'])

    def test(self):
        serials = {self.sn1: "1", self.sn2: "2", self.sn3: "3", self.sn4: "4", self.sn5: "5", self.sn6: "6",
                   self.sn7: "7", self.sn8: "8", self.sn9: "9", self.sn10: "10"}
        for ser, num in serials.items():
            serial = ser.text()
            lss = len(serial)
            mss = serial[:9]
            block = os.path.isfile('%s/testgui/Fix/fixture%s/Block.log' % (ruta, num))
            runing = os.path.isdir('%s/log/%s/running.log' % (ruta, serial))
            #            retest = os.path.isdir('%s/testgui/log/%s/retest.log' % (ruta, serial))
            #            failedlog = os.path.isdir('%s/testgui/log/%s/fail.log' % (ruta, serial))
            pp = os.path.isdir('%s/config/%s' % (ruta, mss))
            if serial != '' and pp and lss == 17 and runing == False and block == False:
                print('okokok')
                subprocess.Popen(['tmux', 'new', '-d', '-s', num])
                os.system('tmux send-keys -t %s "cd %s/script" Enter ' % (num, ruta))
                time.sleep(1)
                subprocess.Popen(['tmux', 'send-keys', '-t', num, './test.sh -s', serial, 'Enter'])
                time.sleep(1)
                subprocess.Popen(['tmux', 'send-keys', '-t', num, './test.sh -s', serial, 'Enter'])
            elif serial != '' and pp and lss == 17 and runing == False and block:
                print('block')
                subprocess.Popen(['tmux', 'new', '-d', '-s', num])
                os.system('tmux send-keys -t %s "cd %s/script" Enter ' % (num, ruta))
                time.sleep(1)
                subprocess.Popen(['tmux', 'send-keys', '-t', num, './test.sh -s', serial, ' ', '-m', 'Enter'])
                time.sleep(1)
                subprocess.Popen(['tmux', 'send-keys', '-t', num, num, 'Enter'])

    def testMPMB(self):
        mac_1 = self.mc1.text()
        mac_2 = self.mc2.text()
        mac_3 = self.mc3.text()
        mac_4 = self.mc4.text()
        mac_5 = self.mc5.text()
        mac_6 = self.mc6.text()
        mac_7 = self.mc7.text()
        mac_8 = self.mc8.text()
        mac_9 = self.mc9.text()
        mac_10 = self.mc10.text()
        seriales = {self.msn1: "%s1" % mac_1, self.msn2: "%s2" % mac_2, self.msn3: "%s3" % mac_3,
                    self.msn4: "%s4" % mac_4, self.msn5: "%s5" % mac_5, self.msn6: "%s6" % mac_6,
                    self.msn7: "%s7" % mac_7, self.msn8: "%s8" % mac_8, self.msn9: "%s9" % mac_9,
                    self.msn10: "%s10" % mac_10}
        for ser, num in seriales.items():
            bmcmac = num[:12]
            fixtmux = num[-1]
            print(fixtmux)
            print(bmcmac)
            serial = ser.text()
            seri_length = len(serial)
            sku_model = serial[:9]
            runing = os.path.isfile('%s/log/%s/running.log' % (ruta, serial))
            #            retest = os.path.isfile('%s/testgui/log/%s/retest.log' % (ruta, serial))
            #            failedlog = os.path.isfile('%s/testgui/log/%s/fail.log' % (ruta, serial))
            sku_exist = os.path.isdir('%s/config/%s' % (ruta, sku_model))
            sku_file = os.path.isfile('%s/config/SKU/%s_sku_coonfig' % (ruta, sku_model))
            if serial != '' and sku_exist == True and seri_length == 17 and runing == False and bmcmac != '':
                subprocess.Popen(['tmux', 'new', '-d', '-s', fixtmux])
                os.system('tmux send-keys -t %s "cd %s/testgui" Enter ' % (fixtmux, ruta))
                time.sleep(1)
                os.system(
                    'tmux send-keys -t %s "/bin/python3 expect.py %s %s %s" Enter ' % (fixtmux, serial, bmcmac, num))
                time.sleep(1)
            elif serial != '' and sku_file == True and seri_length == 17 and runing == False:
                subprocess.Popen(['tmux', 'new', '-d', '-s', fixtmux])
                os.system('tmux send-keys -t %s "cd %s/testgui" Enter ' % (fixtmux, ruta))
                time.sleep(1)
                os.system(
                    'tmux send-keys -t %s "/bin/python3 expect.py %s %s %s" Enter ' % (fixtmux, serial, bmcmac, num))
                time.sleep(1)

    def chk_auto(self, fixtmux, select, chk):
        if select == 'non-sfc' and chk.isChecked():
            print('non_yeah')
            os.system("tmux send-keys -t %s ^c ^c" % fixtmux)
            os.system('tmux send-keys -t %s "cd %s/fix_auto/fixture%s" Enter ' % (fixtmux, ruta, fixtmux))
            os.system('tmux send-keys -t %s "./FCTHostControl -f %s -m" Enter ' % (fixtmux, fixtmux))
            os.system('tmux send-keys -t %s Down Down Enter ')
        else:
            os.system('tmux send-keys -t %s ^c ^c' % fixtmux)
            subprocess.Popen(['tmux', 'new', '-d', '-s', fixtmux])
            os.system('tmux send-keys -t %s "cd %s/script" Enter ' % (fixtmux, ruta))
            os.system('tmux send-keys -t %s "./FCTHostControl -f %s" Enter ' % (fixtmux, fixtmux))
            os.system('tmux send-keys -t %s Down Down Enter ')

    def start_auto(self, fixtmux, select):
        if select == 'start':
            subprocess.Popen(['tmux', 'new', '-d', '-s', fixtmux])
            time.sleep(1)
            os.system('tmux send-keys -t %s "cd %s/fix_auto/fixture%s" Enter ' % (fixtmux, ruta, fixtmux))
            os.system('tmux send-keys -t %s "./FCTHostControl -f %s" Enter ' % (fixtmux, fixtmux))
            os.system('tmux send-keys -t %s Down Down Enter ' % fixtmux)
        elif select == 'stop':
            os.system('tmux send-keys -t %s ^c ^c' % fixtmux)

    def thrado(self):
        t1 = Thread(target=self.Operation)
        t1.start()

    def temp_nitro(self, sn, fix_folder, show_temp):
        chk_temp = os.path.isfile('%s/testgui/Fix/%s/%s/temp_comp.txt' % (ruta, fix_folder, sn))
        sn_temp = os.path.isfile('%s/log/%s/temp_foxpy.txt' % (ruta, sn))
        temp_val = 'null'
        temp_comp = 'null'
        temp_comp_int = 'null'
        if not chk_temp:
            os.popen('touch %s/testgui/Fix/%s/%s/temp_comp.txt' % (ruta, fix_folder, sn)).read()
            bmcip = os.popen('cat %s/testgui/Fix/%s/bmcip.txt' % (ruta, fix_folder)).read()
            os.system('/bin/python3 temp_monitor.py %s %s %s %s' % (get_sn, bmcip, '3', fix_folder))
            show_temp.setText("boot")
        elif chk_temp and sn_temp:
            temp_comp = os.popen('cat %s/testgui/Fix/%s/%s/temp_comp.txt' % (ruta, fix_folder, sn)).read()
            temp_val = os.popen('cat %s/log/%s/temp_foxpy.txt' % (ruta, sn)).read()
            temp_comp_int = int(temp_comp)
        else:
            pass

        if temp_comp != temp_val:
            show_temp.setText(temp_val)
            os.system('echo "%s" >> %s/testgui/Fix/%s/%s/temp_comp.txt' % (temp_val, ruta, fix_folder, sn))
        elif temp_comp_int >= 75:
            show_temp.setStyleSheet("background-color: red")
            show_temp.setText(temp_comp)
        elif temp_comp_int <= 75 and temp_comp_int != 0:
            show_temp.setStyleSheet("background-color: blue")
            show_temp.setText(temp_comp)
        elif temp_comp_int == 0:
            show_temp.setText("Turn Off")
        elif temp_comp == temp_val:
            pass

    def block_unlock(self, auto__led, fix, term_out):
        existe = os.path.isfile('%s/testgui/Fix/%s/status_fix.txt' % (ruta, fix))
        reead = os.popen('cat %s/testgui/Fix/%s/status_fix.txt' % (ruta, fix)).read().rstrip()
        print(reead, existe)
        fixtmux = fix[7]
        print(fixtmux)
        if term_out == '0':
            pass
        else:
            term_out.addWidget(EmbTerminal(fixtmux))

        if not existe:
            os.system('touch %s/testgui/Fix/%s/status_fix.txt' % (ruta, fix))

        if reead == "Block":
            auto__led.setText("Block")
            auto__led.setStyleSheet("background-color: rgb(255, 0, 0);")
            os.system('tmux send-keys -t %s ^z ^c' % fixtmux)
            os.system('tmux send-keys -t %s "cd %s/fix_auto/fixture%s" Enter ' % (fixtmux, ruta, fixtmux))
            os.system('tmux send-keys -t %s "./FCTHostControl -f %s -m" Enter ' % (fixtmux, fixtmux))
            os.system('tmux send-keys -t %s Down Down Enter ')
        elif reead == "Out":
            auto__led.setText("Out")
            auto__led.setStyleSheet("background-color: rgb(255, 255, 0); color: black")
            os.system('tmux send-keys -t %s ^z ^c' % fixtmux)
            os.system('tmux send-keys -t %s "cd %s/fix_auto/fixture%s" Enter ' % (fixtmux, ruta, fixtmux))
            os.system('tmux send-keys -t %s "./FCTHostControl -f %s -m" Enter ' % (fixtmux, fixtmux))
            os.system('tmux send-keys -t %s Down Down Enter ')
        else:
            auto__led.setStyleSheet("background-color: rgb(0, 255, 0);")
            auto__led.setText("Ok")

    def status1(self, rt, ftw, num):
        tserial = rt.text()
        lss = len(tserial)
        mss = tserial[:9]
        block = os.path.isfile('%s/testgui/Fix/fixture%s/Block.log' % (ruta, num))
        pc = os.path.isfile('%s/' % ruta)
        pc = os.path.isfile('%s/log/%s/rete.log' % (ruta, tserial))
        pd = os.path.isdir('%s/config/%s' % (ruta, mss))
        runing = os.path.isfile('%s/log/%s/running.log' % (ruta, tserial))
        skuh = os.path.isfile('%s/config/SKU/%s_sku_config' % (ruta, tserial))
        pp = os.path.isfile('%s/log/%s/PASS.log' % (ruta, tserial))
        ph = os.path.isfile('%s/log/%s/fail.log' % (ruta, tserial))
        if block:
            ftw.setText('Block')
        elif tserial == '':
            ftw.setText('Ready')
        elif not True == skuh and not True == pd or lss != 17:
            ftw.setText('Bad SN')
        elif pc:
            ftw.setText('Retest o fallar')
        elif pp:
            ftw.setText('PASS')
            time.sleep(5)
            rt.setText("")
        elif ph:
            ftw.setText('FAIL')
            self.pushButton.setText('a')
        elif runing:
            ftw.setText('Running')
        else:
            ftw.setText('ready test')

    def status2(self, rt, ftw, mac):
        tserial = rt.text()
        textmac = mac.text()
        lenmac = len(textmac)
        lss = len(tserial)
        mss = tserial[:9]
        retest_dir = os.path.isfile("%s/log/%s/retest.log" % (ruta, tserial))
        pd = os.path.isdir('%s/config/%s' % (ruta, mss))
        skuh = os.path.isfile('%s/config/SKU/%s_sku_config' % (ruta, mss))
        if tserial == '':
            ftw.setText('Ready')
        elif not True == skuh and not True == pd or lss != 17:
            ftw.setText('Bad SN')
        elif textmac == '' or lenmac < 12:
            ftw.setText('input valid Mac')
        elif retest_dir:
            ftw.setText('Beging?')
        else:
            ftw.setText('Ready')

    def st_auto(self, sn_out, status_out, fix_carpet, bg_color, yield_st, temp_lb, led_status):
        get_sn = os.popen("ls -ltr %s/testgui/Fix/%s|grep '^d'| tail -1|awk '{print $9}'" % (ruta, fix_carpet)).read()
        get_sn = get_sn.rstrip()
        get_status = 'null'
        run_status = 'null'
        sumary_status = 'null'
        get_comp = 'null'
        status_exist = os.path.isfile('%s/log/%s/test_item' % (ruta, get_sn))
        comp_exist = os.path.isfile('%s/testgui/Fix/%s/%s/comp.txt' % (ruta, fix_carpet, get_sn))
        if not comp_exist:
            os.system('echo "" >> %s/testgui/Fix/%s/%s/comp.txt' % (ruta, fix_carpet, get_sn))
            sn_out.setText(get_sn)
            os.system('cp -r %s/testgui/Fix/%s/%s %s/log' % (ruta, fix_carpet, get_sn, ruta))
            bg_color.setStyleSheet("background-color: white")
            status_out.setText('Starting')
            print('start')
        elif comp_exist and status_exist:
            sn_out.setText(get_sn)
            get_status = os.popen("tail -1 %s/log/%s/test_item |awk '{print $1}'" % (ruta, get_sn)).read().rstrip()
            get_comp = os.popen(
                "tail -1 %s/testgui/Fix/%s/%s/comp.txt |awk '{print $1}'" % (ruta, fix_carpet, get_sn)).read().rstrip()
            sumary_status = os.popen(
                "tail -1 %s/log/%s/summary_table.conf |awk '{print $4}'" % (ruta, get_sn)).read().rstrip()
            run_status = os.popen("tail -1 %s/log/%s/run_status |awk '{print $1}'" % (ruta, get_sn)).read().rstrip()
        else:
            pass

        if sumary_status == 'FAILED':
            status_out.setText('FAIL')
            os.system("rm -rf %s/log/FAIL/%s" % (ruta, get_sn))
            os.system("mv %s/log/%s  %s/log/FAIL" % (ruta, get_sn, ruta))
            bg_color.setStyleSheet("background-color: red")
            os.system('/bin/python3 yielddb_fail.py %s %s %s' % (get_sn, fix_carpet, get_status))
            self.block_unlock(led_status, fix_carpet, '0')
            time.sleep(1)
            yield_rd = os.popen(
                "tail -1 %s/testgui/Fix/%s/yield_per.txt |awk '{print $1}'" % (ruta, fix_carpet)).read().rstrip()
            yield_st.setText(yield_rd)
            os.system('rm -rf %s/testui/Fix/%s/%s' % (ruta, fix_carpet, get_sn))
        elif run_status == 'PASS' and get_status == '':
            status_out.setText("PASS")
            os.system("rm -rf %s/log/PASS/%s" % (ruta, get_sn))
            os.system("mv %s/log/%s  %s/log/PASS" % (ruta, get_sn, ruta))
            bg_color.setStyleSheet("background-color: green")
            os.system('/bin/python3 yielddb.py %s %s' % (get_sn, fix_carpet))
            self.block_unlock(led_status, fix_carpet, '0')
            time.sleep(1)
            yield_rd = os.popen(
                "tail -1 %s/testgui/Fix/%s/yield_per.txt |awk '{print $1}'" % (ruta, fix_carpet)).read().rstrip()
            yield_st.setText(yield_rd)
            os.system('rm -rf %s/testui/Fix/%s/%s' % (ruta, fix_carpet, get_sn))
        elif get_status == get_comp and get_status != 'null':
            pass
        elif get_status != get_comp:
            print(get_status, get_comp)
            status_out.setText(get_status)
            os.system('echo "%s" >> %s/testgui/Fix/%s/%s/comp.txt' % (get_status, ruta, fix_carpet, get_sn))
#        self.temp_nitro(get_sn, fix_carpet, temp_lb)

    def Operation(self):
        while self.checksub.isChecked():
            self.status1(self.sn1, self.status, '1')
            self.status1(self.sn2, self.status_2, '2')
            self.status1(self.sn3, self.status_3, '3')
            self.status1(self.sn4, self.status_4, '3')
            self.status1(self.sn5, self.status_5, '3')
            self.status1(self.sn6, self.status_6, '3')
            self.status1(self.sn7, self.status_7, '3')
            self.status1(self.sn8, self.status_8, '3')
            self.status1(self.sn9, self.status_9, '3')
            self.status1(self.sn10, self.status_10, '10')
        while self.checkmp.isChecked():
            self.status2(self.msn1, self.status_mpmb, self.mc1)
            self.status2(self.msn2, self.status_mpmb_2, self.mc2)
            self.status2(self.msn3, self.status_mpmb_3, self.mc3)
            self.status2(self.msn4, self.status_mpmb_4, self.mc4)
            self.status2(self.msn5, self.status_mpmb_5, self.mc5)
            self.status2(self.msn6, self.status_mpmb_6, self.mc6)
            self.status2(self.msn7, self.status_mpmb_7, self.mc7)
            self.status2(self.msn8, self.status_mpmb_8, self.mc8)
            self.status2(self.msn9, self.status_mpmb_9, self.mc9)
            self.status2(self.msn10, self.status_mpmb_10, self.mc10)
        while self.checkauto.isChecked():
            self.st_auto(self.nt_sn_auto, self.nt_status, 'fixture1', self.frame_2, self.nt_yiel, self.temp_1, self.led_auto)
            self.st_auto(self.nt_sn_auto_2, self.nt_status_2, 'fixture2', self.frame_3, self.nt_yiel_2, self.temp_2, self.led_auto_2)
            self.st_auto(self.nt_sn_auto_3, self.nt_status_3, 'fixture3', self.frame_4, self.nt_yiel_3, self.temp_3, self.led_auto_3)
            self.st_auto(self.nt_sn_auto_7, self.nt_status_7, 'fixture4', self.frame_6, self.nt_yiel_7, self.temp_4, self.led_auto_4)
            self.st_auto(self.nt_sn_auto_8, self.nt_status_8, 'fixture5', self.frame_7, self.nt_yiel_8, self.temp_5, self.led_auto_5)
            self.st_auto(self.nt_sn_auto_5, self.nt_status_5, 'fixture6', self.frame_5, self.nt_yiel_5, self.temp_6, self.led_auto_6)
            self.st_auto(self.nt_sn_auto_10, self.nt_status_10, 'fixture7', self.frame_8, self.nt_yiel_10, self.temp_7, self.led_auto_7)
            self.st_auto(self.nt_sn_auto_12, self.nt_status_12, 'fixture8', self.frame_9, self.nt_yiel_12, self.temp_8, self.led_auto_8)
            self.st_auto(self.nt_sn_auto_13, self.nt_status_13, 'fixture9', self.frame_10, self.nt_yiel_13, self.temp_9, self.led_auto_9)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = window()
    mi_app.show()
    sys.exit(app.exec_())
