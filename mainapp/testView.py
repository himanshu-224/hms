from django.shortcuts import render
from django_tables2   import RequestConfig
from mainapp.models  import Complaint
from mainapp.staffTables  import ComplaintTable

def view_complaints(request):
	table = UserTable(Complaint.objects.all())
	RequestConfig(request).configure(table)
	return render(request, 'people.html', {'table': table})
