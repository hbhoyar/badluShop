#!/usr/bin/env python3.8

from utils.dbexec import connect, exec_query1

loginName = input('loginName: ')
password = input('password: ')

sql = f"""insert into addaUsers values('{loginName}','{password}')"""

try:
    conn = connect()
    exec_query1(conn, sql)
    conn.commit()
except Exception as e:
    print(e)