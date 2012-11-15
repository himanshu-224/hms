from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django_tables2   import RequestConfig
from django.template.context import RequestContext
from django.contrib.auth.forms import UserCreationForm

from mainapp.tables import *
from mainapp.models import *
from mainapp.forms import *

from mainapp.studentForms import ComplaintForm,DuesForm
from mainapp.studentTables import ComplaintTable,DuesTable
from django.contrib.auth.models import User
import datetime

userTypes={0:'student', 1:'hec',2:'staff',3:'warden', 4:'dosa', 5:'senate'}

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

def update_info(request) :
	if request.user.is_authenticated() :
		layout = request.GET.get('layout')
		if not layout:
			layout = 'vertical'
		if request.method == 'POST' :
			
			form = UpdateInfoForm(request.POST)
			data = request.POST.copy()
			if form.is_valid() :
				#user = form.save()
				name = User.objects.get(username = request.user.username)
				name.first_name = form.cleaned_data['first_name']
				name.last_name = form.cleaned_data['last_name']
				name.email = form.cleaned_data['email']
				name.save()
				return HttpResponseRedirect("/accounts/profile")
		else :
			name = User.objects.get(username = request.user.username)
			form = UpdateInfoForm(instance=name)
			data, errors = {}, {}
		return render_to_response("registration/updateInfo.html", RequestContext(request, {
		'form' : form,
		'layout' : layout,
		}))
	elif not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
		return HttpResponseRedirect('/accounts/profile')
		
	
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

'''
Messages Functionalities
'''
def inbox(request):
	if request.user.is_authenticated():
		table = inboxTable(inboxMessage.objects.filter(receiverlist=request.user.username))

def inbox(request):
	if request.user.is_authenticated():
		table = inboxTable(inboxMessage.objects.filter(receiverlist=request.user.username))
		
		RequestConfig(request).configure(table)
		for i in range(len(userTypes)):
			if request.user.get_profile().userType==i:
				return render(request, userTypes[i]+'/inbox.html', {'table': table})		
	elif not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)

	else:
		return HttpResponseRedirect('/accounts/profile')

def outbox(request):
	if request.user.is_authenticated():
		table = outboxTable(outboxMessage.objects.filter(sender=request.user.username))
		RequestConfig(request).configure(table)
		for i in range(len(userTypes)):
			if request.user.get_profile().userType==i:
				return render(request, userTypes[i]+'/outbox.html', {'table': table})		
	elif not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
		return HttpResponseRedirect('/accounts/profile')
		

def compose_message(request):
	if request.user.is_authenticated():
            layout = request.GET.get('layout')
            if not layout:
                layout = 'vertical'
            if request.method == 'POST':
				form = MessageForm(request.POST)
				if form.is_valid():
					at = form.cleaned_data['To']
					ct = form.cleaned_data['subject']
					dt = form.cleaned_data['message']
					Cmp=inboxMessage(sender=request.user.username,receiverlist=at, subject=ct,message=dt,timestamp=datetime.date.today(),)
					Cmp.save()
					Cmp=outboxMessage(sender=request.user.username,receiverlist=at, subject=ct,message=dt,timestamp=datetime.date.today(),)
					Cmp.save()
					for i in range(len(userTypes)):
						if request.user.get_profile().userType==i:
							return HttpResponseRedirect('/'+userTypes[i]+'/outbox')
            else:
                form = MessageForm()
                for i in range(len(userTypes)):
						if request.user.get_profile().userType==i:
							return render_to_response(userTypes[i]+'/compose_message.html', RequestContext(request, {
							'form': form,
							'layout': layout,
							}))
				
	elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
            return HttpResponseRedirect('/accounts/profile')

def show_message(request,id):
	if request.user.is_authenticated():
	    layout = request.GET.get('layout')
	    if not layout:
		layout = 'vertical'
		m=inboxMessage.objects.get(pk=id)
		#m=outboxMessage.objects.get(pk=id[0])
