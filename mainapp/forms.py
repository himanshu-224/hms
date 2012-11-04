from django import forms
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput


class ComplaintForm(forms.Form):

   	addressed_to = forms.ChoiceField(
        choices=(
            ("warden", "Warden"),
            ("staff", "Hall Staff"),
			("dosa", "DOSA"),
			("hec", "HEC"),
            ),
        )
	complaint_type = forms.CharField(max_length=20)
	details = forms.CharField(max_length=500,widget=forms.Textarea)

