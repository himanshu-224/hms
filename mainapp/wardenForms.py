from django import forms
from django.contrib.auth.models import User
from mainapp.models import Complaint
from django.forms import ModelForm
from django.forms import Textarea
from mainapp.models import Election

class ComplaintForm(ModelForm):
	class Meta:
		model = Complaint
		widgets = {'details': Textarea(attrs={'readonly':'readonly'}),'forwardto_id': forms.TextInput(attrs={'readonly':'readonly'}), 'status': Textarea, 'reason': Textarea, 'complainee_id' : forms.TextInput(attrs={'readonly':'readonly'}),  'addressedto_id' : forms.TextInput(attrs={'readonly':'readonly'}),'complaint_timestamp' : forms.DateInput(attrs={'readonly':'readonly'}),'complaint_type' : forms.TextInput(attrs={'readonly':'readonly'}), 
        }
        
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		self.fields['forwardto_id'].required = False        
		self.fields['reason'].required = False 
		self.fields['status'].required = False 
		
class StartElectionForm(forms.Form) :
	election_type = forms.CharField(max_length = 20,widget=forms.TextInput)
	description = forms.CharField(max_length=500,widget=forms.Textarea()) 
	start_dateTime = forms.CharField(max_length = 20,widget=forms.TextInput) 
	end_dateTime = forms.CharField(max_length = 20,widget=forms.TextInput)
	election_officer = forms.CharField(max_length = 30,widget=forms.TextInput)
	num_candidates = forms.CharField(max_length = 20, widget=forms.TextInput)

class CandidateNominationForm(forms.Form) :
	candidate_username = forms.CharField(max_length = 20,widget=forms.TextInput)
	candidate_post = forms.CharField(max_length = 20,widget=forms.TextInput)