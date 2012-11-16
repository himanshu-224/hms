from django import forms
from django.contrib.auth.models import User
from mainapp.models import Complaint,DuesItem,MessBill
from django.forms import ModelForm
from django.forms import Textarea,TextInput


class ComplaintForm(ModelForm):

	Choices1=(
        ("Warden", "Warden"),
        ("", "Don't Forward"),
	)
	forwardto_id = forms.ChoiceField(choices=Choices1)
	class Meta:
		model = Complaint
		widgets = {'details': Textarea(attrs={'readonly':'readonly'}), 'status': Textarea, 'reason': Textarea, 'complainee_id' : forms.TextInput(attrs={'readonly':'readonly'}),  'addressedto_id' : forms.TextInput(attrs={'readonly':'readonly'}),'complaint_timestamp' : forms.DateInput(attrs={'readonly':'readonly'}),'complaint_type' : forms.TextInput(attrs={'readonly':'readonly'}), 
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
	isApproved_staff = forms.ChoiceField(choices=Choices1)	
	class Meta:
		model = DuesItem
		exclude={'isApproved_warden'}
		widgets = {'duesitem_type':forms.TextInput(attrs={'readonly':'readonly'}),'duesdetails': Textarea(attrs={'readonly':'readonly'}),'submitted':forms.TextInput(attrs={'readonly':'readonly'}),'paymentInfo':forms.TextInput(attrs={'readonly':'readonly'}),'set_dues':forms.TextInput(attrs={'readonly':'readonly'}),'pay_dues':forms.TextInput(attrs={'readonly':'readonly'}), 'status': Textarea,'payee_id' : forms.TextInput(attrs={'readonly':'readonly'}),'submission_timestamp' : forms.DateInput(attrs={'readonly':'readonly'}), 
        }
        
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		self.fields['status'].required = False 
		self.fields['paymentInfo'].required = False	
		
class MessBillForm(forms.Form):
	payee_id = forms.CharField(max_length=10,widget=forms.TextInput)
	month = forms.ChoiceField(
		choices=(
			("january","january "),
			("february","February"),
			("march","March"),
			("april","April"),
			("may","May"),
			("june","June"),
			("july","July"),
			("august","August"),
			("september","September"),
			("october","October"),
			("october","November"),
			("december","December"),
			),widget=forms.Select
		)
	no_of_days= forms.IntegerField()
	rebate_days =forms.IntegerField()
	basic_amount=forms.FloatField() 
	extra = forms.FloatField()
	details = forms.CharField(max_length=500,widget=forms.Textarea)
	
class MessBillForm1(ModelForm):
	month = forms.ChoiceField(
		choices=(
			("january","january "),
			("february","February"),
			("march","March"),
			("april","April"),
			("may","May"),
			("june","June"),
			("july","July"),
			("august","August"),
			("september","September"),
			("october","October"),
			("october","November"),
			("december","December"),
			),widget=forms.Select
		)	
	class Meta:
		model = MessBill
		exclude={'submission_timestamp','submitted','paymentInfo','isVerified_staff','total_bill','pay_messbill','status'}
		widgets = {'payee_id':forms.TextInput(attrs={'readonly':'readonly'}),'no_of_days':forms.TextInput,'rebate_days':forms.TextInput,'basic_amount':forms.TextInput,'extra':forms.TextInput 
        }
        
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		#self.fields['status'].required = False 
		#self.fields['paymentInfo'].required = False
		self.fields['details'].required = False
			
		
class MessBillForm2(ModelForm):
	Choices1=(
			("Accepted","Accepted"),
			("Rejected","Rejected"),
			("Pending","Pending"),
			)
	isVerified_staff = forms.ChoiceField(choices=Choices1)	
	class Meta:
		model = MessBill
		exclude=('no_of_days','rebate_days','basic_amount','extra')
		widgets = {'payee_id' : forms.TextInput(attrs={'readonly':'readonly'}),'month':forms.TextInput(attrs={'readonly':'readonly'}),'details':forms.TextInput(attrs={'readonly':'readonly'}),'total_bill': TextInput(attrs={'readonly':'readonly'}),'pay_messbill':forms.TextInput(attrs={'readonly':'readonly'}),'submitted':forms.TextInput(attrs={'readonly':'readonly'}),'paymentInfo':forms.TextInput(attrs={'readonly':'readonly'}), 'status': Textarea,'submission_timestamp' : forms.DateInput(attrs={'readonly':'readonly'}), 
        }
        
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		self.fields['status'].required = False 
		self.fields['paymentInfo'].required = False	
		
