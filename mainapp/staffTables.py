import django_tables2 as tables
from mainapp.models import Complaint
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
