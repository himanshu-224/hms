from django import forms
from mainapp.models import *
from django.forms import ModelForm
from django.forms import Textarea,TextInput


class AddItemForm(ModelForm):
    class Meta:
        model = InventoryItem
        exclude=('date_added','no_issued','Issue','Delete')

class IssueItemForm(ModelForm):
    class Meta:
        model = InventoryIssue
        exclude=('issue_timestamp','issued_duration','Return','item_id')
       
        
   