from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysmsapp.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	# url(r'^$',home),
	url(r'^send_msg_from_user',send_msg_from_user),
    # Examples:
    # url(r'^$', 'MyApp.views.home', name='home'),
    # url(r'^MyApp/', include('MyApp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
