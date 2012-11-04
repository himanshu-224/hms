from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from mainapp.views import profile, register, view_complaints_student

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
)
