from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django_tables2   import RequestConfig

from mainapp.models import Complaint
from mainapp.models import Election
from mainapp.wardenForms import ComplaintForm
from mainapp.wardenForms import StartElectionForm
from mainapp.wardenForms import CandidateNominationForm
from mainapp.wardenTables import ComplaintTable
from django.forms.formsets import formset_factory

import datetime


def view_complaints(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==3:
		table = ComplaintTable(Complaint.objects.filter(addressedto_id='warden'))
		RequestConfig(request).configure(table)
		return render(request, 'warden/viewComplaint.html', {'table': table})
	elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
            return HttpResponseRedirect('/accounts/profile')


def act_on_complaint(request,id):
	if request.user.is_authenticated() and request.user.get_profile().userType==3:
	    layout = request.GET.get('layout')
	    if not layout:
		layout = 'vertical'
		if request.method == 'POST':
			form=ComplaintForm(request.POST)
			if form.is_valid():
				p=Complaint.objects.get(pk=id)
				p.status = form.cleaned_data['status']
				p.isAccepted = form.cleaned_data['isAccepted']
				p.reason = form.cleaned_data['reason']
				p.save()		    
				return HttpResponseRedirect('/warden/viewComplaints')
		    
		else:
			complaints=Complaint.objects.get(pk=id)
			form = ComplaintForm(instance = complaints)
	    

            return render_to_response('warden/act_on_complaint.html', RequestContext(request, {
            'form': form,
            'layout': layout,
            }))
	elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
            return HttpResponseRedirect('/accounts/profile')


def conduct_election(request):
	if request.user.is_authenticated() and request.user.get_profile().userType == 3 :
		layout = request.GET.get('layout')
		if not layout :
			layout = 'vertical'
		if request.method == 'POST' :
			form = StartElectionForm(request.POST)
			#electionFormset = formset_factory(CandidateNominationForm, extra=10, max_num = 2)
			#el_formset = electionFormset()
			#for form in el_formset.forms :
			#	form 
			#	data = request.POST.copy()
			#if form.is_valid() :
			if form.is_valid() : 
				form = StartElectionForm() ## store in table
				data, errors = {}, {}
				return render_to_response("warden/election.html", RequestContext(request, {
				'form' : form,
				'layout' : layout,
				}))
		else :
			form = StartElectionForm()
			data, errors = {}, {}
		return render_to_response("warden/election.html", RequestContext(request, {
		'form' : form,
		'layout' : layout,
		}))
	elif not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
		return HttpResponseRedirect('/accounts/profile')
	return 
	
def add_candidate(request) :
	if request.user.is_authenticated() and request.user.get_profile().userType == 3 :
		layout = request.GET.get('layout')
		if not layout :
			layout = 'vertical'
			return HttpResponseRedirect('/accounts/profile')
		if request.method == 'POST' :
			return HttpResponseRedirect('/accounts/profile')
	elif not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
		return HttpResponseRedirect('/accounts/profile') 
	