from django import forms
from django.contrib.auth.models import User
from mainapp.models import Complaint,DuesItem,MessBill
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

class DuesForm(ModelForm):
	class Meta:
		model = DuesItem
		fields=('duesitem_type','duesdetails','set_dues','pay_dues','paymentInfo')
		widgets={'duesitem_type':TextInput(attrs={'readonly':'readonly'}) ,'duesdetails':Textarea(attrs={'readonly':'readonly'}),'set_dues':TextInput(attrs={'readonly':'readonly'}),}
	
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		self.fields['duesdetails'].required = False       
		
class MessBillForm(ModelForm):
	class Meta:
		model = MessBill
		fields=('month','details','total_bill','pay_messbill','paymentInfo')
		widgets={'month':TextInput(attrs={'readonly':'readonly'}) ,'details':Textarea(attrs={'readonly':'readonly'}),'total_bill':TextInput(attrs={'readonly':'readonly'}),}
	
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		self.fields['details'].required = False      
		
