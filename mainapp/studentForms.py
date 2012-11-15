from django import forms
from django.contrib.auth.models import User
from mainapp.models import Complaint,DuesItem
from django.forms import ModelForm, Textarea, TextInput


class ComplaintForm1(ModelForm):
	class Meta:
		model = Complaint
		widgets = {'details': Textarea,  'addressedto_id' : TextInput,'complaint_type' : TextInput}
        fields =('addressedto_id','complaint_type','details',)
        
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

class DuesForm(forms.Form):
	duesitem_type = forms.ChoiceField(
		choices=(
			("mess bill","Mess Bill"),
			("fine","Fine"),
			),widget=forms.Select
		)
	duesdetails = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'readonly':'readonly'}))
	pay_dues = forms.IntegerField()
	paymentInfo = forms.CharField(max_length=100,widget=forms.TextInput)
	
	def __init__(self, *args, **kwargs):
		super(forms.Form, self).__init__(*args, **kwargs)
		self.fields['duesdetails'].required = False       
