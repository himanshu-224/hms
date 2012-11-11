import django_tables2 as tables
from mainapp.models import Complaint
from django_tables2.utils import A  # alias for Accessor

class ComplaintTable(tables.Table):
	id = tables.Column()
	Edit = tables.LinkColumn( 'act_on_complaint_dosa', accessor='id',args=[A('pk')], verbose_name='Edit')
	details = tables.Column(orderable=False)
	status = tables.Column(verbose_name="Status Details",orderable=False)
	reason = tables.Column(orderable=False)
	complaint_type = tables.Column(verbose_name="Subject",orderable=False)
	addressedto_id = tables.Column(verbose_name = "Addressed To")
	complainee_id = tables.Column(verbose_name="Complainee ID")
	complaint_timestamp = tables.Column(verbose_name="Date of Complaint")
	isAccepted=tables.Column(verbose_name="Status")

	class Meta:
		model = Complaint
		exclude=("forwardto_id",)
		attrs = {"class": "paleblue"}
