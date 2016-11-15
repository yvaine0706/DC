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
    with open('E:/DC/train/borrow_train.txt') as file:
        lines = file.readlines()
        for line in lines:
            items = line.split(',')
            
            if items[-1][1]>'A' and items[-1][1]<'Z' and items[-1][0]=='"':
                #print items[0],items[1],items[-1]  
                print items[-1]
                sql = 'insert into borrow_train(id ,date,bianhao) values ( %d, %s, %s)' % (int(items[0]), items[1],items[-1])
                cur.execute(sql)
            else:
                print items[-1]
                sql = 'insert into borrow_train(id ,date,bianhao) values ( %d, %s, %s)' % (int(items[0]), items[1],"-1")
                cur.execute(sql)
                
                
    conn.commit()
    conn.close()

except Exception as e:
    pdb.set_trace()
    conn.close()
    print e