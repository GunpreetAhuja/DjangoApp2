from django.shortcuts import render
from django import forms
# Create your views here.
from shop.models import Entry
from shop.forms import AddItem

def input(request):
    if request.method=='POST':
        form = AddItem(request.POST)
        if form.is_valid():
            no_of_items = form.cleaned_data['no_of_items']
            item = form.cleaned_data['item']
            obj = Entry(item='{{item}}', no_of_items='{{no_of_items}}')
            obj.save()
    else:
        form = AddItem()
    return render(request, 'input.html', {'form': form,
        })

def display(request):
    obj = Entry.objects.get()
    item = obj.item
    no_of_items = obj.no_of_items
    total = no_of_items * item
    return render(request, 'display.html', {'item':item, 'no_of_items': no_of_items, 'total': total})
