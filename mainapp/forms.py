from django import forms
from django.contrib.auth.models import User


class ComplaintForm(forms.Form):
   	addressedto_id = forms.ChoiceField(
        choices=(
            ("Warden", "Warden"),
            ("Staff", "Hall Staff"),
			("Dosa", "DOSA"),
			("Hec", "HEC"),
            ),widget=forms.Select
        )
	complaint_type = forms.CharField(max_length=100,widget=forms.TextInput)
	details = forms.CharField(max_length=500,widget=forms.Textarea())  

