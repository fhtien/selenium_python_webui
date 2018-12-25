#!/usr/bin/python
import pytest
import psycopg2
import json

conn = psycopg2.connect(database="hlxj", user="hlxj_read_only", password="gzshili@2018", host="rm-wz9823mjt2rv76g4kwo.pg.rds.aliyuncs.com", port="3432")

print("Opened database successfully")

cur = conn.cursor()

# cur.execute("SELECT id, name, address, salary  from COMPANY")
# sql = 'select name, configother FROM tb_unit WHERE configother != \'\''
sql = "SELECT r.name, l.name, l.patrolranglayer  FROM tb_unit AS l RIGHT JOIN tb_unit AS r ON l.pid = r.id WHERE l.unittype IN ('SYSTEM') AND l.patrolranglayer !=''"

cur.execute(sql)

rows = cur.fetchall()
for row in rows:
   print( row[0], '-', row[1], end=' - ')
   j = json.loads(row[2])
   try:
      assert "layers" in j.keys()
      print('有配layers数据')
   except AssertionError as e:
      print('图层配置：',row[2] )

print("Operation done successfully")
conn.close()