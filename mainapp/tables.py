import django_tables2 as tables
from mainapp.models import *
from django_tables2.utils import A  # alias for Accessor
button="DELETE"

class inboxTable(tables.Table):
	id = tables.Column()
	button = tables.LinkColumn('deleteInbox_message',accessor='button', args=[A('pk')], verbose_name='',orderable=False)
	sender = tables.Column(verbose_name="Sender ID")
	receiverlist = tables.Column(verbose_name="SendTo List")
	subject = tables.LinkColumn('showInbox_message',verbose_name="Subject",orderable=False,accessor='subject', args=[A('pk')])
	message = tables.Column(verbose_name="Message",orderable=False)
	timestamp = tables.Column(verbose_name="Date") ##NEED TO MODIFY TO TILL SECOND
	isRead = tables.Column(verbose_name="Status")
	class Meta:
		model = inboxMessage
		attrs = {"class": "paleblue"}
		exclude=("message","receiverlist","id")



class outboxTable(tables.Table):
	id = tables.Column()
	button = tables.LinkColumn('deleteOutbox_message',accessor='button', args=[A('pk')], verbose_name='Delete')	
	sender = tables.Column(verbose_name="Sender ID")
	receiverlist = tables.Column(verbose_name="SendTo List")
	subject = tables.LinkColumn('showOutbox_message',verbose_name="Subject",orderable=False,accessor='subject', args=[A('pk')])
	message = tables.Column(verbose_name="Message",orderable=False)
	timestamp = tables.Column(verbose_name="Date") ##NEED TO MODIFY TO TILL SECOND

	class Meta:
		model = outboxMessage
		attrs = {"class": "paleblue"}
		exclude=("message","sender","id")
	
class draftsTable(tables.Table):
	id = tables.Column()
	Delete = tables.LinkColumn('delete_message',accessor='id', args=[A('pk')], verbose_name='Delete')	
	sender = tables.Column(verbose_name="Sender ID")
	receiverlist = tables.Column(verbose_name="SendTo List")
	subject = tables.LinkColumn('show_message',verbose_name="Subject",orderable=False,accessor='id', args=[A('pk')])
	message = tables.Column(verbose_name="Message",orderable=False)
	timestamp = tables.Column(verbose_name="Date") ##NEED TO MODIFY TO TILL SECOND
	

	class Meta:
		model = draftMessage
		attrs = {"class": "paleblue"}
		exclude=("message","sender","id")

class candidateListTable(tables.Table):
	
	id = tables.Column()
	username = tables.Column(verbose_name = "Username")
	total_votes = tables.Column(verbose_name = "Total Votes")
	post = tables.Column(verbose_name = "Post")
	candidate_name = tables.Column(verbose_name = "Candidate Name")
	
	class Meta :
		model = candidateList
		attrs = {"class": "paleblue"}
		exclude=("candidate_name",)
