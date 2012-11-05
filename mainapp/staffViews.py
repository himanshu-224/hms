from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.forms import UserCreationForm
from mainapp.models import Complaint
from mainapp.staffForms import StaffComplaintForm, StaffComplaintViewForm

import datetime


def view_complaints(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==2:
	    layout = request.GET.get('layout')
	    if not layout:
		layout = 'vertical'
	    p=Complaint.objects.filter(addressedto_id='staff')
	    p=p.filter(isAccepted='pending')
	    forms=[]
	    context={}
            if request.method == 'POST':
		for i in request.POST.keys():
		    if request.POST[i]=='Select':
			id=i
			
		return HttpResponseRedirect('/staff/actOnComplaint/id=%s' %id)
            else:
		for complaints in p:
		    default_dict={}
		    default_dict['complainee_id']=complaints.complainee_id
		    default_dict['addressed_to'] = complaints.addressedto_id
		    default_dict['forwarded_to'] = complaints.forwardto_id
		    default_dict['complaint_timestamp']=complaints.complaint_timestamp
		    default_dict['complaint_type']=complaints.complaint_type
		    default_dict['details'] = complaints.details
		    default_dict['status']=complaints.status
		    default_dict['is_Accepted'] = complaints.isAccepted
		    form=StaffComplaintViewForm(default_dict)
		    form.id=complaints.id
		    forms.append(form)
		    context['forms']=forms

            return render_to_response('staff/view_complaints.html', RequestContext(request, {
            'forms': forms,
            'layout': layout,
            }))
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
		    p.status = form.cleaned_data['status']
		    p.isAccepted = form.cleaned_data['is_Accepted']
		    p.reason = form.cleaned_data['reason']
		    p.save()		    
		    return HttpResponseRedirect('/staff/viewComplaints')
            else:
		complaints=Complaint.objects.get(pk=id)
		default_dict={}
		default_dict['complainee_id']=complaints.complainee_id
		default_dict['addressed_to'] = complaints.addressedto_id
		default_dict['forwarded_to'] = complaints.forwardto_id
		default_dict['complaint_timestamp']=complaints.complaint_timestamp
		default_dict['complaint_type']=complaints.complaint_type
		default_dict['details'] = complaints.details
		default_dict['status']=complaints.status
		default_dict['is_Accepted'] = complaints.isAccepted
		form=StaffComplaintForm(default_dict)		
	    

            return render_to_response('staff/act_on_complaint.html', RequestContext(request, {
            'form': form,
            'layout': layout,
            }))
	elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
            return HttpResponseRedirect('/accounts/profile')


