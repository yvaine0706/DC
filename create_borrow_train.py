import os
import pdb
import utils

import MySQLdb
try:
    conn = utils.persist.connection()
    cur = conn.cursor()
    #companysql ='DROP TABLE IF EXISTS borrow_train'
    companysql = 'create table borrow_train(id int,date varchar(10),bianhao varchar(50))'

    scoretol = cur.execute(companysql)
    conn.commit()
    conn.close()

except Exception as e:

    conn.close()
    print e
