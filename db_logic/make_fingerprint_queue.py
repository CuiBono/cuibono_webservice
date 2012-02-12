import sqlite3
import sys

cb_home = '/var/www/cuibono_webservice/'

out = open('fingerprint_queue.txt','a')

con = sqlite3.connect(cb_home+'cuibono.db')
cur = con.cursor()
cur.execute('select file from cuibono_ad where ingested = 0')
results = cur.fetchall()
for result in results:
    out.write(cb_home+'media/'+result[0])
    out.write('\n')

out.close()
