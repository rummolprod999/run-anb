import subprocess
import time

import pymysql as pymysql

USERDB = 'root'
PASSDB = '1234'
DB = 'anb'


def main():
    con = pymysql.connect(host="localhost", user=USERDB, passwd=PASSDB, db=DB, charset='utf8',
                          init_command='SET NAMES UTF8', cursorclass=pymysql.cursors.DictCursor, autocommit=True)
    cur = con.cursor()
    cur.execute(
            """SELECT id FROM users WHERE is_admin = 0""")
    res = cur.fetchall()
    cur.close()
    con.close()
    for r in res:
        try:
            subprocess.Popen(['java', '-jar', './parser/anb-1.0-jar-with-dependencies.jar', 'anb', str(r['id'])])
            time.sleep(15 * 60)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
