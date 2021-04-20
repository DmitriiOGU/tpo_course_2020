import pandas as pd
import os
import sqlalchemy
import psycopg2
from psycopg2 import sql
import time

time.sleep(2)
connection = psycopg2.connect(dbname='postgres', user='postgres',\
                 password='postgres', host='localhost', port=5432)
cursor = connection.cursor()
cursor.execute("CREATE TABLE if not exists test (id serial PRIMARY KEY, value_1 varchar, value_2 integer);")

df = pd.read_csv('/manage_db/my.csv', header=None)
for i in range(df.shape[0]):
        insert = "INSERT INTO test (value_1,value_2) VALUES ('{}',{})".format(df.loc[i][0],df.loc[i][1])
        cursor.execute(insert)
connection.commit()
cursor.execute('SELECT value_1,value_2 FROM test')
records = cursor.fetchall()
flag = True
for i in range(df.shape[0]):
        if not tuple(df.loc[i]) in records:
                flag = False
                break
if flag:
        print('\n THE DATA IS CORRECTLY ADDED TO TABLE!!! \n')
else:
        print('\n THE DATA WAS NOT APPEND TO DATABASE\n')
try:
        cursor.close()
        connection.close()
except:
        connection.close()