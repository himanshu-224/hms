import django_tables2 as tables
<<<<<<< HEAD
from mainapp.models import Complaint,DuesItem,MessBill
=======
from mainapp.models import Complaint,DuesItem

>>>>>>> b13aca3383b79e53abebb0e44e510d7752ce02f6
from django_tables2.utils import A  # alias for Accessor
from mainapp.models import *

class ComplaintTable(tables.Table):
	id = tables.Column()
	Delete = tables.LinkColumn('delete_complaint',accessor='id', args=[A('pk')], verbose_name='Delete')
	details = tables.Column(orderable=False)
	status = tables.Column(verbose_name="Status Details",orderable=False)
	reason = tables.Column(orderable=False)
	complaint_type = tables.Column(verbose_name="Subject",orderable=False)
	addressedto_id = tables.Column(verbose_name = "Addressed To")
	complainee_id = tables.Column(verbose_name="Complainee ID")
	forwardto_id = tables.Column(verbose_name="Forwarded To")
	complaint_timestamp = tables.Column(verbose_name="Date of Complaint")
	isAccepted=tables.Column(verbose_name="Status")

	class Meta:
		model = Complaint
		attrs = {"class": "paleblue"}

		
class DuesTable(tables.Table):
	id = tables.Column()
	duesdetails = tables.Column(orderable=False)
	status = tables.Column(verbose_name="Status Details",orderable=False)
	duesitem_type = tables.Column(verbose_name="Subject",orderable=False)
	payee_id = tables.Column(verbose_name="Payee ID")
	set_dues = tables.Column(verbose_name="Dues")
	submission_timestamp = tables.Column(verbose_name="Date of Payment")
	isApproved_staff = tables.Column(verbose_name="Approved by staff")
	isApproved_warden = tables.Column(verbose_name="Approved by warden")
		
	class Meta:
		model = DuesItem
		sequence=('id','payee_id','duesitem_type','set_dues','pay_dues','submission_timestamp','duesdetails','paymentInfo','isApproved_staff','isApproved_warden','status',)
		attrs = {"class":"paleblue"}
		
<<<<<<< HEAD
class DuesTable1(tables.Table):
	id = tables.Column()
	pay = tables.LinkColumn('pay_dues',accessor='id', args=[A('pk')], verbose_name='Pay')
	duesdetails = tables.Column(orderable=False)
	status = tables.Column(verbose_name="Status Details",orderable=False)
	duesitem_type = tables.Column(verbose_name="Subject",orderable=False)
	payee_id = tables.Column(verbose_name="Payee ID")
	set_dues = tables.Column(verbose_name="Dues")
	submission_timestamp = tables.Column(verbose_name="Date of Payment")
	isApproved_staff = tables.Column(verbose_name="Approved by staff")
	isApproved_warden = tables.Column(verbose_name="Approved by warden")
		
	class Meta:
		model = DuesItem
		exclude=('status','isApproved_staff','isApproved_warden','submitted','submission_timestamp','paymentInfo',)
		sequence=('id','payee_id','duesitem_type','set_dues','pay_dues','duesdetails',)
		attrs = {"class":"paleblue"}
		
class MessBillTable(tables.Table):
	id = tables.Column()
	details = tables.Column(orderable=False)
	status = tables.Column(verbose_name="Status Details",orderable=False)
	payee_id = tables.Column(verbose_name="Payee ID")
	no_of_days=tables.Column(verbose_name ="No. Of Days")
	rebate_days = tables.Column(verbose_name ="Rebate Days")
	basic_amount = tables.Column(verbose_name ="Basic Amount")
	extra= tables.Column(verbose_name ="Extra Cost")
	month = tables.Column(verbose_name ="Month")
	submission_timestamp = tables.Column(verbose_name="Date of Payment")
	isVerified_staff = tables.Column(verbose_name="Verified by staff")
	
	class Meta:
		model = MessBill
		sequence=('id','payee_id','month','no_of_days','rebate_days','basic_amount','extra','total_bill','pay_messbill','paymentInfo','details','status','isVerified_staff',)
		attrs = {"class":"paleblue"}
	
class MessBillTable1(tables.Table):
	id = tables.Column()
	pay_messbill = tables.LinkColumn('pay_messbill',accessor='id', args=[A('pk')], verbose_name='Pay')
	details = tables.Column(orderable=False)
	status = tables.Column(verbose_name="Status Details",orderable=False)
	payee_id = tables.Column(verbose_name="Payee ID")
	no_of_days=tables.Column(verbose_name ="No. Of Days")
	rebate_days = tables.Column(verbose_name ="Rebate Days")
	basic_amount = tables.Column(verbose_name ="Basic Amount")
	extra= tables.Column(verbose_name ="Extra Cost")
	month = tables.Column(verbose_name ="Month")
	submission_timestamp = tables.Column(verbose_name="Date of Payment")
	isVerified_staff = tables.Column(verbose_name="Verified by staff")
	
	class Meta:
		model = MessBill
		exclude=('status','isVerified_staff','submission_timestamp','submitted','paymentInfo',)
		sequence=('id','payee_id','month','no_of_days','rebate_days','basic_amount','extra','total_bill','details',)
		attrs = {"class":"paleblue"}
		
=======


class InventoryIssueTable(tables.Table):
    
    item_id = tables.Column(verbose_name="Item Id")
    issuer_id = tables.Column(verbose_name="Issuer Id")
    issue_timestamp = tables.Column(verbose_name="Issued on")
    return_timestamp = tables.Column(verbose_name="Returned on")
    issued_duration=tables.Column(verbose_name="No of days")
    isReturned = tables.Column(verbose_name="Is Returned")
    fine=tables.Column(verbose_name="Fine")
    
    class Meta:
        model = InventoryIssue
        attrs = {"class": "paleblue"}  
        exclude=('Delete','Return')
>>>>>>> b13aca3383b79e53abebb0e44e510d7752ce02f6
