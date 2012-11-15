from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login,logout_then_login
from mainapp.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

userTypes={0:'student', 1:'hec',2:'staff',3:'warden', 4:'dosa', 5:'senate'}
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
(r'^student/inbox/$','mainapp.views.inbox'),
(r'^student/outbox/$','mainapp.views.outbox'),
(r'student/compose/$','mainapp.views.compose_message'),
url('^student/deleteMessage/id=(\d+)$', 'mainapp.views.delete_message', name='delete_message'),
url('^student/showMessage/id=(\d+)$', 'mainapp.views.show_message', name='show_message'),





(r'^staff/home/$','mainapp.views.homepage',{'template_name' : 'staff/home.html'}),
(r'^staff/home/$','mainapp.views.profile',{'template_name' : 'staff/home.html'}),
(r'^staff/viewComplaints/$','mainapp.staffViews.view_complaints'),
url('^staff/actOnComplaint/id=(\d+)$', 'mainapp.staffViews.act_on_complaint', name='act_on_complaint_staff'),
(r'^staff/inbox/$','mainapp.views.inbox'),
(r'^staff/outbox/$','mainapp.views.outbox'),
(r'staff/compose/$','mainapp.views.compose_message'),
url('^staff/deleteMessage/id=(\d+)$', 'mainapp.views.delete_message', name='delete_message'),
url('^staff/showMessage/id=(\d+)$', 'mainapp.views.show_message', name='show_message'),



(r'^warden/home/$','mainapp.views.homepage',{'template_name' : 'warden/home.html'}),
(r'^warden/viewComplaints/$','mainapp.wardenViews.view_complaints'),
url('^warden/actOnComplaint/id=(\d+)$', 'mainapp.wardenViews.act_on_complaint', name='act_on_complaint_warden'),
(r'^warden/inbox/$','mainapp.views.inbox'),
(r'^warden/outbox/$','mainapp.views.outbox'),
(r'warden/compose/$','mainapp.views.compose_message'),
url('^warden/deleteMessage/id=(\d+)$', 'mainapp.views.delete_message', name='delete_message'),
url('^warden/showMessage/id=(\d+)$', 'mainapp.views.show_message', name='show_message'),

(r'^hec/home/$','mainapp.views.homepage',{'template_name' : 'hec/home.html'}),

url('^hec/addItem/$', 'mainapp.hecViews.add_item'),
url('^hec/viewItem/$', 'mainapp.hecViews.view_item'),
url('^hec/issueItem/id=(\d+)$', 'mainapp.hecViews.issue_item', name='issue_item'),
url('^hec/deleteItem/id=(\d+)$', 'mainapp.hecViews.delete_item', name='delete_item'),
url('^hec/returnItem/$', 'mainapp.hecViews.return_item'),

(r'^hec/inbox/$','mainapp.views.inbox'),
(r'^hec/outbox/$','mainapp.views.outbox'),
(r'hec/compose/$','mainapp.views.compose_message'),
url('^hec/deleteMessage/id=(\d+)$', 'mainapp.views.delete_message', name='delete_message'),
url('^hec/showMessage/id=(\d+)$', 'mainapp.views.show_message', name='show_message'),

(r'^dosa/home/$','mainapp.views.homepage',{'template_name' : 'dosa/home.html'}),
(r'^dosa/inbox/$','mainapp.views.inbox'),
(r'^dosa/outbox/$','mainapp.views.outbox'),
(r'dosa/compose/$','mainapp.views.compose_message'),
url('^dosa/deleteMessage/id=(\d+)$', 'mainapp.views.delete_message', name='delete_message'),
url('^dosa/showMessage/id=(\d+)$', 'mainapp.views.show_message', name='show_message'),

(r'^senate/home/$','mainapp.views.homepage',{'template_name' : 'senate/home.html'}),
(r'^senate/inbox/$','mainapp.views.inbox'),
(r'^senate/outbox/$','mainapp.views.outbox'),
(r'senate/compose/$','mainapp.views.compose_message'),
url('^senate/deleteMessage/id=(\d+)$', 'mainapp.views.delete_message', name='delete_message'),
url('^senate/showMessage/id=(\d+)$', 'mainapp.views.show_message', name='show_message'),
 
    (r'^$', direct_to_template, {'template': 'index.html'}, "home"),
)


url1=(url('^hec/viewPolicies/$', 'mainapp.hecViews.view_policies', name = 'view_policies'), 
url('^hec/createBudget/$', 'mainapp.hecViews.create_budget'),
url('^hec/modifyBudget/id=(\d+)$', 'mainapp.hecViews.view_boudget'),
url('^hec/createMessMenu/$', 'mainapp.hecViews.create_mess_menu'),
url('^hec/modifyMessMenu/id=(\d+)$', 'mainapp.hecViews.modify_mess_menu'),
url('^hec/createMessBill/$', 'mainapp.hecViews.create_mess_bill'),
url('^hec/modifyMessBill/id=(\d+)$', 'mainapp.hecViews.modify_mess_bill'),
url('^hec/arrangeMeeting/$', 'mainapp.hecViews.arrange_meeting'),
url('^hec/modifyMeeting/id=(\d+)$', 'mainapp.hecViews.modify_meeting'),)
