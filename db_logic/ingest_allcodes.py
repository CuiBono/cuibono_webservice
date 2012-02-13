import sys
import sqlite3
import os
try:
    import json
except:
    import simplejson as json
import datetime

cb_home = '/var/www/cuibono_webservice/'

sys.path.insert(0, "./echoprint_server_api")
import fp
import pytyrant


def find_ad_id(filename):
    media_home = cb_home+'media/'
    filename = filename.replace(media_home,'')
    print media_home
    print filename
    con = sqlite3.connect(cb_home+'cuibono.db')
    cur = con.cursor()
    cur.execute("select id from cuibono_ad where file = '%s'" % filename)
    r = cur.fetchall()
    con.close()
    return r[0][0]
    

def parse_json_dump(jfile):
    codes = json.load(open(jfile))
    fullcodes = []
    trids = []
    for c in codes:
        if "code" not in c:
            continue
        code = c["code"]
        m = c["metadata"]
        trid = find_ad_id(m["filename"])
        length = m["duration"]
        version = m["version"]
        artist = m.get("artist",None)
        title = m.get("title",None)
        release = m.get("release",None)
        decoded = fp.decode_code_string(code)

        data = {"track_id": trid,
                "fp": decoded,
                "length": length,
                "codever": "%.2f" % version
               }
        fullcodes.append(data)
        trids.append(trid)
        
    return fullcodes,trids

def check_ingests(trids):
    dt = datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d_%H%M%S')
    log = open('logs/'+dt+'.log','w')
    con = sqlite3.connect(cb_home+'cuibono.db')
    cur = con.cursor()
    t = pytyrant.PyTyrant.open('127.0.0.1',1978)
    ty_keys = t.keys()
    for trid in trids:
        if str(trid)+'-1' in ty_keys:
            cur.execute('UPDATE cuibono_ad SET ingested = 1 WHERE id = %d' % trid)
        elif str(trid)+'-0' in ty_keys:
            cur.execute('UPDATE cuibono_ad SET ingested = 1 WHERE id = %d' % trid)
        else:
            log.write('ad id '+trid+' not ingested correctly.')
    con.commit()


if __name__ == "__main__":
    jfile = sys.argv[1]
    fullcodes,trids = parse_json_dump(jfile)
    fp.ingest(fullcodes, do_commit=False)
    fp.commit()
    check_ingests(trids)        
    os.remove(jfile)
    os.remove('fingerprint_queue.txt')
