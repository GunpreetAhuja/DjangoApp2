from django.shortcuts import render
from django import forms
# Create your views here.
from shop.models import *
#from shop.forms import AddItem
from django.http import HttpResponseRedirect

def input(request):
    if request.method=='POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            #no_of_items = form.cleaned_data['no_of_items']
            #item = form.cleaned_data['item']
            cd=form.cleaned_data
            item=cd['item']
            no_of_items=cd['no_of_items']
            obj = Entry(item=item, no_of_items=no_of_items)
            obj.save()
            return HttpResponseRedirect('/shop/display/')
          
    else:
        form = EntryForm()
    return render(request, 'input.html', {'form': form
     })

def display(request):
    obj = Entry.objects.get(id=9)
    item = obj.item
    cost = obj.cost
    no_of_items = obj.no_of_items
    total = no_of_items * cost
    return render(request, 'display.html', {'item':item, 'cost':cost, 'total': total})
