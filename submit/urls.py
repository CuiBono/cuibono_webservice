from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
#from api.handlers import AdHandler

import submit.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url('^ad/$',submit.views.upload_handler),
                       url('^thanks/$', submit.views.thanks),


)
