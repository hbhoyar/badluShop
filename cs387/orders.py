from django.http import HttpResponse

def orders(req):
    # items = ['samosas', 'chai', 'idli vada']
    html = "Your order:<br>"
    itemplate = "{0} = {1}<br>"
    for item, quantity in req.GET.items():
        html += itemplate.format(item, quantity)
    
    return HttpResponse(html)