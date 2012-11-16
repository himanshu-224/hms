from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login,logout_then_login
from mainapp.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from mainapp.staffViews import createbill

userTypes={0:'student', 1:'hec',2:'staff',3:'warden', 4:'dosa', 5:'senate'}
admin.autodiscover()


urlpatterns = patterns('',
url(r'^admin/', include(admin.site.urls)),
(r'^accounts/login/$', login,{'template_name' : 'registration/login.html'}),
(r'^accounts/logout/$', logout_then_login, {'login_url': '/accounts/login'}),
(r'^accounts/profile/$', 'mainapp.views.profile'),
(r'^accounts/register/$','mainapp.views.register'),
(r'^accounts/updateInfo/$', 'mainapp.views.update_info'),


(r'^student/home/$','mainapp.views.homepage',{'template_name' : 'student/home.html'}),
(r'^student/viewComplaints/$','mainapp.views.view_complaints'),
(r'^student/addComplaint/$','mainapp.views.add_complaint'),
(r'^student/viewDues/$','mainapp.views.view_dues'),
url('^student/PayDues/id=(\d+)$', 'mainapp.views.pay_dues', name='pay_dues'),
(r'^student/viewPaidDues/$','mainapp.views.view_paid_dues'),

(r'^student/viewMessBill/$','mainapp.views.view_messbill'),
url('^student/PayMessBill/id=(\d+)$', 'mainapp.views.pay_messbill', name='pay_messbill'),
(r'^student/viewPaidMessBill/$','mainapp.views.view_paid_messbill'),


url('^student/deleteComplaint/id=(\d+)$', 'mainapp.views.delete_complaint', name='delete_complaint'),
(r'^student/inbox/$','mainapp.views.inbox'),
(r'^student/outbox/$','mainapp.views.outbox'),
(r'student/compose/$','mainapp.views.compose_message'),
url('^student/deleteMessage/id=(\d+)$', 'mainapp.views.delete_message', name='delete_message'),
url('^student/showMessage/id=(\d+)$', 'mainapp.views.show_message', name='show_message'),


url('^student/deleteInbox_message/id=(\d+)$', 'mainapp.views.deleteInbox_message', name='deleteInbox_message'),
url('^student/showInbox_message/id=(\d+)$', 'mainapp.views.showInbox_message', name='showInbox_message'),
url('^student/deleteOutbox_message/id=(\d+)$', 'mainapp.views.deleteOutbox_message', name='deleteOutbox_message'),
url('^student/showOutbox_message/id=(\d+)$', 'mainapp.views.showOutbox_message', name='showOutbox_message'),
(r'^student/issuedStatus/$','mainapp.studentViews.issued_status'),

(r'^staff/addDues/$','mainapp.staffViews.add_Dues'),
(r'^staff/viewDues/$','mainapp.staffViews.view_Dues'),
url('^staff/deleteDues/id=(\d+)$', 'mainapp.staffViews.delete_dues', name='delete_dues'),
url('^staff/actOnDues/id=(\d+)$', 'mainapp.staffViews.act_on_dues', name='act_on_dues_staff'),

(r'^staff/home/$','mainapp.views.homepage',{'template_name' : 'staff/home.html'}),
(r'^staff/home/$','mainapp.views.profile',{'template_name' : 'staff/home.html'}),
(r'^staff/viewComplaints/$','mainapp.staffViews.view_complaints'),
url('^staff/actOnComplaint/id=(\d+)$', 'mainapp.staffViews.act_on_complaint', name='act_on_complaint_staff'),
(r'^staff/inbox/$','mainapp.views.inbox'),
(r'^staff/outbox/$','mainapp.views.outbox'),
(r'staff/compose/$','mainapp.views.compose_message'),
<<<<<<< HEAD
url('^staff/deleteMessage/id=(\d+)$', 'mainapp.views.delete_message', name='delete_message'),
url('^staff/showMessage/id=(\d+)$', 'mainapp.views.show_message', name='show_message'),
(r'^staff/addMessBill/$',createbill),
(r'^staff/viewMessBill/$','mainapp.staffViews.view_MessBill'),
url('^staff/UpdateMessBill/id=(\d+)$', 'mainapp.staffViews.update_messbill', name='update_messbill'),
url('^staff/actOnMessBill/id=(\d+)$', 'mainapp.staffViews.act_on_messBill', name='act_on_messBill_staff'),
=======
url('^staff/deletezinbox_message/id=(\d+)$', 'mainapp.views.deleteInbox_message', name='deleteInbox_message'),
url('^staff/showInbox_message/id=(\d+)$', 'mainapp.views.showInbox_message', name='showInbox_message'),
url('^staff/deleteOutbox_message/id=(\d+)$', 'mainapp.views.deleteOutbox_message', name='deleteOutbox_message'),
url('^staff/showOutbox_message/id=(\d+)$', 'mainapp.views.showOutbox_message', name='showOutbox_message'),
>>>>>>> b13aca3383b79e53abebb0e44e510d7752ce02f6



(r'^warden/home/$','mainapp.views.homepage',{'template_name' : 'warden/home.html'}),
(r'^warden/viewComplaints/$','mainapp.wardenViews.view_complaints'),
url('^warden/actOnComplaint/id=(\d+)$', 'mainapp.wardenViews.act_on_complaint', name='act_on_complaint_warden'),
(r'^warden/inbox/$','mainapp.views.inbox'),
(r'^warden/outbox/$','mainapp.views.outbox'),
(r'warden/compose/$','mainapp.views.compose_message'),
url('^warden/election/$', 'mainapp.wardenViews.conduct_election', name='conduct_election'),
url('^warden/addCandidate/$', 'mainapp.wardenViews.add_candidate', name='add_candidate'),
url('^warden/deleteInbox_message/id=(\d+)$', 'mainapp.views.deleteInbox_message', name='deleteInbox_message'),
url('^warden/showInbox_message/id=(\d+)$', 'mainapp.views.showInbox_message', name='showInbox_message'),
url('^warden/deleteOutbox_message/id=(\d+)$', 'mainapp.views.deleteOutbox_message', name='deleteOutbox_message'),
url('^warden/showOutbox_message/id=(\d+)$', 'mainapp.views.showOutbox_message', name='showOutbox_message'),


(r'^hec/home/$','mainapp.views.homepage',{'template_name' : 'hec/home.html'}),

url('^hec/addItem/$', 'mainapp.hecViews.add_item'),
url('^hec/viewItem/$', 'mainapp.hecViews.view_item'),
url('^hec/issueItem/id=(.+)$', 'mainapp.hecViews.issue_item', name='issue_item'),
url('^hec/deleteItem/id=(.+)$', 'mainapp.hecViews.delete_item', name='delete_item'),
url('^hec/returnItem/id=(\d+)$', 'mainapp.hecViews.return_item', name='return_item'),
url('^hec/issuedStatus/id=(.+)$', 'mainapp.hecViews.issued_status', name='issued_status'),
url('^hec/deleteIssueItem/id=(.+)$', 'mainapp.hecViews.delete_issueitem', name='delete_issueitem'),
(r'^hec/home/$','mainapp.views.homepage',{'template_name' : 'hec/home.html'}),


(r'^hec/inbox/$','mainapp.views.inbox'),
(r'^hec/outbox/$','mainapp.views.outbox'),
(r'hec/compose/$','mainapp.views.compose_message'),
url('^hec/deleteInbox_message/id=(\d+)$', 'mainapp.views.deleteInbox_message', name='deleteInbox_message'),
url('^hec/showInbox_message/id=(\d+)$', 'mainapp.views.showInbox_message', name='showInbox_message'),
url('^hec/deleteOutbox_message/id=(\d+)$', 'mainapp.views.deleteOutbox_message', name='deleteOutbox_message'),
url('^hec/showOutbox_message/id=(\d+)$', 'mainapp.views.showOutbox_message', name='showOutbox_message'),

(r'^dosa/home/$','mainapp.views.homepage',{'template_name' : 'dosa/home.html'}),
(r'^dosa/inbox/$','mainapp.views.inbox'),
(r'^dosa/outbox/$','mainapp.views.outbox'),
(r'dosa/compose/$','mainapp.views.compose_message'),
url('^dosa/deleteInbox_message/id=(\d+)$', 'mainapp.views.deleteInbox_message', name='deleteInbox_message'),
url('^dosa/showInbox_message/id=(\d+)$', 'mainapp.views.showInbox_message', name='showInbox_message'),
url('^dosa/deleteOutbox_message/id=(\d+)$', 'mainapp.views.deleteOutbox_message', name='deleteOutbox_message'),
url('^dosa/showOutbox_message/id=(\d+)$', 'mainapp.views.showOutbox_message', name='showOutbox_message'),

(r'^senate/home/$','mainapp.views.homepage',{'template_name' : 'senate/home.html'}),
(r'^senate/inbox/$','mainapp.views.inbox'),
(r'^senate/outbox/$','mainapp.views.outbox'),
(r'senate/compose/$','mainapp.views.compose_message'),
url('^senate/deleteInbox_message/id=(\d+)$', 'mainapp.views.deleteInbox_message', name='deleteInbox_message'),
url('^senate/showInbox_message/id=(\d+)$', 'mainapp.views.showInbox_message', name='showInbox_message'),
url('^senate/deleteOutbox_message/id=(\d+)$', 'mainapp.views.deleteOutbox_message', name='deleteOutbox_message'),
url('^senate/showOutbox_message/id=(\d+)$', 'mainapp.views.showOutbox_message', name='showOutbox_message'), 
 (r'^$', direct_to_template, {'template': 'index.html'}, "home"),)


url1=(url('^hec/viewPolicies/$', 'mainapp.hecViews.view_policies', name = 'view_policies'), 
url('^hec/createBudget/$', 'mainapp.hecViews.create_budget'),
url('^hec/modifyBudget/id=(\d+)$', 'mainapp.hecViews.view_boudget'),
url('^hec/createMessMenu/$', 'mainapp.hecViews.create_mess_menu'),
url('^hec/modifyMessMenu/id=(\d+)$', 'mainapp.hecViews.modify_mess_menu'),
url('^hec/createMessBill/$', 'mainapp.hecViews.create_mess_bill'),
url('^hec/modifyMessBill/id=(\d+)$', 'mainapp.hecViews.modify_mess_bill'),
url('^hec/arrangeMeeting/$', 'mainapp.hecViews.arrange_meeting'),
url('^hec/modifyMeeting/id=(\d+)$', 'mainapp.hecViews.modify_meeting'),
)
