#!/bin/bash

LOGIC_DIR=/home/blannon/db_logic/
CB_DIR=/var/www/cuibono_webservice/

python make_fingerprint_queue.py
./echoprint-codegen -s < fingerprint_queue.txt > allcodes.json
python ingest_allcodes.py allcodes.json
