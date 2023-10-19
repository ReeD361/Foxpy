import os
import sys
import time
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from threading import *
import sqlite3
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

fix = "fixture1"
#fix = sys.argv[1]
ruta_primary = '/home/red361/Roms'


class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        loadUi('table.ui', self)
        self.ffix.setText(fix)
        self.bt_history.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.bt_failhistory.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.bt_yiel_global.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.bt_yiel_day.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.bt_metrics.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_5))
        self.histo()
        self.fail_histo()
        self.yield_g()
        self.yield_dxd()

    def histo(self):
        ruta = "%s/testgui/Fix/%s" % (ruta_primary, fix)
        sql = sqlite3.connect('%s/yield.db' % ruta)
        cur = sql.cursor()
        sqlquery = "SELECT * FROM history ORDER BY hour DESC LIMIT 50"
        self.history.setRowCount(50)
        tablerow = 0
        for row in cur.execute(sqlquery):
            self.history.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.history.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.history.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.history.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.history.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.history.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            tablerow += 1

    def fail_histo(self):
        ruta = "%s/testgui/Fix/%s" % (ruta_primary, fix)
        sql = sqlite3.connect('%s/yield.db' % ruta)
        cur = sql.cursor()
        sqlquery = "SELECT * FROM fail_history LIMIT 50"
        self.fai_history.setRowCount(50)
        tablerow = 0
        for row in cur.execute(sqlquery):
            self.fai_history.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.fai_history.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.fai_history.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            tablerow += 1

    def yield_g(self):
        ruta = "%s/testgui/Fix/%s" % (ruta_primary, fix)
        sql = sqlite3.connect('%s/yield.db' % ruta)
        cur = sql.cursor()
        sqlquery = "SELECT * FROM yield_global LIMIT 1"
        self.yield_global.setRowCount(1)
        tablerow = 0
        for row in cur.execute(sqlquery):
            self.yield_global.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.yield_global.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.yield_global.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.yield_global.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))

    def yield_dxd(self):
        ruta = "%s/testgui/Fix/%s" % (ruta_primary, fix)
        sql = sqlite3.connect('%s/yield.db' % ruta)
        cur = sql.cursor()
        sqlquery = "SELECT * FROM yielddxd LIMIT 50"
        self.yield_day.setRowCount(50)
        tablerow = 0
        for row in cur.execute(sqlquery):
            self.yield_day.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.yield_day.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.yield_day.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.yield_day.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            tablerow += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = window()
    mi_app.show()
    sys.exit(app.exec_())
