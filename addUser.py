#!/usr/bin/env python3.8

from utils.dbexec import connect, exec_query1

loginName = input('loginName: ')
password = input('password: ')

sql = f"""insert into addaUsers values('{loginName}','{password}')"""

try:
    exec_query1(sql)
except Exception as e:
    print(e)