from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login,logout
from mainapp.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
url(r'^admin/', include(admin.site.urls)),
(r'^accounts/login/$', login),
(r'^accounts/logout/$', logout,{'template_name' : 'registration/logout.html'}),
(r'^accounts/profile/$', 'mainapp.views.profile'),
(r'^accounts/register/$','mainapp.views.register'),

(r'^student/viewComplaint/$','mainapp.views.view_complaints'),
(r'^student/addComplaint/$','mainapp.views.add_complaint'),

(r'^staff/viewComplaints/$','mainapp.staffViews.view_complaints'),
(r'^staff/actOnComplaint/id=(\d+)$','mainapp.staffViews.act_on_complaint'),
    
    (r'^$', direct_to_template, {'template': 'index.html'}, "home"),
    
    (r'^profile$','test_bootstrap.views.profile_form'),


    (r'^testurl$',direct_to_template,{'template':'contact.html'},"testurl"),
    
#    (r'^contact$', direct_to_template, {'template': 'contact.html'}, "contact"),
    (r'^form$', 'test_bootstrap.views.test_form'),
    (r'^form_template$', 'test_bootstrap.views.test_form_with_template'),
    (r'^form_inline$', 'test_bootstrap.views.test_form_inline'),
    (r'^tabs$', 'test_bootstrap.views.test_tabs', {}, "tabs"),
    (r'^widgets$', 'test_bootstrap.views.test_widgets', {}, "widgets"),
)

