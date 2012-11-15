from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.forms import UserCreationForm
from mainapp.models import Complaint
from mainapp.forms import ComplaintForm

import datetime


