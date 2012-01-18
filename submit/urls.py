from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
#from api.handlers import AdHandler

from cuibono_webservice.submit import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url('^ad/$',views.submit_ad),
                       url('^thanks/$', views.thanks),


)
