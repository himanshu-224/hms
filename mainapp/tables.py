import django_tables2 as tables
from mainapp.models import *
from django_tables2.utils import A  # alias for Accessor
button="DELETE"

class inboxTable(tables.Table):
	id = tables.Column()
	button = tables.LinkColumn('delete_message',accessor='button', args=[A('pk')], verbose_name='',orderable=False)
	sender = tables.Column(verbose_name="Sender ID")
	receiverlist = tables.Column(verbose_name="SendTo List")
	subject = tables.LinkColumn('show_message',verbose_name="Subject",orderable=False,accessor='subject', args=[A('pk')])
	message = tables.Column(verbose_name="Message",orderable=False)
	timestamp = tables.Column(verbose_name="Date") ##NEED TO MODIFY TO TILL SECOND
	isRead = tables.Column(verbose_name="Status")
	class Meta:
		model = inboxMessage
		attrs = {"class": "paleblue"}
		exclude=("message","receiverlist")



class outboxTable(tables.Table):
	id = tables.Column()
	button = tables.LinkColumn('delete_message',accessor='button', args=[A('pk')], verbose_name='Delete')	
	sender = tables.Column(verbose_name="Sender ID")
	receiverlist = tables.Column(verbose_name="SendTo List")
	subject = tables.LinkColumn('show_message',verbose_name="Subject",orderable=False,accessor='subject', args=[A('pk')])
	message = tables.Column(verbose_name="Message",orderable=False)
	timestamp = tables.Column(verbose_name="Date") ##NEED TO MODIFY TO TILL SECOND

	class Meta:
		model = outboxMessage
		attrs = {"class": "paleblue"}
		exclude=("message","sender")
	
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


