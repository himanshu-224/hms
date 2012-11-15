from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django_tables2   import RequestConfig
from django.template.context import RequestContext

from mainapp.studentTables import *
import datetime
from mainapp.models import *

def issued_status(request):
    if request.user.is_authenticated() and request.user.get_profile().userType==0:
        items=InventoryIssue.objects.filter(issuer_id=request.user)
        for item in items:
            itemType=item.item_id
            if item.isReturned == 'No':
                delta=datetime.date.today()-item.issue_timestamp
                item.issued_duration=delta.days
                if item.issued_duration > itemType.issued_for:
                    item.fine = itemType.fine_rate * (item.issued_duration - itemType.issued_for)
                item.save()

        table=InventoryIssueTable(items)
        RequestConfig(request).configure(table)
        return render(request, 'student/view_item.html', {'table': table})
    elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
            return HttpResponseRedirect('/accounts/profile')        