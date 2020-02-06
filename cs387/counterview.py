from django.http import HttpResponse

count = 0

def counter(req):
    global count
    count += 1
    html = str(count)
    return HttpResponse(html)