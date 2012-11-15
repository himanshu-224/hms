import django_tables2 as tables
from mainapp.models import Complaint,DuesItem

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
		sequence=('id','payee_id','duesitem_type','set_dues','pay_dues','submission_timestamp','duesdetails','paymentInfo','isApproved_staff','isApproved_warden','status',)
		attrs = {"class":"paleblue"}
		


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
