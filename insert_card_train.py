#coding:utf8

import os
import json
import sys
import re
reload(sys)
sys.setdefaultencoding('utf8')
import utils
import traceback
import pdb


try:

    conn = utils.persist.connection()
    cur = conn.cursor()
    cur.execute('set character_set_client=utf8')
    cur.execute('set character_set_connection=utf8')
    cur.execute('set character_set_database=utf8')
    cur.execute('set character_set_results=utf8')
    cur.execute('set character_set_server=utf8')
    conn.commit()
    mode = re.compile(r'\d+')
    with open('E:/DC/train/card_train.txt') as file:
        lines = file.readlines()
        for line in lines:
            items = line.split(',')
#             if items[3] == '':
#                 items[3]='null'
            print int(items[0]), items[1], items[2], items[3]
            
            
                
            sql = 'insert into card_train(id,leibie,didian,fangshi,shijian,jine,sy_jine) values ( %d, %s, %s, %s, %s, %s, %s)' % (int(items[0]), items[1], items[2], items[3], items[4], items[5], items[6])
            cur.execute(sql)
                
    conn.commit()
    conn.close()

except Exception as e:
    pdb.set_trace()
    conn.close()
    print e