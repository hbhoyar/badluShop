from django.http import HttpResponse
from django.shortcuts import render, redirect
from utils.dbexec import connect, exec_query

def login(req):
    error = ''
    conn = connect()

    if req.method == "GET":
        return render(req, "login.html")

    if req.method == "POST":
        loginName = req.POST.get('loginName')
        password = req.POST.get('password')
        
        if not loginName or not password:
            return render(req, 'login.html')

        sql = f"""select password from addaUsers where loginName='{loginName}'"""
        headers, data = exec_query(conn, sql)
        print(data)

        if not len(data):
            error = "User does not exists"
            print(error)
            return render(req, "login.html")

        if data[0][0] != password:
            error = "Wrong password"
            print(error)
            return render(req, "login.html")

        req.session.cycle_key()
        req.session['loginName'] = loginName
        return redirect('orders')

