import django_tables2 as tables
from mainapp.models import *
from django_tables2.utils import A  # alias for Accessor

class InventoryItemTable(tables.Table):
    
    Issue = tables.LinkColumn('issue_item', args=[A('pk')])
    Delete = tables.LinkColumn('delete_item', args=[A('pk')])
    item_id = tables.LinkColumn('issued_status',args=[A('pk')],verbose_name="Item Id")
    name = tables.Column(verbose_name="Name")
    no_total=tables.Column(verbose_name="Total No")
    no_issued=tables.Column(verbose_name="Issued No")
    date_added = tables.Column(verbose_name="Date Added")
    issued_for=tables.Column(verbose_name="Days Allowed")
    fine_rate=tables.Column(verbose_name="Fine per day")
    
    class Meta:
        model = InventoryItem
        attrs = {"class": "paleblue"}    


class InventoryIssueTable(tables.Table):
    
    Return = tables.LinkColumn('return_item', args=[A('pk')])
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
        