from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login,logout_then_login
from mainapp.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
url(r'^admin/', include(admin.site.urls)),
(r'^accounts/login/$', login,{'template_name' : 'registration/login.html'}),
(r'^accounts/logout/$', logout_then_login, {'login_url': '/accounts/login'}),
(r'^accounts/profile/$', 'mainapp.views.profile'),
(r'^accounts/register/$','mainapp.views.register'),

(r'^student/home/$','mainapp.views.homepage',{'template_name' : 'student/home.html'}),
(r'^student/viewComplaints/$','mainapp.views.view_complaints'),
(r'^student/addComplaint/$','mainapp.views.add_complaint'),
url('^student/deleteComplaint/id=(\d+)$', 'mainapp.views.delete_complaint', name='delete_complaint'),

(r'^staff/home/$','mainapp.views.homepage',{'template_name' : 'staff/home.html'}),
(r'^staff/home/$','mainapp.views.profile',{'template_name' : 'staff/home.html'}),
(r'^staff/viewComplaints/$','mainapp.staffViews.view_complaints'),
url('^staff/actOnComplaint/id=(\d+)$', 'mainapp.staffViews.act_on_complaint', name='act_on_complaint_staff'),

(r'^warden/home/$','mainapp.views.homepage',{'template_name' : 'warden/home.html'}),
(r'^warden/viewComplaints/$','mainapp.wardenViews.view_complaints'),
url('^warden/actOnComplaint/id=(\d+)$', 'mainapp.wardenViews.act_on_complaint', name='act_on_complaint_warden'),

(r'^hec/home/$','mainapp.views.homepage',{'template_name' : 'hec/home.html'}),

(r'^dosa/home/$','mainapp.views.homepage',{'template_name' : 'dosa/home.html'}),

(r'^senate/home/$','mainapp.views.homepage',{'template_name' : 'senate/home.html'}),
 
    (r'^$', direct_to_template, {'template': 'index.html'}, "home"),
)


