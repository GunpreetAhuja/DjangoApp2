from django.shortcuts import render
from shop.models import *

def display(request):
    error = False
    form = EntryForm()
    if 'item' in request.GET:
       item = request.GET['item']
       no_of_items = request.GET['no_of_items']
       if not (item or no_of_items):
            error = True
       else:
            val = Entry.objects.filter(item=item)
            total = val.no_of_items * val.cost
            return render(request, 'display.html', {'item': val.item, 'cost': val.cost, 'total': total})
    
    
    return render(request, 'input.html',{'error':error,'form':form})   


