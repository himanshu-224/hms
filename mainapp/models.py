from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.forms import ModelForm

class UserProfile(models.Model):
	userType_CHOICES = (
		(0, u'Student'),
		(1, u'HEC'),
		(2, u'STAFF'),
		(3, u'WARDEN'),
		(4, u'DOSA'),
		(5, u'SENATE'),
	)
	user = models.OneToOneField(User)
	userType = models.IntegerField(max_length=10, choices=userType_CHOICES,default=0)
	

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User )

class Request(models.Model):
	isAccepted_CHOICES = (
		(0, u'Accepted'),
		(1, u'Rejected'),
		(2, u'Pending'),
	)
	requester_id = models.CharField(max_length=30)
	addressedto_id = models.CharField(max_length=20)
	forwardto_id = models.CharField(max_length=20)
	request_timestamp = models.DateField(max_length=20)
	request_type = models.CharField(max_length=20)
	details = models.CharField(max_length=20)
	status = models.CharField(max_length=20)
	reason = models.CharField(max_length=20)
	isAccepted = models.IntegerField(max_length=3, choices=isAccepted_CHOICES, default=2)

class Complaint(models.Model):
	isAccepted_CHOICES = (
		(0, u'Accepted'),
		(1, u'Rejected'),
		(2, u'Pending'),
	)
	complainee_id = models.CharField(max_length=30)
	addressedto_id = models.CharField(max_length=30)
	forwardto_id = models.CharField(max_length=30,default='')
	complaint_timestamp = models.DateField(max_length=30)
	complaint_type = models.CharField(max_length=30)
	details = models.CharField(max_length=500)
	status = models.CharField(max_length=200,default='')
	reason = models.CharField(max_length=200,default='')
	isAccepted = models.IntegerField(max_length=3, choices=isAccepted_CHOICES,default=2)
	
class DuesItem(models.Model):
	isApproved_CHOICES = (
		(0, u'Accepted'),
		(1, u'Rejected'),
		(2, u'Pending'),
	)
	payee_id = models.CharField(max_length=30)
	duesitem_type = models.CharField(max_length=30)
	amount = models.IntegerField(max_length=30)
	submission_timestamp = models.DateField(max_length=30)
	duesdetails = models.CharField(max_length=30)
	status = models.CharField(max_length=30)
	paymentInfo = models.CharField(max_length=30)
	isApproved_staff = models.CharField(max_length=30, choices=isApproved_CHOICES)
	isApproved_warden = models.CharField(max_length=30, choices=isApproved_CHOICES)
	
class InventoryItem(models.Model):
	item_id = models.CharField(max_length=10)
	name = models.CharField(max_length=30)
	inventoryItem_type = models.CharField(max_length=30)
	no_total = models.IntegerField(max_length=30)
	no_issued = models.IntegerField(max_length=30)
	
class InventoryIssue(models.Model):
	item_id = models.ForeignKey(InventoryItem)
	issuer_id = models.CharField(max_length=20)
	issue_timestamp = models.DateField(max_length=10)
	issued_duration = models.DateField(max_length=10)
	
class Activity(models.Model):
	isApproved_CHOICES = (
		(0, u'Accepted'),
		(1, u'Rejected'),
		(2, u'Pending'),
	)
	name = models.CharField(max_length=20)
	description = models.CharField(max_length=20)
	start_dateTime = models.DateField(max_length=20)
	end_dateTime = models.DateField(max_length=20)
	is_Approved = models.IntegerField(max_length=20, choices=isApproved_CHOICES)
	
class Election(models.Model):
	isApproved_CHOICES = (
		(0, u'Accepted'),
		(1, u'Rejected'),
		(2, u'Pending'),
	)
	election_type = models.CharField(max_length=20)
	description = models.CharField(max_length=20)
	start_dateTime = models.DateField(max_length=20)
	end_dateTime = models.DateField(max_length=20)
	candidate_list = models.CharField(max_length=10)
	election_officer = models.CharField(max_length=20)
	is_Approved = models.IntegerField(max_length=20, choices=isApproved_CHOICES)
	
class Meeting(models.Model):
	isApproved_CHOICES = (
		(0, u'Accepted'),
		(1, u'Rejected'),
		(2, u'Pending'),
	)
	subject= models.CharField(max_length=20)
	description = models.CharField(max_length=20)
	start_dateTime = models.DateField(max_length=20)
	end_dateTime = models.DateField(max_length=20)
	called_by = models.CharField(max_length=10)
	meeting_invitees = models.CharField(max_length=10)
	is_Approved = models.IntegerField(max_length=20, choices=isApproved_CHOICES)
	
class MessMenu(models.Model):
	isApproved_CHOICES = (
		(0, u'Accepted'),
		(1, u'Rejected'),
		(2, u'Pending'),
	)
	menu = models.CharField(max_length=20)
	start_date = models.DateField(max_length=20)
	mess_timings = models.DateField(max_length=20)
	is_Approved = models.IntegerField(max_length=20, choices=isApproved_CHOICES)
	
class MessBill(models.Model):
	isApproved_CHOICES = (
		(0, u'Accepted'),
		(1, u'Rejected'),
		(2, u'Pending'),
	)
	basic_amount= models.IntegerField(max_length=20)
	start_dateTime = models.DateField(max_length=20)
	end_dateTime = models.DateField(max_length=20)
	is_Approved = models.IntegerField(max_length=20, choices=isApproved_CHOICES)
	
class Budget(models.Model):
	isApproved_CHOICES = (
		(0, u'Accepted'),
		(1, u'Rejected'),
		(2, u'Pending'),
	)
	total_amount= models.IntegerField(max_length=20)
	budget_type= models.CharField(max_length=20)
	description = models.CharField(max_length=20)
	start_dateTime = models.DateField(max_length=20)
	end_dateTime = models.DateField(max_length=20)
	is_Approved = models.IntegerField(max_length=20, choices=isApproved_CHOICES)
	
class PolicyInformation(models.Model):
	currently_active_policy = models.CharField(max_length=20)
	proposed_policy = models.CharField(max_length=20)
	policy_status = models.CharField(max_length=20)
	message = models.CharField(max_length=20)
	
class HallGuest(models.Model):
	guest_id = models.CharField(max_length=10)
	name = models.CharField(max_length=10)
	permanent_address = models.CharField(max_length=20)
	temp_IITK_address = models.CharField(max_length=10)
	contact_no  = models.IntegerField(max_length=10)
	email = models.CharField(max_length=10)
	staying_from = models.DateField(max_length=10)
	staying_till = models.DateField(max_length=10)
	
class Message(models.Model):
	isRead_CHOICES = (
		(0, u'Unread'),
		(1, u'Read'),
	)
	sender = models.CharField(max_length=10)
	receiver = models.CharField(max_length=10)
	subject = models.CharField(max_length=10)
	message = models.CharField(max_length=20)
	timestamp = models.DateField(max_length=10)
	isRead = models.IntegerField(max_length=10, choices=isRead_CHOICES)



	

# Create your models here.
