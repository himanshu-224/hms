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
url('^student/viewPolicies/$', 'mainapp.views.view_policies', name = 'view_policies'), 

(r'^staff/home/$','mainapp.views.homepage',{'template_name' : 'staff/home.html'}),
(r'^staff/home/$','mainapp.views.profile',{'template_name' : 'staff/home.html'}),
(r'^staff/viewComplaints/$','mainapp.staffViews.view_complaints'),
url('^staff/actOnComplaint/id=(\d+)$', 'mainapp.staffViews.act_on_complaint', name='act_on_complaint_staff'),
url('^staff/viewPolicies/$', 'mainapp.views.view_policies', name = 'view_policies'), 

(r'^warden/home/$','mainapp.views.homepage',{'template_name' : 'warden/home.html'}),
(r'^warden/viewComplaints/$','mainapp.wardenViews.view_complaints'),
url('^warden/actOnComplaint/id=(\d+)$', 'mainapp.wardenViews.act_on_complaint', name='act_on_complaint_warden'),
url('^warden/viewPolicies/$', 'mainapp.views.view_policies', name = 'view_policies'), 



(r'^hec/home/$','mainapp.views.homepage',{'template_name' : 'hec/home.html'}),
url('^hec/viewPolicies/$', 'mainapp.views.view_policies', name = 'view_policies'), 
url(r"^hec/main/(\d+)/$", "mainapp.hecViews.main"),
url(r"^hec/main/$", "mainapp.hecViews.main"),
url(r"^hec/month/(\d+)/(\d+)/(prev|next)/$", "mainapp.hecViews.month"),
url(r"^hec/month/(\d+)/(\d+)/$", "mainapp.hecViews.month"),
url(r"^hec/month$", "mainapp.hecViews.month"),
url(r"^hec/day/(\d+)/(\d+)/(\d+)/$", "mainapp.hecViews.day"),

(r'^dosa/home/$','mainapp.views.homepage',{'template_name' : 'dosa/home.html'}),
(r'^dosa/viewComplaints/$','mainapp.dosaViews.view_complaints'),
url('^dosa/actOnComplaint/id=(\d+)$', 'mainapp.dosaViews.act_on_complaint', name='act_on_complaint_dosa'),
url(r'^dosa/viewPolicies/$', 'mainapp.views.view_policies', name = 'view_policies'),
url(r'^dosa/pendingRequests/$', 'mainapp.dosaViews.pending_requests', name = 'pending_requests'),
url(r'^dosa/acceptRequest/(?P<pid>\d+)/$', 'mainapp.dosaViews.accept_request', name = 'accept_request'),
url(r'^dosa/rejectRequest/(?P<pid>\d+)/$', 'mainapp.dosaViews.reject_request', name = 'reject_request'),
url(r'^dosa/deleteRequest/(?P<pid>\d+)/$', 'mainapp.dosaViews.delete_request', name = 'delete_request'),
url(r'^dosa/changeRequest/(?P<pid>\d+)/$', 'mainapp.dosaViews.change_request', name = 'change_request'),
url(r'^dosa/submitChangeRequest/(?P<pid>\d+)/$', 'mainapp.dosaViews.submit_change_request', name = 'submit_change_request'),
url(r'^dosa/createPolicy/$', 'mainapp.dosaViews.create_policy', name = 'create_policy'),
url(r'^dosa/deletePolicy/$', 'mainapp.dosaViews.delete_policy', name = 'delete_policy'),
url(r'^dosa/submitPolicy/(?P<req>\w+)/$', 'mainapp.dosaViews.submit_policy', name = 'submit_policy'),
url(r'^dosa/changePolicy/$', 'mainapp.dosaViews.change_policy', name = 'change_policy'),
url(r'^dosa/deleteProposal/(?P<pid>\d+)/$', 'mainapp.dosaViews.delete_proposal', name = 'delete_proposal'),

(r'^senate/home/$','mainapp.views.homepage',{'template_name' : 'senate/home.html'}),
url('^senate/viewPolicies/$', 'mainapp.views.view_policies', name = 'view_policies'), 
url(r'^senate/pendingRequests/$', 'mainapp.senateViews.pending_requests', name = 'pending_requests'),
url(r'^senate/acceptRequest/(?P<pid>\d+)/$', 'mainapp.senateViews.accept_request', name = 'accept_request'),
url(r'^senate/rejectRequest/(?P<pid>\d+)/$', 'mainapp.senateViews.reject_request', name = 'reject_request'),
url(r'^senate/deleteRequest/(?P<pid>\d+)/$', 'mainapp.senateViews.delete_request', name = 'delete_request'),
url(r'^senate/changeRequest/(?P<pid>\d+)/$', 'mainapp.senateViews.change_request', name = 'change_request'),
url(r'^senate/submitChangeRequest/(?P<pid>\d+)/$', 'mainapp.senateViews.submit_change_request', name = 'submit_change_request'),
url(r'^senate/createPolicy/$', 'mainapp.senateViews.create_policy', name = 'create_policy'),
url(r'^senate/deletePolicy/$', 'mainapp.senateViews.delete_policy', name = 'delete_policy'),
url(r'^senate/submitPolicy/(?P<req>\w+)/$', 'mainapp.senateViews.submit_policy', name = 'submit_policy'),
url(r'^senate/changePolicy/$', 'mainapp.senateViews.change_policy', name = 'change_policy'),
url(r'^senate/deleteProposal/(?P<pid>\d+)/$', 'mainapp.senateViews.delete_proposal', name = 'delete_proposal'),

 
    (r'^$', direct_to_template, {'template': 'index.html'}, "home"),
)


