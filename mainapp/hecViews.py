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
            item=InventoryItem.objects.get(item_id=id)
            if item.no_total>item.no_issued:
                if request.method == 'POST':
                    form = IssueItemForm(request.POST)
                    if form.is_valid():
                        at = form.cleaned_data['issuer_id']
                        item.no_issued+=1
                        item.save()
                        data=InventoryIssue(issuer_id=at,item_id=item,issue_timestamp=datetime.date.today(), return_timestamp=datetime.date.today())
                        data.save()
                        return HttpResponseRedirect('/hec/viewItem')
                else:
                    form = IssueItemForm()
                return render_to_response('hec/form_add_item.html', RequestContext(request, {
                'form': form,
                }))
                
            else:
                message="Cannot Issue Item " +item.item_id +" as it is already issued"
                return render_to_response('hec/form_message.html', RequestContext(request,{'message':message }))
    elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
            return HttpResponseRedirect('/accounts/profile')    
            

def delete_item(request,id):
    if request.user.is_authenticated() and request.user.get_profile().userType==1:
        item=InventoryItem.objects.get(item_id=id)
        if item.no_issued==0:
            item.delete()
        else:
            message="Cannot Delete Item " +item.item_id +" as it is issued to someone."            
            return render_to_response('hec/form_message.html', RequestContext(request,{'message':message }))
        return HttpResponseRedirect('/hec/viewItem')

    elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
            return HttpResponseRedirect('/accounts/profile')            
            
            
def return_item(request,id):
    if request.user.is_authenticated() and request.user.get_profile().userType==1:
        item=InventoryIssue.objects.get(pk=id)
        itemType=item.item_id
        if item.isReturned == 'No':
            item.isReturned='Yes'
            item.return_timestamp=datetime.date.today()
            delta=item.return_timestamp-item.issue_timestamp
            item.issued_duration=delta.days;
            if item.issued_duration > itemType.issued_for:
                item.fine = itemType.fine_rate * (item.issued_duration - itemType.issued_for)
            item.save()
            itemType.no_issued-=1
            itemType.save()
        else:
            message="Cannot Return Item " +itemType.item_id +" issued by "+ item.issuer_id.username+" as it has already been returned."            
            return render_to_response('hec/form_message.html', RequestContext(request,{'message':message }))            
        return HttpResponseRedirect('/hec/issuedStatus/id='+itemType.item_id)

    elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
            return HttpResponseRedirect('/accounts/profile')              

def issued_status(request,id):
    if request.user.is_authenticated() and request.user.get_profile().userType==1:
        item=InventoryItem.objects.get(item_id=id)
        issuedItems=InventoryIssue.objects.filter(item_id=item)
        table=InventoryIssueTable(issuedItems)
        RequestConfig(request).configure(table)
        return render(request, 'hec/view_item.html', {'table': table})
    elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
            return HttpResponseRedirect('/accounts/profile')           
            

def delete_issueitem(request,id):
    if request.user.is_authenticated() and request.user.get_profile().userType==1:
        item=InventoryIssue.objects.get(pk=id)
        if item.isReturned=='Yes':
            item.delete()
        else:
            message="Cannot Delete Issue Record for " +item.item_id.item_id +" as the item has not been returned"
            return render_to_response('hec/form_message.html', RequestContext(request,{'message':message }))
        return HttpResponseRedirect('/hec/viewItem')

    elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
            return HttpResponseRedirect('/accounts/profile')   