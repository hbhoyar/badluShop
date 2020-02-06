from django.shortcuts import render, redirect
from django.http import HttpResponse
from utils.dbexec import connect, exec_query
from datetime import datetime


def orders(req):
    items = ['samosa', 'chai', 'idli']
    loginName = req.session.get('loginName')

    if not loginName:
        return redirect('login')

    conn = connect()

    sql = f"""select loginName from addaUsers where loginName='{loginName}'"""
    _, rows = exec_query(conn, sql)

    if not len(rows):
        return redirect('login')

    historySql = f"""select orderId, item, itemQuantity, dateTime from orderHistory 
            where loginName='{loginName}' order by orderId desc limit 5 """

    _, orderHistory = exec_query(conn, historySql)

    # print(orderHistory)

    if req.method == "GET":
        return render(req, 'orders.html', {
            'items': items,
            'orderHistory': orderHistory
        })

    if req.method == "POST":
        orders = {}
        
        for item in items:
            try:
                x = int(req.POST[item])
                if x < 0:
                    orders = {}
                    break
                elif x > 0:
                    orders[item] = x
            except:
                pass

        if not len(orders):
            return render(req, 'orders.html', {
                'items': items,
                'orderHistory': orderHistory,
                'status': 'error',
                'message': 'Invalid order'
            })

        orderIds = []

        for item, val in orders.items():
            sql = f"""insert into orderHistory(loginName, dateTime, item, itemQuantity) values
                ('{loginName}','{str(datetime.now())}','{item}','{val}')
                returning orderId"""
            _, rows = exec_query(conn, sql)

            orderIds.append([item, val, rows[0][0]])

        conn.commit()
        # print(orderIds)

        _, orderHistory = exec_query(conn, historySql)
        
        return render(req, 'orders.html', {
            'items': items,
            'orderHistory': orderHistory,
            'status': 'success',
            'orders': orderIds
        })
