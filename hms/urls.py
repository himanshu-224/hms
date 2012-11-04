from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from mainapp.views import profile, register, view_complaints_student, complain_form
from mainapp.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',(r'^accounts/login/$', login),
(r'^accounts/logout/$', logout,{'template_name' : 'registration/logout.html'}),
(r'^accounts/profile/$', profile),
(r'^accounts/register/$',register),
(r'^student/viewComplaint/$',view_complaints_student),
    # Examples:
    # url(r'^$', 'hms.views.home', name='home'),
    # url(r'^hms/', include('hms.foo.urls')),

    #Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^$', direct_to_template, {'template': 'index.html'}, "home"),
    
    (r'^profile$','test_bootstrap.views.profile_form'),

	(r'^student/addComplaint$','mainapp.views.complain_form'),
 
    (r'^testurl$',direct_to_template,{'template':'contact.html'},"testurl"),
    
#    (r'^contact$', direct_to_template, {'template': 'contact.html'}, "contact"),
    (r'^form$', 'test_bootstrap.views.test_form'),
    (r'^form_template$', 'test_bootstrap.views.test_form_with_template'),
    (r'^form_inline$', 'test_bootstrap.views.test_form_inline'),
    (r'^tabs$', 'test_bootstrap.views.test_tabs', {}, "tabs"),
    (r'^widgets$', 'test_bootstrap.views.test_widgets', {}, "widgets"),
)

