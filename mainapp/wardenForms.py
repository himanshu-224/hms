from django import forms
from django.contrib.auth.models import User
from mainapp.models import Complaint,DuesItem
from django.forms import ModelForm
from django.forms import Textarea


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
		
class DuesForm(forms.Form):
	duesitem_type = forms.ChoiceField(
		choices=(
			("mess bill","Mess Bill"),
			("fine","Fine"),
			),widget=forms.Select
		)
	duesdetails = forms.CharField(max_length=500,widget=forms.Textarea)
	set_dues = forms.IntegerField()
	payee_id = forms.CharField(max_length=10,widget=forms.TextInput)
		
class DuesForm1(ModelForm):
	Choices1=(
			("Accepted","Accepted"),
			("Rejected","Rejected"),
			("Pending","Pending"),
			)
	isApproved_warden = forms.ChoiceField(choices=Choices1)	
	class Meta:
		model = DuesItem
		widgets = {'duesitem_type':forms.TextInput(attrs={'readonly':'readonly'}),'isApproved_staff':forms.TextInput(attrs={'readonly':'readonly'}),'duesdetails': Textarea(attrs={'readonly':'readonly'}),'submitted':forms.TextInput(attrs={'readonly':'readonly'}),'paymentInfo':forms.TextInput(attrs={'readonly':'readonly'}),'set_dues':forms.TextInput(attrs={'readonly':'readonly'}),'pay_dues':forms.TextInput(attrs={'readonly':'readonly'}), 'status': Textarea,'payee_id' : forms.TextInput(attrs={'readonly':'readonly'}),'submission_timestamp' : forms.DateInput(attrs={'readonly':'readonly'}), 
        }
        
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		self.fields['status'].required = False 
		self.fields['paymentInfo'].required = False	
		self.fields['isApproved_staff'].required = False
		
