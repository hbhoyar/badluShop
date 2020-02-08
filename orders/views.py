from django.shortcuts import render, redirect
from django.http import HttpResponse
from utils.dbexec import connect, exec_query, exec_query1
from datetime import datetime

items = ['samosa', 'chai', 'idli']

def getHistoryOrders(conn, loginName):
    orders = []
    sql = f"""select orderId, dateTime from public.order 
            where loginName='{loginName}' order by orderId desc limit 5 """
    _, orderHistory = exec_query(conn, sql)

    for order in orderHistory:
        sql = f"""select item, itemQuantity from orderItem 
            where orderId='{order[0]}' """
        _, orderItems = exec_query(conn, sql)
        order1 = [order[0], 0, 0, 0, order[1]]
        for orderItem in orderItems:
            order1[items.index(orderItem[0])+1] = orderItem[1]

        orders.append(order1)

    return orders

def orders(req):
    loginName = req.session.get('loginName')

    if not loginName:
        return redirect('login')

    conn = connect()

    sql = f"""select loginName from addaUsers where loginName='{loginName}'"""
    _, rows = exec_query(conn, sql)

    if not len(rows):
        return redirect('login')

    if req.method == "GET":
        return render(req, 'orders.html', {
            'items': items,
            'orderHistory': getHistoryOrders(conn, loginName)
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
                'orderHistory': getHistoryOrders(conn, loginName),
                'status': 'error',
                'message': 'Invalid order'
            })
        
        sql = f"""insert into public.order(loginName, dateTime) values
                ('{loginName}','{str(datetime.now())}')
                returning orderId"""

        _, rows = exec_query(conn, sql)
        orderId = rows[0][0]

        for item, val in orders.items():
            sql = f"""insert into orderItem(orderId, item, itemQuantity) values
                ('{orderId}','{item}','{val}')"""
            exec_query1(conn, sql)

        conn.commit()
        # print(orderIds)
        
        return render(req, 'orders.html', {
            'items': items,
            'orderHistory': getHistoryOrders(conn, loginName),
            'status': 'success',
            'orderId': orderId
        })
