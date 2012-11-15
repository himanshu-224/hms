from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django_tables2   import RequestConfig

from mainapp.models import *
from mainapp.hecForms import *
from mainapp.hecTables import *
import datetime

def create_boudget(request) :
	return

def view_boudget(request) :
	return

def modify_boudget(request, id) :
	return
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
def create_mess_menu(request) :
	return

def modify_mess_menu(request, id) :
	return

def create_mess_bill(request) :
	return

def modify_mess_bill(request,id) :
	return

def arrange_meeting(request) :
	return

def modify_meeting(request, id) :
	return 
def add_item(request):
    if request.user.is_authenticated() and request.user.get_profile().userType==1:
            if request.method == 'POST':
                form = AddItemForm(request.POST)
                if form.is_valid():
                    at = form.cleaned_data['item_id']
                    ct = form.cleaned_data['name']
                    dt = form.cleaned_data['no_total']
                    et = form.cleaned_data['issued_for']
                    ft = form.cleaned_data['fine_rate']
                    data=InventoryItem(item_id=at,name=ct, no_total=dt,date_added=datetime.date.today(), fine_rate=ft, issued_for=et)
                    data.save()
                    return HttpResponseRedirect('/hec/home')
            else:
                form = AddItemForm()
            return render_to_response('hec/form_add_item.html', RequestContext(request, {
            'form': form,
            }))
    elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
            return HttpResponseRedirect('/accounts/profile')

def view_item(request):
    if request.user.is_authenticated() and request.user.get_profile().userType==1:
        table = InventoryItemTable(InventoryItem.objects.all())
        RequestConfig(request).configure(table)
        return render(request, 'hec/view_item.html', {'table': table})
    elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
            return HttpResponseRedirect('/accounts/profile')
            
         
def issue_item(request,id):
    if request.user.is_authenticated() and request.user.get_profile().userType==1:
            if request.method == 'POST':
                form = IssueItemForm(request.POST)
                if form.is_valid():
                    at = form.cleaned_data['issuer_id']
                    bt = form.cleaned_data['item_id']
                    data=InventoryItem(issuer_id=at,item_id=bt,issue_timestamp=datetime.datetime.today())
                    data.save()
                    return HttpResponseRedirect('/hec/home')
            else:
                form = IssueItemForm()
            return render_to_response('hec/form_add_item.html', RequestContext(request, {
            'form': form,
            }))
    elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
            return HttpResponseRedirect('/accounts/profile')    
            

def delete_item(request,id):
    if request.user.is_authenticated() and request.user.get_profile().userType==0:
        complaints=Complaint.objects.get(pk=id)
        if complaints.complainee_id == request.user.username and complaints.isAccepted=='Pending':
            complaints.delete()
        return HttpResponseRedirect('/student/viewComplaints')

    elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
            return HttpResponseRedirect('/accounts/profile')            
            
            
def return_item(request,id):
    if request.user.is_authenticated() and request.user.get_profile().userType==0:
        complaints=Complaint.objects.get(pk=id)
        if complaints.complainee_id == request.user.username and complaints.isAccepted=='Pending':
            complaints.delete()
        return HttpResponseRedirect('/student/viewComplaints')

    elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
            return HttpResponseRedirect('/accounts/profile')              
