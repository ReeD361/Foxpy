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
sql = sqlite3.connect('%s/biti.db' % ruta_fix)


class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        loadUi('bitacora.ui', self)
        ""
        self.fix.setText(fix)
        self.bt_write.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.bt_ver.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.bt_out_pg.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.bt_search_pg.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.bt_enviar.clicked.connect(lambda: self.obbtener_texto())
        self.bt_consultar.clicked.connect(lambda: self.mostrar_text())
        self.bt_out.clicked.connect(lambda: self.obbtener_out())
        self.bt_ver_3.clicked.connect(lambda: self.mostrar_out())
        self.bt_btl.clicked.connect(lambda: self.regresar_out())
        self.bt_consultar_2.clicked.connect(lambda: self.buscar())
        self.status()

    def status(self):
        combo = self.comboBox_2
        combo.clear()
        cur = sql.cursor()
        cur.execute("SELECT fecha FROM bitacora")
        cur.execute('SELECT * FROM (SELECT fecha FROM bitacora ORDER BY fecha DESC LIMIT 6)')
        lis = cur.fetchall()
        for l in lis:
            combo.addItem(str(l[0]))
            print(l)
        cur.close()

    def obbtener_texto(self):
        text_b = self.text_bbox.toPlainText()
        usr = self.lineEdit_2.text()
        turno = self.comboBox.currentText()
        print(usr, turno)
        fecha = os.popen('date +%Y/%m/%d_%H%M%S').read().rstrip()
        cur = sql.cursor()
        cur.execute("INSERT INTO bitacora VALUES (?,?,?,?)", (fecha, text_b, usr, turno))
        sql.commit()
        cur.close()
        self.status()
        print(text_b)

    def mostrar_text_old(self):
        cur = sql.cursor()
        cur.execute('SELECT bita FROM bitacora WHERE bita = (SELECT bita FROM bitacora ORDER BY fecha DESC LIMIT 1)')
        aa = str(cur.fetchone()[0])
        cur.execute('SELECT fecha FROM bitacora WHERE fecha = (SELECT fecha FROM bitacora ORDER BY fecha DESC LIMIT 1)')
        fecha = str(cur.fetchone()[0])
        cur.execute('SELECT user FROM bitacora WHERE user = (SELECT user FROM bitacora ORDER BY fecha DESC LIMIT 1)')
        usr = str(cur.fetchone()[0])
        print(fecha)
        sql.commit()
        cur.close()
        print(aa)
        self.text_out.setText(aa)
        self.fecha_ver.setText(fecha)
        self.usr_ver.setText(usr)

    def mostrar_text(self):
        cur = sql.cursor()
        fate = self.comboBox_2.currentText()
        print(fate)
        cur.execute('SELECT bita FROM bitacora WHERE fecha = ?', (fate,))
        aa = str(cur.fetchone()[0])
        cur.execute('SELECT fecha FROM bitacora WHERE fecha = ? ', (fate,))
        fecha = str(cur.fetchone()[0])
        cur.execute('SELECT user FROM bitacora WHERE fecha = ?', (fate,))
        usr = str(cur.fetchone()[0])
        sql.commit()
        cur.close()
        print(aa)
        self.text_out.setText(aa)
        self.fecha_ver.setText(fecha)
        self.usr_ver.setText(usr)

    def obbtener_out(self):
        text_b = self.text_bbox_2.toPlainText()
        usr = self.lineEdit_8.text()
        turno = self.comboBox_10.currentText()
        fecha = os.popen('date +%Y%m%d_%H%M%S').read().rstrip()
        if text_b != '' and usr != "":
            cur = sql.cursor()
            cur.execute("INSERT INTO out VALUES (?,?,?,?)", (fecha, text_b, usr, turno))
            sql.commit()
            cur.close()
            status_txt = open('%s/status_fix.txt' % ruta_fix, "w")
            status_txt.write('Out')
            status_txt.close()
            self.st_enviar_2.setText('DB actualizada')
        else:
            self.st_enviar_2.setText('Error de datos')
        print(text_b)

    def mostrar_out(self):
        cur = sql.cursor()
        cur.execute('SELECT cause FROM out WHERE cause = (SELECT cause FROM out ORDER BY fecha DESC LIMIT 1)')
        aa = str(cur.fetchone()[0])
        sql.commit()
        cur.close()
        print(aa)
        self.text_out_2.setText(aa)

    def regresar_out(self):
        status_txt = open('%s/status_fix.txt' % ruta_fix, "w")
        status_txt.write('')
        status_txt.close()
        self.st_enviar_2.setText('Vuelve a linea')

    def buscar(self):
        cur = sql.cursor()
        sqlquery = "SELECT * FROM bitacora LIMIT 20"
        self.buscar_db.setRowCount(20)
        tablerow = 0
        for row in cur.execute(sqlquery):
            self.buscar_db.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.buscar_db.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.buscar_db.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.buscar_db.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            tablerow += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = window()
    mi_app.show()
    sys.exit(app.exec_())
