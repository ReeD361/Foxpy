import sqlite3
import os
import sys

#status = 'Pass'
#serial = '1231'
#fix = 'fixture2'
status = 'Pass'
serial = sys.argv[1]
fix = sys.argv[2]
date = os.popen('date +%d%m%Y').read().rstrip()
dias = os.popen('date +%d').read().rstrip()
mees = os.popen('date +%m').read().rstrip()
year = os.popen('date +%Y').read().rstrip()
hour = os.popen('date +%H%M%S').read().rstrip()
ruta = "/home/red361/Roms/testgui/Fix/%s" % fix
sql = sqlite3.connect('%s/yield.db' % ruta)
fecha = os.popen('date +%Y%m%d_%H%M%S').read().rstrip()

def unblock():
    cur = sql.cursor()
    cur.execute('SELECT * FROM (SELECT status FROM history ORDER BY hour DESC LIMIT 3)')
    aa = str(cur.fetchall())
    sql.commit()
    cur.close()
    if aa != "[('Fail',), ('Fail',), ('Fail',)]":
        print("yeah")
        status_txt = open('%s/status_fix.txt' % ruta, "w")
        status_txt.write('')
        status_txt.close()

def global_story():
    cur = sql.cursor()
    cur.execute('SELECT pass FROM yield_global WHERE id = 1')
    txt_pass = int(cur.fetchone()[0])
    qty = txt_pass + 1
    qty_tex = str(qty)
    cur.execute('Update yield_global set pass = ? WHERE id = 1', (qty_tex,))
    sql.commit()
    cur.close()
    os.system('touch %s/green.log' % ruta)


def sn_history():
    cur = sql.cursor()
    cur.execute("INSERT INTO history VALUES (?,?,?,?,?,?)", (dias, mees, year, serial, status, fecha))
    sql.commit()
    cur.close()


def regeddit():
    cur = sql.cursor()
    if cur.execute("SELECT * FROM yielddxd WHERE date = ?", (date,)).fetchone():
        cur.execute('SELECT pass_qty FROM yielddxd WHERE date = ?', (date,))
        txt_pass = int(cur.fetchone()[0])
        qty = txt_pass + 1
        qty_tex = str(qty)
        cur.execute('Update yielddxd set pass_qty = ? WHERE date = ?', (qty_tex, date,))
        cur.execute('SELECT fail_qty FROM yielddxd WHERE date = ?', (date,))
        t_fail = int(cur.fetchone()[0])
        try:
            yie = qty / (qty + t_fail) * 100
            yie = str(yie)
        except ZeroDivisionError:
            yie = '100'
        cur.execute('Update yielddxd set yield = ? WHERE date = ?', (yie, date,))
        yield_txt = open('%s/yield_per.txt' % ruta, "w")
        yield_txt.write(yie)
        yield_txt.close()
        sql.commit()
        cur.close()
        sn_history()
        global_story()
        unblock()
    else:
        cur.execute("INSERT INTO yielddxd VALUES (?,?,?,?)", (date, '0', '0', '0'))
        sql.commit()
        regeddit()


regeddit()
