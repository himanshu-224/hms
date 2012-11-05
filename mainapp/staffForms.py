from django import forms
from django.contrib.auth.models import User
from mainapp.models import Complaint
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput


class StaffComplaintViewForm(forms.Form):
	id=0
	Choices=(
            ("Pending", "Pending"),
            ("Accepted", "Accepted"),
			("Rejected", "Rejected")
			)
	Choices1=(
        ("Warden", "Warden"),
        ("Staff", "Hall Staff"),
		("Dosa", "DOSA"),
		("Hec", "HEC"),
         )			

	complainee_id = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'readonly':'readonly'}))
	addressed_to = forms.ChoiceField(choices=Choices1,widget=forms.Select(attrs={'readonly':'readonly'}))
   	forwarded_to = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'readonly':'readonly'}))
   	complaint_timestamp = forms.DateField(widget=forms.DateInput(attrs={'readonly':'readonly'}))
	complaint_type = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'readonly':'readonly'}))
	details = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'readonly':'readonly'}))
	status = forms.CharField(max_length=200,widget=forms.Textarea(attrs={'readonly':'readonly'}))
	reason = forms.CharField(max_length=200,widget=forms.Textarea(attrs={'readonly':'readonly'}))
	is_Accepted = forms.ChoiceField(choices=Choices,widget=forms.Select(attrs={'readonly':'readonly'}))

class StaffComplaintForm(forms.Form):
	Choices=(
            ("Pending", "Pending"),
            ("Accepted", "Accepted"),
			("Rejected", "Rejected")
			)	
	Choices1=(
        ("Warden", "Warden"),
        ("Staff", "Hall Staff"),
		("Dosa", "DOSA"),
		("Hec", "HEC"),
         )
	complainee_id = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'readonly':'readonly'}))
   	addressed_to = forms.ChoiceField(choices=Choices1,widget=forms.Select(attrs={'readonly':'readonly'}))
   	forwarded_to = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'readonly':'readonly'}))
   	complaint_timestamp = forms.DateField(widget=forms.DateInput(attrs={'readonly':'readonly'}))
	complaint_type = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'readonly':'readonly'}))
	details = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'readonly':'readonly'}))
	status = forms.CharField(max_length=200,widget=forms.Textarea)
	reason = forms.CharField(max_length=200,widget=forms.Textarea)
	is_Accepted = forms.ChoiceField(choices=Choices,widget=forms.Select(attrs={'readonly':'readonly'}))
