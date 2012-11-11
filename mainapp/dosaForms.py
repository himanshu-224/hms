from django import forms
from django.contrib.auth.models import User
from mainapp.models import Complaint
from django.forms import ModelForm
from django.forms import Textarea

class ComplaintForm(ModelForm):
	class Meta:
		model = Complaint
		exclude=("forwardto_id",)
		widgets = {'details': Textarea(attrs={'readonly':'readonly'}), 'status': Textarea, 'reason': Textarea, 'complainee_id' : forms.TextInput(attrs={'readonly':'readonly'}),  'addressedto_id' : forms.TextInput(attrs={'readonly':'readonly'}),'complaint_timestamp' : forms.DateInput(attrs={'readonly':'readonly'}),'complaint_type' : forms.TextInput(attrs={'readonly':'readonly'}), 
        }
        
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)       
		self.fields['reason'].required = False 
		self.fields['status'].required = False 
		
