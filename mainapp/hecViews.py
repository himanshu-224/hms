from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.forms import UserCreationForm
from mainapp.models import Complaint
from mainapp.forms import ComplaintForm
from mainapp.models import Entry
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.forms.models import modelformset_factory

import time
import datetime

from datetime import date, timedelta
import calendar

mnames = "January February March April May June July August September October November December"
mnames = mnames.split()

def main(request, year=None):
    """Main listing, years and months; two years per page."""
    # prev / next years
    if request.user.is_authenticated() and request.user.get_profile().userType==1:
        if year: year = int(year)
        else:    year = time.localtime()[0]

        nowy, nowm = time.localtime()[:2]
        lst = []

    # create a list of months for each year, indicating ones that contain entries and current
        for y in [year, year + 1]:
            mlst = []
            for n, month in enumerate(mnames):
                entry = current = False   # are there entry(s) for this month; current month?
                entries = Entry.objects.filter(date__year=y, date__month=n+1)

                if entries:
                    entry = True
                if y == nowy and n+1 == nowm:
                    current = True
                mlst.append(dict(n=n+1, name=month, entry=entry, current=current))
            lst.append((y, mlst))

        return render_to_response("hec/calendar.html", dict(years=lst, user=request.user, year=year))


def month(request, year, month, change=None):
    if request.user.is_authenticated() and request.user.get_profile().userType==1:
        """Listing of days in `month`."""
        year, month = int(year), int(month)

    # apply next / previous change
        if change in ("next", "prev"):
            now, mdelta = date(year, month, 15), timedelta(days=31)
            if change == "next":   mod = mdelta
            elif change == "prev": mod = -mdelta

            year, month = (now+mod).timetuple()[:2]

    # init variables
        cal = calendar.Calendar()
        month_days = cal.itermonthdays(year, month)
        nyear, nmonth, nday = time.localtime()[:3]
        lst = [[]]
        week = 0

    # make month lists containing list of days for each week
    # each day tuple will contain list of entries and 'current' indicator
        for day in month_days:
            entries = current = False   # are there entries for this day; current day?
            if day:
                entries = Entry.objects.filter(date__year=year, date__month=month, date__day=day)
                if day == nday and year == nyear and month == nmonth:
                    current = True

            lst[week].append((day, entries, current))
            if len(lst[week]) == 7:
                lst.append([])
                week += 1

        return render_to_response("hec/month.html", dict(year=year, month=month, user=request.user,month_days=lst, mname=mnames[month-1]))




def day(request, year, month, day):
    if request.user.is_authenticated() and request.user.get_profile().userType==1:

        """Entries for the day."""
        EntriesFormset = modelformset_factory(Entry, extra=1, exclude=("creator", "date"),can_delete=True)

        if request.method == 'POST':
            formset = EntriesFormset(request.POST)
            if formset.is_valid():
               # add current user and date to each entry & save
                entries = formset.save(commit=False)
                for entry in entries:
                    entry.creator = request.user
                    entry.date = date(int(year), int(month), int(day))
                    entry.save()
                return HttpResponseRedirect(reverse("mainapp.hecViews.month", args=(year, month)))

        else:
        # display formset for existing enties and one extra form
            formset = EntriesFormset(queryset=Entry.objects.filter(date__year=year,
                date__month=month, date__day=day, creator=request.user))
        return render_to_response("hec/day.html", add_csrf(request, entries=formset, year=year,month=month, day=day))


def add_csrf(request, ** kwargs):
    if request.user.is_authenticated() and request.user.get_profile().userType==1:
        """Add CSRF and user to dictionary."""
        d = dict(user=request.user, ** kwargs)
        d.update(csrf(request))
        return d



from django_tables2   import RequestConfig

from mainapp.models import *
from mainapp.hecForms import *
from mainapp.hecTables import *
import datetime

def create_boudget(request) :
	return


def view_boudget(request) :
	return

def modify_boudget(request, id) :
	return
def create_mess_menu(request) :
	return

def modify_mess_menu(request, id) :
	return

def create_mess_bill(request) :
	return

def modify_mess_bill(request,id) :
	return

def arrange_meeting(request) :
	return

def modify_meeting(request, id) :
	return 
