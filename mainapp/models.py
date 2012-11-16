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
		('Accepted', u'Accepted'),
		('Rejected', u'Rejected'),
		('Pending', u'Pending'),
	)
	requester_id = models.CharField(max_length=30)
	addressedto_id = models.CharField(max_length=30)
	forwardto_id = models.CharField(max_length=30,default='')
	request_timestamp = models.DateField(max_length=30)
	request_type = models.CharField(max_length=30)
	details = models.CharField(max_length=500)
	status = models.CharField(max_length=200,default='')
	reason = models.CharField(max_length=200,default='')
	isAccepted = models.CharField(max_length=10, choices=isAccepted_CHOICES,default='Pending')

class Complaint(models.Model):
	isAccepted_CHOICES = (
		('Accepted', u'Accepted'),
		('Rejected', u'Rejected'),
		('Pending', u'Pending'),
	)
	complainee_id = models.CharField(max_length=30)
	addressedto_id = models.CharField(max_length=30)
	forwardto_id = models.CharField(max_length=30,default='')
	complaint_timestamp = models.DateField(max_length=30)
	complaint_type = models.CharField(max_length=30)
	details = models.CharField(max_length=500)
	status = models.CharField(max_length=200,default='')
	reason = models.CharField(max_length=200,default='')
	isAccepted = models.CharField(max_length=10, choices=isAccepted_CHOICES,default='Pending')
	
class DuesItem(models.Model):
	isApproved_CHOICES = (
		('Accepted', u'Accepted'),
		('Rejected', u'Rejected'),
		('Pending', u'Pending'),
	)
	payee_id = models.CharField(max_length=30)
	duesitem_type = models.CharField(max_length=30)
	amount = models.IntegerField(max_length=30)
	submission_timestamp = models.DateField(max_length=30)
	duesdetails = models.CharField(max_length=500,default='')
	status = models.CharField(max_length=200,default='')
	paymentInfo = models.CharField(max_length=30)
	isApproved_staff = models.CharField(max_length=10, choices=isApproved_CHOICES,default='Pending')
	isApproved_warden = models.CharField(max_length=10, choices=isApproved_CHOICES,default='Pending')
	
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
	
class Policy(models.Model):
    statement = models.CharField(max_length = 1000)
    proposal = models.CharField(max_length = 1000, blank = True)
    STATUS = (
    (u'APP', u'Approved'),
    (u'PFC', u'Proposed for change'),
    (u'NPR', u'New Proposal'),
    (u'PFD', u'Proposed for deletion'),
    )
    status = models.CharField(max_length = 10, choices = STATUS)
    SEND_REQ_TO = (
    (u'DS', u'Dosa'),
    (u'SS', u'Student Senate'),
    )
    requestedTo = models.CharField(max_length = 10, choices = SEND_REQ_TO, blank = True)
    message = models.CharField(max_length = 500, blank = True) #not used

    def getStatement(self):
        return self.statement
    
    def setStatement(self, stmt):
        self.statement = stmt
        self.save()

    def getProposal(self):
        return self.proposal

    def setProposal(self, stmt):
        self.proposal = stmt
        self.save()

    def getStatus(self):
        return self.status

    def setStatus(self, stat):
        self.status = stat
        self.save()

    def getReqTo(self):
        return self.status

    def setReqTo(self, reqTo):
        self.status = reqTo
        self.save()

    def getMessage(self):
        return self.message

    def setMessage(self, msg):
        self.message = msg
        self.save()

    def getId(self):
        return self.id

    def delPolicy(self):
        self.delete()
	
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

class Entry(models.Model):
    title = models.CharField(max_length=40)
    snippet = models.CharField(max_length=150, blank=True)
    body = models.TextField(max_length=10000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateField(blank=True)
    creator = models.ForeignKey(User, blank=True, null=True)
#    remind = models.BooleanField(default=False)#not implemented

    def __unicode__(self):
        if self.title:
            return unicode(self.creator) + u" - " + self.title
        else:
            return unicode(self.creator) + u" - " + self.snippet[:40]

    def short(self):
        if self.snippet:
            return "<i>%s</i> - %s" % (self.title, self.snippet)
        else:
            return self.title
    short.allow_tags = True

    class Meta:
        verbose_name_plural = "entries"


### Admin

#class EntryAdmin(admin.ModelAdmin):
 #   list_display = ["creator", "date", "title", "snippet"]
  #  list_filter = ["creator"]

#admin.site.register(Entry, EntryAdmin)



