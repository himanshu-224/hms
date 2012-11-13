from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django_tables2   import RequestConfig
from django.template.context import RequestContext
from django.contrib.auth.forms import UserCreationForm

from mainapp.models import Complaint
from mainapp.studentForms import ComplaintForm
from mainapp.studentTables import ComplaintTable

from mainapp.models import Policy

import datetime

userTypes={0:'student', 1:'hec',2:'staff',3:'dosa', 4:'dosa', 5:'senate'}

def homepage(request,template_name):
	if request.user.is_authenticated():
		context={'username': request.user.username, 'first_name' : request.user.first_name, 'last_name' : request.user.last_name, 'email' : request.user.email}
		for i in range(len(userTypes)):
			if request.user.get_profile().userType==i:
				if template_name.find(userTypes[i])!=-1:			
					return render_to_response(template_name,context)
				else:
					return HttpResponseRedirect('/accounts/profile')
		return HttpResponseRedirect('/accounts/profile')
					
	elif not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)

def profile(request):
	if request.user.is_authenticated():
		for i in range(len(userTypes)):
			if request.user.get_profile().userType==i:
				return HttpResponseRedirect('/'+userTypes[i]+'/home/')
		return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)		
	elif not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)

def register(request):
	form = UserCreationForm()
	if request.method == 'POST':
                data = request.POST.copy()
		errors = form.get_svalidation_errors(data)
		if not errors:
			new_user = form.save()
			return HttpResponseRedirect("/accounts/created/")
	else:
		data, errors = {}, {}
	return render_to_response("registration/register.html")

def view_complaints(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==0:
		table = ComplaintTable(Complaint.objects.filter(complainee_id=request.user.username))
		RequestConfig(request).configure(table)
		return render(request, 'student/viewComplaint.html', {'table': table})
		
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
					at = form.cleaned_data['addressedto_id']
					ct = form.cleaned_data['complaint_type']
					dt = form.cleaned_data['details']
					Cmp=Complaint(complainee_id=request.user.username,addressedto_id=at, complaint_type=ct,details=dt,complaint_timestamp=datetime.date.today(),)
					Cmp.save()
					return HttpResponseRedirect('/student/home')
            else:
                form = ComplaintForm()
            return render_to_response('student/form_complaint.html', RequestContext(request, {
            'form': form,
            'layout': layout,
            }))
	elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
            return HttpResponseRedirect('/accounts/profile')


def delete_complaint(request,id):
	if request.user.is_authenticated() and request.user.get_profile().userType==0:
	    layout = request.GET.get('layout')
	    if not layout:
		layout = 'vertical'
		complaints=Complaint.objects.get(pk=id)
		if complaints.complainee_id == request.user.username and complaints.isAccepted=='Pending':
			complaints.delete()
		return HttpResponseRedirect('/student/viewComplaints')

	elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
            return HttpResponseRedirect('/accounts/profile')

def view_policies(request):
	if request.user.is_authenticated():
		policies = Policy.objects.filter(status='APP')
		usr = request.user.get_profile().userType
		if usr == 0:
			return render_to_response('student/viewPolicy.html', {'policies': policies})
		elif usr == 1:
			return render_to_response('hec/viewPolicy.html', {'policies': policies})
		elif usr == 2:
			return render_to_response('staff/viewPolicy.html', {'policies': policies})
		elif usr == 3:
			return render_to_response('warden/viewPolicy.html', {'policies': policies})
		elif usr == 4:
			return render_to_response('dosa/viewPolicy.html', {'policies': policies})
		else:
			return render_to_response('senate/viewPolicy.html', {'policies': policies})
	