def showInbox_message(request,id):
	if request.user.is_authenticated():
		layout = request.GET.get('layout')
		if not layout:
			layout = 'vertical'
		m=inboxMessage.objects.get(pk=id)
		subject=m.subject
		msg=m.message
		timestamp=m.timestamp
		m.isRead='read'
		m.save()
		#msg=inboxMessage(sender=m.sender,receiverlist=m.receiverlist,subject=m.subject,message=m.message,timestamp=m.timestamp,m.isRead='read')
		#msg.save()
		for i in range(len(userTypes)):
						if request.user.get_profile().userType==i:
							return render_to_response(userTypes[i]+'/show_message.html', RequestContext(request, {
							'sender':m.sender,
							'subject':m.subject,
							'timestamp':m.timestamp,
							'message':m.message
							}))		

	elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
            return HttpResponseRedirect('/accounts/profile')

		
#def delete_message(request,id):

def deleteInbox_message(request,id):
	
	if request.user.is_authenticated():
		layout = request.GET.get('layout')
		if not layout:
			layout = 'vertical'
		messages=inboxMessage.objects.get(pk=id)
		messages.delete() 
		for i in range(len(userTypes)):
			if request.user.get_profile().userType==i:
				return HttpResponseRedirect('/'+userTypes[i]+'/inbox')
			'''messages=outboxMessage.objects.get(pk=id)
			messages.delete() 
			for i in range(len(userTypes)):
				if request.user.get_profile().userType==i:
					return HttpResponseRedirect('/'+userTypes[i]+'/outbox')'''
	elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
            return HttpResponseRedirect('/accounts/profile')
            

def showOutbox_message(request,id):
	if request.user.is_authenticated():
		layout = request.GET.get('layout')
		if not layout:
			layout = 'vertical'
		m=outboxMessage.objects.get(pk=id)
		subject=m.subject
		msg=m.message
		timestamp=m.timestamp
		m.isRead='read'
		m.save()
		for i in range(len(userTypes)):
					if request.user.get_profile().userType==i:
						return render_to_response(userTypes[i]+'/show_message.html', RequestContext(request, {
						'sender':m.sender,
						'subject':m.subject,
						'timestamp':m.timestamp,
						'message':m.message
						}))		    


	elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
            return HttpResponseRedirect('/accounts/profile')

		
def deleteOutbox_message(request,id):
	
	if request.user.is_authenticated():
		layout = request.GET.get('layout')
		if not layout:
			layout = 'vertical'
		messages=outboxMessage.objects.get(pk=id)
		messages.delete() 
		for i in range(len(userTypes)):
			if request.user.get_profile().userType==i:
				return HttpResponseRedirect('/'+userTypes[i]+'/outbox')
	elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
            return HttpResponseRedirect('/accounts/profile')
            
def pay_dues(request,id):
	if request.user.is_authenticated() and request.user.get_profile().userType==0:
		layout = request.GET.get('layout')
		if not layout:
			layout = 'vertical'
		Dues=DuesItem.objects.get(pk=id)
		if Dues.payee_id == request.user.username and Dues.submitted=='submitted':
			return HttpResponseRedirect('/student/viewDues')
		
		elif request.method == 'POST':
			form = DuesForm(request.POST)
			if form.is_valid():
				amt= form.cleaned_data['pay_dues']
				payInf= form.cleaned_data['paymentInfo']
				Dues.pay_dues=amt
				Dues.submitted='submitted'
				Dues.paymentInfo = payInf
				Dues.submission_timestamp=datetime.date.today()
				Dues.save()
				return HttpResponseRedirect('/student/home')
		else:
			form = DuesForm()
		return render_to_response('student/pay_dues.html', RequestContext(request, {
		'form': form,
		'layout':layout,
		}))
	elif not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
		return HttpResponseRedirect('/accounts/profile')
		
def view_dues(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==0:
		table = DuesTable(DuesItem.objects.filter(payee_id=request.user.username ,submitted = "not submitted" ))
		RequestConfig(request).configure(table)
		return render(request,'student/viewDues.html',{'table': table})
	elif not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/next=%s' % request.path)
	else:
		return HttpResponseRedirect('/accounts/profile')

def view_paid_dues(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==0:
		table = DuesTable(DuesItem.objects.filter(payee_id=request.user.username,submitted = "submitted"))
		RequestConfig(request).configure(table)
		return render(request,'student/viewDues.html',{'table': table})
	elif not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/next=%s' % request.path)
	else:
		return HttpResponseRedirect('/accounts/profile')
            
            
            
