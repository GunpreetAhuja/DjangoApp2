from django import forms
from shop.models import Entry


class AddItem(forms.Form):
    item = forms.CharField(max_length=220)
    no_of_items = forms.IntegerField()
