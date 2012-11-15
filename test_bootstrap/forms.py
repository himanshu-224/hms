from django import forms
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput

#created for the profile link in dashboard 
class ProfileForm(forms.Form):
    #initially filling the values

#    def __init__(self, subdomain, *args, **kwargs):
#        self.default_username = default_username
#        super(UserForm, self).__init__(*args, **kwargs)
    
    name= forms.CharField(
        max_length=40,
        help_text=u'eg Archit',
    )
    
    roll_number=forms.CharField(
        max_length=10,
        help_text=u'eg Y9000',
    )
    
    email = forms.EmailField(
        help_text=u'eg architb@iitk.ac.in'
    )
 
    contact_number=forms.CharField(
        max_length=10,
        help_text=u'eg 9000090000',
    )
    
    username=forms.CharField(
        min_length=5,
        max_length=14,
    )     
    def clean(self):
        cleaned_data = super(TestForm, self).clean()
        raise forms.ValidationError("This error was added to show the non field errors styling.")
        return cleaned_data

class ComplainForm(forms.Form):
    #initially filling the values

#    def __init__(self, subdomain, *args, **kwargs):
#        self.default_username = default_username
#        super(UserForm, self).__init__(*args, **kwargs)

    # the person should be tagged from db
    to= forms.CharField(
        max_length=40,
        help_text=u'eg Waden/Hall Office/HEC',
    )
   
   
    type_of_complaint = forms.ChoiceField(
        choices=(
            ("Elec", "Plain text"),
            ("Water", "HTML"),
        ),
        help_text=u'Pick your choice',
    )

    def clean(self):
        cleaned_data = super(TestForm, self).clean()
        raise forms.ValidationError("This error was added to show the non field errors styling.")
        return cleaned_data




class TestForm(forms.Form):
    date = forms.DateField(
        widget=BootstrapDateInput(),
    )
    title = forms.CharField(
        max_length=100,
        help_text=u'This is the standard text input',
    )
    disabled = forms.CharField(
        max_length=100,
        help_text=u'I am read only',
        widget=forms.TextInput(attrs={
            'disabled': 'disabled',
            'placeholder': 'I am disabled',
        })
    )
    content = forms.ChoiceField(
        choices=(
            ("text", "Plain text"),
            ("html", "HTML"),
        ),
        help_text=u'Pick your choice',
    )
    email = forms.EmailField()
    like = forms.BooleanField(required=False)
    fruits = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=(
            ("apple", "Apple"),
            ("pear", "Pear"),
        ),
        help_text=u'As you can see, multiple checkboxes work too',
    )
    veggies = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={
            'inline': True,
        }),
        choices=(
            ("broccoli", "Broccoli"),
            ("carrots", "Carrots"),
            ("turnips", "Turnips"),
        ),
        help_text=u'And can be inline',
    )
    color = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=(
            ("#f00", "red"),
            ("#0f0", "green"),
            ("#00f", "blue"),
        ),
        help_text=u'And we have <i>radiosets</i>',
    )
    prepended = forms.CharField(
        max_length=100,
        help_text=u'I am prepended by a P',
        widget=BootstrapTextInput(prepend='P'),
    )

    def clean(self):
        cleaned_data = super(TestForm, self).clean()
        raise forms.ValidationError("This error was added to show the non field errors styling.")
        return cleaned_data

class TestModelForm(forms.ModelForm):
    class Meta:
        model = User

class TestInlineForm(forms.Form):
    query = forms.CharField(required=False, label="")
    vegetable = forms.ChoiceField(
        choices=(
            ("broccoli", "Broccoli"),
            ("carrots", "Carrots"),
            ("turnips", "Turnips"),
        ),
    )
    active = forms.ChoiceField(widget=forms.RadioSelect, label="", choices=(
        ('all', 'all'),
        ('active', 'active'),
        ('inactive', 'inactive')
        ), initial='all')
    mine = forms.BooleanField(required=False, label='Mine only', initial=False)

class WidgetsForm(forms.Form):
    date = forms.DateField(widget=BootstrapDateInput)
