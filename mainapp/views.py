from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
#from django import oldforms as forms
from mainapp.forms import ComplaintForm
from django.template.context import RequestContext
from django.contrib.auth.forms import UserCreationForm
from mainapp.models import Complaint
import datetime

def profile(request):
	if request.user.is_authenticated():
		context={'username': request.user.username, 'first_name' : request.user.first_name, 'last_name' : request.user.last_name, 'email' : request.user.email}
		return render_to_response('user/profile.html',context)	
	elif not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)

def register(request):
	form = UserCreationForm()
	if request.method == 'POST':
                data = request.POST.copy()
		errors = form.get_validation_errors(data)
		if not errors:
			new_user = form.save()
			return HttpResponseRedirect("/accounts/created/")
	else:
		data, errors = {}, {}
	return render_to_response("registration/register.html")

def view_complaints(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==0:
		myComplaints= Complaint.objects.filter(complainee_id=request.user.username)
		for i in myComplaints:
			i.isAccepted=i.get_isAccepted_display()
		context={'complaints' : myComplaints}
		return render_to_response("student/viewComplaint.html",context)
	elif not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
		return HttpResponseRedirect('/accounts/profile')
		


def add_complaint(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==0:
            layout = request.GET.get('layout')
            if not layout:
                layout = 'vertical'
            if request.method == 'POST':
                form = ComplaintForm(request.POST)
		if form.is_valid():
                    at = form.cleaned_data['addressed_to']
		    ct = form.cleaned_data['complaint_type']
		    dt = form.cleaned_data['details']
		    Cmp=Complaint(complainee_id=request.user.username,addressedto_id=at, complaint_type=ct,details=dt,complaint_timestamp=datetime.date.today(),)
		    Cmp.save()
		    return HttpResponseRedirect('/accounts/profile')
            else:
                form = ComplaintForm()
            return render_to_response('form_complaint.html', RequestContext(request, {
            'form': form,
            'layout': layout,
            }))
	elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
            return HttpResponseRedirect('/accounts/profile')

