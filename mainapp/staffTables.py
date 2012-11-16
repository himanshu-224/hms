import django_tables2 as tables
from mainapp.models import Complaint,DuesItem,MessBill
from django_tables2.utils import A  # alias for Accessor

class ComplaintTable(tables.Table):
	id = tables.LinkColumn('act_on_complaint_staff', args=[A('pk')])
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
		
class DuesTable1(tables.Table):
	id = tables.LinkColumn('act_on_dues_staff', args=[A('pk')])
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
	
class MessBillTable(tables.Table):
	id = tables.LinkColumn('act_on_messBill_staff', args=[A('pk')])
	Update = tables.LinkColumn('update_messbill',accessor='id', args=[A('pk')], verbose_name='Update')
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
		sequence=('id','payee_id','month','no_of_days','rebate_days','basic_amount','extra','total_bill','pay_messbill','submission_timestamp','details','paymentInfo','status','isVerified_staff',)
		attrs = {"class":"paleblue"}
		
		
