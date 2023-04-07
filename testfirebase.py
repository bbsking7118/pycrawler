import os,sys,json
sys.path.append(("D:\work1\study\firebase\backend"))
# os.chdir('d:\data')
from dbHandler.firebase import *

auth = FireAuth()
fdb = FireStore()
fsdb = FireStorage()

with open('file/csv_to_json.json', 'r', encoding='utf-8') as f:
    js = json.loads(f.read())

for key in js :
    fdb.write('hanbang',js[key])

