import os
import pdb
import utils

import MySQLdb
try:
    conn = utils.persist.connection()
    cur = conn.cursor()

    companysql = 'create table card_train(id int,leibie varchar(10),didian varchar(10),fangshi varchar(6),shijian varchar(20),jine varchar(12),sy_jine varchar(10))'

    scoretol = cur.execute(companysql)
    conn.commit()
    conn.close()

except Exception as e:

    conn.close()
    print e