def add_item(request):
    if request.user.is_authenticated() and request.user.get_profile().userType==1:
            if request.method == 'POST':
                form = AddItemForm(request.POST)
                if form.is_valid():
                    at = form.cleaned_data['item_id']
                    ct = form.cleaned_data['name']
                    dt = form.cleaned_data['no_total']
                    et = form.cleaned_data['issued_for']
                    ft = form.cleaned_data['fine_rate']
                    data=InventoryItem(item_id=at,name=ct, no_total=dt,date_added=datetime.date.today(), fine_rate=ft, issued_for=et)
                    data.save()
                    return HttpResponseRedirect('/hec/home')
            else:
                form = AddItemForm()
            return render_to_response('hec/form_add_item.html', RequestContext(request, {
            'form': form,
            }))
    elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
            return HttpResponseRedirect('/accounts/profile')

def view_item(request):
    if request.user.is_authenticated() and request.user.get_profile().userType==1:
        table = InventoryItemTable(InventoryItem.objects.all())
        RequestConfig(request).configure(table)
        return render(request, 'hec/view_item.html', {'table': table})
    elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
            return HttpResponseRedirect('/accounts/profile')
            
         
def issue_item(request,id):
    if request.user.is_authenticated() and request.user.get_profile().userType==1:
            item=InventoryItem.objects.get(item_id=id)
            if item.no_total>item.no_issued:
                if request.method == 'POST':
                    form = IssueItemForm(request.POST)
                    if form.is_valid():
                        at = form.cleaned_data['issuer_id']
                        item.no_issued+=1
                        item.save()
                        data=InventoryIssue(issuer_id=at,item_id=item,issue_timestamp=datetime.date.today(), return_timestamp=datetime.date.today())
                        data.save()
                        return HttpResponseRedirect('/hec/viewItem')
                else:
                    form = IssueItemForm()
                return render_to_response('hec/form_add_item.html', RequestContext(request, {
                'form': form,
                }))
                
            else:
                message="Cannot Issue Item " +item.item_id +" as it is already issued"
                return render_to_response('hec/form_message.html', RequestContext(request,{'message':message }))
    elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
            return HttpResponseRedirect('/accounts/profile')    
            

def delete_item(request,id):
    if request.user.is_authenticated() and request.user.get_profile().userType==1:
        item=InventoryItem.objects.get(item_id=id)
        if item.no_issued==0:
            item.delete()
        else:
            message="Cannot Delete Item " +item.item_id +" as it is issued to someone."            
            return render_to_response('hec/form_message.html', RequestContext(request,{'message':message }))
        return HttpResponseRedirect('/hec/viewItem')

    elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
            return HttpResponseRedirect('/accounts/profile')            
            
            
def return_item(request,id):
    if request.user.is_authenticated() and request.user.get_profile().userType==1:
        item=InventoryIssue.objects.get(pk=id)
        itemType=item.item_id
        if item.isReturned == 'No':
            item.isReturned='Yes'
            item.return_timestamp=datetime.date.today()
            delta=item.return_timestamp-item.issue_timestamp
            item.issued_duration=delta.days;
            if item.issued_duration > itemType.issued_for:
                item.fine = itemType.fine_rate * (item.issued_duration - itemType.issued_for)
            item.save()
            itemType.no_issued-=1
            itemType.save()
        else:
            message="Cannot Return Item " +itemType.item_id +" issued by "+ item.issuer_id.username+" as it has already been returned."            
            return render_to_response('hec/form_message.html', RequestContext(request,{'message':message }))            
        return HttpResponseRedirect('/hec/issuedStatus/id='+itemType.item_id)

    elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
            return HttpResponseRedirect('/accounts/profile')              

def issued_status(request,id):
    if request.user.is_authenticated() and request.user.get_profile().userType==1:
        item=InventoryItem.objects.get(item_id=id)
        issuedItems=InventoryIssue.objects.filter(item_id=item)
        table=InventoryIssueTable(issuedItems)
        RequestConfig(request).configure(table)
        return render(request, 'hec/view_item.html', {'table': table})
    elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
            return HttpResponseRedirect('/accounts/profile')           
            
def delete_issueitem(request,id):
    if request.user.is_authenticated() and request.user.get_profile().userType==1:
        item=InventoryIssue.objects.get(pk=id)
        if item.isReturned=='Yes':
            item.delete()
        else:
            message="Cannot Delete Issue Record for " +item.item_id.item_id +" as the item has not been returned"
            return render_to_response('hec/form_message.html', RequestContext(request,{'message':message }))
        return HttpResponseRedirect('/hec/viewItem')

    elif not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
            return HttpResponseRedirect('/accounts/profile')   
