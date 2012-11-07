from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django_tables2   import RequestConfig

from mainapp.models import Complaint
from mainapp.staffForms import StaffComplaintForm
from mainapp.staffTables import ComplaintTable

import datetime


def view_complaints(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==2:
		table = ComplaintTable(Complaint.objects.all())
		RequestConfig(request).configure(table)
		return render(request, 'staff/staffComplaint.html', {'table': table})
	elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
            return HttpResponseRedirect('/accounts/profile')


def act_on_complaint(request,id):
	if request.user.is_authenticated() and request.user.get_profile().userType==2:
	    layout = request.GET.get('layout')
	    if not layout:
		layout = 'vertical'
		if request.method == 'POST':
			form=StaffComplaintForm(request.POST)
			if form.is_valid():
				p=Complaint.objects.get(pk=id)
				p.forwardto_id=form.cleaned_data['forwardto_id']
				p.status = form.cleaned_data['status']
				p.isAccepted = form.cleaned_data['isAccepted']
				p.reason = form.cleaned_data['reason']
				p.save()		    
				return HttpResponseRedirect('/staff/viewComplaints')
		    
		else:
			complaints=Complaint.objects.get(pk=id)
			form = StaffComplaintForm(instance = complaints)
	    

            return render_to_response('staff/act_on_complaint.html', RequestContext(request, {
            'form': form,
            'layout': layout,
            }))
	elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
            return HttpResponseRedirect('/accounts/profile')


