from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django_tables2   import RequestConfig
from mainapp.models import Complaint,DuesItem
from mainapp.staffForms import ComplaintForm,DuesForm,DuesForm1
from mainapp.staffTables import ComplaintTable,DuesTable1

import datetime


def view_complaints(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==2:
		p=Complaint.objects.filter(addressedto_id='staff')
		p=p.exclude(forwardto_id='warden')
		table = ComplaintTable(p)
		RequestConfig(request).configure(table)
		return render(request, 'staff/viewComplaint.html', {'table': table})
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
			form=ComplaintForm(request.POST)
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
			form = ComplaintForm(instance = complaints)
	    

            return render_to_response('staff/act_on_complaint.html', RequestContext(request, {
            'form': form,
            'layout': layout,
            }))
	elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
            return HttpResponseRedirect('/accounts/profile')
            
            
def view_Dues(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==2:
		p=DuesItem.objects.all()
		table= DuesTable1(p)
		RequestConfig(request).configure(table)
		return render(request, 'staff/viewDues.html', {'table': table})
	elif not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
		return HttpResponseRedirect('/accounts/profile')
		
		
def add_Dues(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==2:
		layout= request.GET.get('layout')
		if not layout:
			layout='vertical'
		if request.method == 'POST':
			form = DuesForm(request.POST)
			if form.is_valid():
				amt= form.cleaned_data['set_dues']
				dt=form.cleaned_data['duesdetails']
				di_type = form.cleaned_data['duesitem_type']
				payee_id = form.cleaned_data['payee_id']
				Dues=DuesItem(payee_id=payee_id,set_dues=amt,duesitem_type=di_type,submitted='not submitted' ,duesdetails=dt,submission_timestamp=datetime.date.today())
				Dues.save()
				return HttpResponseRedirect('/staff/home')
		else:
			form = DuesForm
		return render_to_response('staff/add_dues.html', RequestContext(request, {
			'form': form,
			'layout':layout,
		}))
	elif not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
		return HttpResponseRedirect('/accounts/profile')
		
		
def delete_dues(request,id):
	if request.user.is_authenticated() and request.user.get_profile().userType==2 or request.user.get_profile().userType==3:
	    layout = request.GET.get('layout')
	    if not layout:
		layout = 'vertical'
		dues=DuesItem.objects.get(pk=id)
		dues.delete()
		return HttpResponseRedirect('/staff/viewDues')

	elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
            return HttpResponseRedirect('/accounts/profile')
            
def act_on_dues(request,id):
	if request.user.is_authenticated() and request.user.get_profile().userType==2:
		layout = request.GET.get('layout')
		if not layout:
			layout = 'vertical'
			
		p=DuesItem.objects.get(pk=id)
		if p.submitted=='not submitted':
			return HttpResponseRedirect('/student/viewDues')
		if request.method == 'POST':
			form=DuesForm1(request.POST)
			if form.is_valid():
				p.isApproved_staff=form.cleaned_data['isApproved_staff']
				p.status = form.cleaned_data['status']
				p.save()		    
				return HttpResponseRedirect('/staff/viewDues')
		else:
			dues=DuesItem.objects.get(pk=id)
			form = DuesForm1(instance = dues)
	        return render_to_response('staff/act_on_dues.html', RequestContext(request, {
            'form': form,
            'layout': layout,
            }))
	elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
            return HttpResponseRedirect('/accounts/profile')


