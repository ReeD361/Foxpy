import os
import sys
import time
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from threading import *
import sqlite3
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow

fix = "fixture1"
#fix = sys.argv[1]
ruta = "/home/red361/Roms"
ruta_fix = "/home/red361/Roms/testgui/Fix/%s" % fix
sql = sqlite3.connect('%s/testgui/cook_book.db' % ruta)


class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        loadUi('book.ui', self)
        self.cb1()
        self.cb_model.activated.connect(lambda: self.cb2())
        self.unlock.clicked.connect(lambda: self.unlock_def())
        self.bt_see.clicked.connect(lambda: self.buscar())

    def block(self):
        status_txt = open('%s/status_fix.txt' % ruta_fix, "w")
        status_txt.write('Block')
        status_txt.close()

    def cb2(self):
        combo = self.cb_test
        card = self.cb_model.currentText()
        print(card)
        combo.clear()
        cur = sql.cursor()
        cur.execute("SELECT test FROM %s" % card)
        cur.execute('SELECT * FROM (SELECT test FROM %s)' % card)
        lis = cur.fetchall()
        for l in lis:
            combo.addItem(str(l[0]))
            print(l)
        cur.close()

    def cb1(self):
        combo = self.cb_model
        combo.clear()
        cur = sql.cursor()
        cur.execute("SELECT name FROM models")
        cur.execute('SELECT * FROM (SELECT name FROM models)')
        lis = cur.fetchall()
        for l in lis:
            combo.addItem(str(l[0]))
            print(l)
        cur.close()

    def unlock_def(self):
        fail = self.cb_test.currentText()
        type_fail = self.cb_type.currentText()
        no_employ = self.no_empleado.text()
        pss = self.password.text()
        solution = self.cause_edit.toPlainText()
        fecha = os.popen('date +%Y/%m/%d_%H%M%S').read().rstrip()
        if fail == '' or no_employ == '' or pss == '' or solution == '':
            self.status.setText("Error favor de rellenar todos los capos")
        else:
            cur = sql.cursor()
            cur.execute("INSERT INTO book VALUES (?,?,?,?,?,?)", (type_fail, no_employ, fecha, fail, solution, fix))
            sql.commit()
            cur.close()
            self.block()

    def buscar(self):
         cur = sql.cursor()
         sqlquery = "SELECT * FROM book LIMIT 20"
         self.ver.setRowCount(20)
         tablerow = 0
         for row in cur.execute(sqlquery):
                self.ver.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
                self.ver.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[3]))
                self.ver.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[4]))
                self.ver.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[5]))
                tablerow += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = window()
    mi_app.show()
    sys.exit(app.exec_())
