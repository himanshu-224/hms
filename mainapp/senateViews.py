from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.forms import UserCreationForm
from mainapp.models import Complaint
from mainapp.forms import ComplaintForm

from mainapp.models import Policy
from django.views.decorators.csrf import csrf_exempt

import datetime


def pending_requests(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==5:
		pending1 = Policy.objects.filter(requestedTo="SS", status = "NPR")
		pending2 = Policy.objects.filter(requestedTo="SS", status = "PFC")
		pending3 = Policy.objects.filter(requestedTo="SS", status = "PFD")
		pending4 = Policy.objects.filter(requestedTo="DS", status = "NPR")
		pending5 = Policy.objects.filter(requestedTo="DS", status = "PFC")
		pending6 = Policy.objects.filter(requestedTo="DS", status = "PFD")
		return render_to_response('senate/pendingRequests.html', {'pending1': pending1, 'pending2': pending2, 'pending3': pending3, 'l1' : len(pending1), 'l2' : len(pending2), 'l3' : len(pending3), 'pending4': pending4, 'pending5': pending5, 'pending6': pending6 })

def accept_request(request, pid):
	if request.user.is_authenticated() and request.user.get_profile().userType==5:
		p = Policy.objects.get(id=pid)
		if p.status == "PFD":
			p.delete()
		else:		
			p.statement = p.proposal
			p.proposal = ""
			p.status = "APP"
			p.requestedTo = ""
			p.save()
        return HttpResponseRedirect('/senate/pendingRequests')
 		        
def reject_request(request, pid):
	if request.user.is_authenticated() and request.user.get_profile().userType==5:
		p = Policy.objects.get(id=pid)
		if p.status == "NPR":
			p.delete()
		else:
			p.status == "APP"
			p.proposal = ""
			p.requestedTo = ""
			p.save()
		return HttpResponseRedirect('/senate/pendingRequests')

def create_policy(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==5:
		return render_to_response('senate/createPolicy.html')

def delete_policy(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==5:
		pol = Policy.objects.filter(status = "APP")
		return render_to_response('senate/deletePolicy.html', {'pol': pol})

def delete_request(request, pid):
	if request.user.is_authenticated() and request.user.get_profile().userType==5:
		p = Policy.objects.get(id=pid)
		p.status = "PFD"
		p.requestedTo = "DS"
		p.save()
		return HttpResponseRedirect('/senate/deletePolicy')

def change_policy(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==5:
		pol = Policy.objects.filter(status = "APP")
		return render_to_response('senate/changePolicy.html', {'pol': pol})

def change_request(request, pid):
	if request.user.is_authenticated() and request.user.get_profile().userType==5:
		pol = Policy.objects.get(id = pid)
		return render_to_response('senate/modifyPolicy.html', {'pol': pol})

def delete_proposal(request, pid):
	if request.user.is_authenticated() and request.user.get_profile().userType==5:
		pol = Policy.objects.get(id = pid)
		if pol.status == "NPR":
			pol.delete()
		else:
			pol.status = ""
			pol.proposal = ""
			pol.requestedTo = ""
			pol.save()
		return HttpResponseRedirect('/senate/pendingRequests')
		
		
@csrf_exempt
def submit_change_request(request, pid):
	if request.user.is_authenticated() and request.user.get_profile().userType==5:
		if request.POST['policy'] == "" or request.POST['policy'].isspace():
			return HttpResponseRedirect('/senate/changePolicy')
		else:		
			pol = Policy.objects.get(id = pid)
			pol.proposal = request.POST['policy']
			pol.status = "PFC"
			pol.requestedTo = "DS"
			pol.save() 
			return HttpResponseRedirect('/senate/changePolicy')

@csrf_exempt
def submit_policy(request, req):
	if request.user.is_authenticated() and request.user.get_profile().userType==5: 
		if request.POST['policy'] == "" or request.POST['policy'].isspace():
			return HttpResponseRedirect('/senate/createPolicy') 		
		elif req == "NPR":
			p = Policy(proposal = request.POST['policy'], status = "NPR", requestedTo = "DS")
			p.save()
			return render_to_response('senate/submitPolicy.html')
		elif req == "PFC":
			p = Policy(proposal = request.POST['policy'], status = "PFC", requestedTo = "DS")
			p.save()
			return render_to_response('senate/submitPolicy.html')	
		elif req == "PFD":
			p = Policy(proposal = request.POST['policy'], status = "PFD", requestedTo = "DS")
			p.save()
			return render_to_response('senate/submitPolicy.html')	



