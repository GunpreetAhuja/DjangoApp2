from django.db import models
from django.forms import ModelForm

# Create your models here.
class Entry(models.Model):
    item = models.CharField(max_length=200)
    no_of_items = models.IntegerField()
    cost = models.IntegerField()
    total = models.IntegerField(default=0)   
    def __unicode__(self):
        return self.item


class EntryForm(ModelForm):
   class Meta:
	model = Entry
	exclude = ['total', 'cost']
    


