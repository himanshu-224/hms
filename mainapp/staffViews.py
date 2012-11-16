from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django_tables2   import RequestConfig

from mainapp.models import Complaint,DuesItem,MessBill
from mainapp.staffForms import ComplaintForm,DuesForm,DuesForm1,MessBillForm,MessBillForm1,MessBillForm2
from mainapp.staffTables import ComplaintTable,DuesTable1,MessBillTable

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
           
def createbill(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==2:
		layout= request.GET.get('layout')
		if not layout:
			layout='vertical'
		if request.method == 'POST':
			form = MessBillForm(request.POST)
			if form.is_valid():
				no_of_days=form.cleaned_data['no_of_days']
				rebate_days = form.cleaned_data['rebate_days']
				dt=form.cleaned_data['details']
				amt = form.cleaned_data['basic_amount']
				extra= form.cleaned_data['extra']
				payee_id = form.cleaned_data['payee_id']
				month = form.cleaned_data['month']
				Messbill=MessBill(payee_id=payee_id,month=month,no_of_days=no_of_days,rebate_days=rebate_days,basic_amount=amt,extra=extra,total_bill=((no_of_days-rebate_days)*amt+extra),details=dt,submitted='not submitted' ,submission_timestamp=datetime.date.today())
				Messbill.save()
				return HttpResponseRedirect('/staff/home')
		else:
			form = MessBillForm
		return render_to_response('staff/add_messbill.html', RequestContext(request, {
			'form': form,
			'layout':layout,
		}))
	elif not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
		return HttpResponseRedirect('/accounts/profile')
		
def view_MessBill(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==2:
		p=MessBill.objects.all()
		table= MessBillTable(p)
		RequestConfig(request).configure(table)
		return render(request, 'staff/viewMessBill.html', {'table': table})
	elif not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
		return HttpResponseRedirect('/accounts/profile')
### need to change		
def update_messbill(request,id):
	if request.user.is_authenticated() and request.user.get_profile().userType==2:
		layout = request.GET.get('layout')
		if not layout:
			layout = 'vertical'
			
		p=MessBill.objects.get(pk=id)
		if p.submitted=='submitted':
			return HttpResponseRedirect('/student/viewMessBill')
		if request.method == 'POST':
			form=MessBillForm1(request.POST)
			if form.is_valid():
				p.no_of_days=form.cleaned_data['no_of_days']
				p.rebate_days = form.cleaned_data['rebate_days']
				p.details=form.cleaned_data['details']
				p.basic_amount= form.cleaned_data['basic_amount']
				p.extra= form.cleaned_data['extra']
				p.month = form.cleaned_data['month']
				p.save()		    
				return HttpResponseRedirect('/staff/viewMessBill')
		else:
			Bill=MessBill.objects.get(pk=id)
			form = MessBillForm1(instance = Bill)
	        return render_to_response('staff/updateMessBill.html', RequestContext(request, {
            'form': form,
            'layout': layout,
            }))
	elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
            return HttpResponseRedirect('/accounts/profile')
            
def act_on_messBill(request,id):
	if request.user.is_authenticated() and request.user.get_profile().userType==2:
		layout = request.GET.get('layout')
		if not layout:
			layout = 'vertical'
			
		p=MessBill.objects.get(pk=id)
		if p.submitted=='not submitted':
			return HttpResponseRedirect('/student/viewMessBill')
		if request.method == 'POST':
			form=MessBillForm2(request.POST)
			if form.is_valid():
				p.isVerified_staff=form.cleaned_data['isVerified_staff']
				p.status = form.cleaned_data['status']
				p.save()		    
				return HttpResponseRedirect('/staff/viewDues')
		else:
			Bill=MessBill.objects.get(pk=id)
			form = MessBillForm2(instance = Bill)
	        return render_to_response('staff/act_on_messBill.html', RequestContext(request, {
            'form': form,
            'layout': layout,
            }))
	elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
            return HttpResponseRedirect('/accounts/profile')


