from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django_tables2   import RequestConfig

from mainapp.models import Complaint
from mainapp.dosaForms import ComplaintForm
from mainapp.dosaTables import ComplaintTable
from mainapp.models import Policy
from django.views.decorators.csrf import csrf_exempt


import datetime


def view_complaints(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==4:
		table = ComplaintTable(Complaint.objects.filter(addressedto_id='dosa'))
		RequestConfig(request).configure(table)
		return render(request, 'dosa/viewComplaint.html', {'table': table})
	elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
            return HttpResponseRedirect('/accounts/profile')


def act_on_complaint(request,id):
	if request.user.is_authenticated() and request.user.get_profile().userType==4:
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
				return HttpResponseRedirect('/dosa/viewComplaints')
		    
		else:
			complaints=Complaint.objects.get(pk=id)
			form = ComplaintForm(instance = complaints)
	    

            return render_to_response('dosa/act_on_complaint.html', RequestContext(request, {
            'form': form,
            'layout': layout,
            }))
	elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
            return HttpResponseRedirect('/accounts/profile')

def pending_requests(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==4:
		pending1 = Policy.objects.filter(requestedTo="DS", status = "NPR")
		pending2 = Policy.objects.filter(requestedTo="DS", status = "PFC")
		pending3 = Policy.objects.filter(requestedTo="DS", status = "PFD")
		pending4 = Policy.objects.filter(requestedTo="SS", status = "NPR")
		pending5 = Policy.objects.filter(requestedTo="SS", status = "PFC")
		pending6 = Policy.objects.filter(requestedTo="SS", status = "PFD")
		return render_to_response('dosa/pendingRequests.html', {'pending1': pending1, 'pending2': pending2, 'pending3': pending3, 'l1' : len(pending1), 'l2' : len(pending2), 'l3' : len(pending3), 'pending4': pending4, 'pending5': pending5, 'pending6': pending6 })

def accept_request(request, pid):
	if request.user.is_authenticated() and request.user.get_profile().userType==4:
		p = Policy.objects.get(id=pid)
		if p.status == "PFD":
			p.delete()
		else:		
			p.statement = p.proposal
			p.proposal = ""
			p.status = "APP"
			p.requestedTo = ""
			p.save()
        return HttpResponseRedirect('/dosa/pendingRequests')
 		        
def reject_request(request, pid):
	if request.user.is_authenticated() and request.user.get_profile().userType==4:
		p = Policy.objects.get(id=pid)
		if p.status == "NPR":
			p.delete()
		else:
			p.status == "APP"
			p.proposal = ""
			p.requestedTo = ""
			p.save()
		return HttpResponseRedirect('/dosa/pendingRequests')

def create_policy(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==4:
		return render_to_response('dosa/createPolicy.html')

def delete_policy(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==4:
		pol = Policy.objects.filter(status = "APP")
		return render_to_response('dosa/deletePolicy.html', {'pol': pol})

def delete_request(request, pid):
	if request.user.is_authenticated() and request.user.get_profile().userType==4:
		p = Policy.objects.get(id=pid)
		p.status = "PFD"
		p.requestedTo = "SS"
		p.save()
		return HttpResponseRedirect('/dosa/deletePolicy')

def change_policy(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==4:
		pol = Policy.objects.filter(status = "APP")
		return render_to_response('dosa/changePolicy.html', {'pol': pol})

def change_request(request, pid):
	if request.user.is_authenticated() and request.user.get_profile().userType==4:
		pol = Policy.objects.get(id = pid)
		return render_to_response('dosa/modifyPolicy.html', {'pol': pol})

def delete_proposal(request, pid):
	if request.user.is_authenticated() and request.user.get_profile().userType==4:
		pol = Policy.objects.get(id = pid)
		if pol.status == "NPR":
			pol.delete()
		else:
			pol.status = ""
			pol.proposal = ""
			pol.requestedTo = ""
			pol.save()
		return HttpResponseRedirect('/dosa/pendingRequests')
		
		
@csrf_exempt
def submit_change_request(request, pid):
	if request.user.is_authenticated() and request.user.get_profile().userType==4:
		if request.POST['policy'] == "" or request.POST['policy'].isspace():
			return HttpResponseRedirect('/dosa/changePolicy')
		else:		
			pol = Policy.objects.get(id = pid)
			pol.proposal = request.POST['policy']
			pol.status = "PFC"
			pol.requestedTo = "SS"
			pol.save() 
			return HttpResponseRedirect('/dosa/changePolicy')

@csrf_exempt
def submit_policy(request, req):
	if request.user.is_authenticated() and request.user.get_profile().userType==4: 
		if request.POST['policy'] == "" or request.POST['policy'].isspace():
			return HttpResponseRedirect('/dosa/createPolicy') 		
		elif req == "NPR":
			p = Policy(proposal = request.POST['policy'], status = "NPR", requestedTo = "SS")
			p.save()
			return render_to_response('dosa/submitPolicy.html')
		elif req == "PFC":
			p = Policy(proposal = request.POST['policy'], status = "PFC", requestedTo = "SS")
			p.save()
			return render_to_response('dosa/submitPolicy.html')	
		elif req == "PFD":
			p = Policy(proposal = request.POST['policy'], status = "PFD", requestedTo = "SS")
			p.save()
			return render_to_response('dosa/submitPolicy.html')	

	




