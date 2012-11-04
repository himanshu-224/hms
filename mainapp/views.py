from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
#from django import oldforms as forms
from django.contrib.auth.forms import UserCreationForm
from mainapp.models import Complaint

def profile(request):
	if request.user.is_authenticated():
		context={'username': request.user.username, 'first_name' : request.user.first_name, 'last_name' : request.user.last_name, 'email' : request.user.email}
		return render_to_response('user/profile.html',context)	
	elif not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)

def register(request):
	form = UserCreationForm()
	if request.method == 'POST':
		data = request.POST.copy()
		errors = form.get_validation_errors(data)
		if not errors:
			new_user = form.save()
			return HttpResponseRedirect("/accounts/created/")
	else:
		data, errors = {}, {}
	return render_to_response("registration/register.html")

def view_complaints_student(request):
	if request.user.is_authenticated() and request.user.get_profile().userType==0:
		myComplaints= Complaint.objects.filter(complainee_id=request.user.username)
		for i in myComplaints:
			if i.isAccepted==0:
				i.isAccepted='Accepted'
			elif i.isAccepted==1:
				i.isAccepted='Rejected'
			elif i.isAccepted==2:
				i.isAccepted='Pending'
		context={'complaints' : myComplaints}
		return render_to_response("student/viewComplaint.html",context)
	elif not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	else:
		return HttpResponseRedirect('/accounts/profile')
		


	


