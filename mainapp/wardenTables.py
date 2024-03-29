import django_tables2 as tables
from mainapp.models import Complaint,DuesItem
from django_tables2.utils import A  # alias for Accessor

class ComplaintTable(tables.Table):
	id = tables.LinkColumn('act_on_complaint_warden', args=[A('pk')])
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
'''		
class DuesTable(tables.Table):
	id = tables.LinkColumn('act_on_dues_warden', args=[A('pk')])
	Delete = tables.LinkColumn('delete_dues',accessor='id', args=[A('pk')], verbose_name='Delete')
	duesdetails = tables.Column(orderable=False)
	status = tables.Column(verbose_name="Status Details",orderable=False)
	duesitem_type = tables.Column(verbose_name="Subject",orderable=False)
	payee_id = tables.Column(verbose_name="Payee ID")
	submission_timestamp = tables.Column(verbose_name="Date of Payment")
	isApproved_staff = tables.Column(verbose_name="Approved by staff")
	isApproved_warden = tables.Column(verbose_name="Approved by warden")
		
	class Meta:
		model = DuesItem
		sequence=('id','payee_id','duesitem_type','set_dues','pay_dues','submission_timestamp','duesdetails','paymentInfo','isApproved_staff','isApproved_warden','status',)
		attrs = {"class":"paleblue"}
		'''
