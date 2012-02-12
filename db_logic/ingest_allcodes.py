import sys
import sqlite3
import os
try:
    import json
except:
    import simplejson as json

cb_home = '/var/www/cuibono_webservice/'

sys.path.insert(0, "./echoprint_server_api")
import fp

def find_ad_id(filename):
    media_home = cb_home+'media/'
    filename = filename.replace(media_home,'')
    print media_home
    print filename
    con = sqlite3.connect(cb_home+'cuibono.db')
    cur = con.cursor()
    cur.execute("select id from cuibono_ad where file = '%s'" % filename)
    r = cur.fetchall()
    return r[0][0]

def parse_json_dump(jfile):
    codes = json.load(open(jfile))
    fullcodes = []
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
        
    return fullcodes

if __name__ == "__main__":
    jfile = sys.argv[1]
    fullcodes = parse_json_dump(jfile)
    fp.ingest(fullcodes, do_commit=False)
    fp.commit()

