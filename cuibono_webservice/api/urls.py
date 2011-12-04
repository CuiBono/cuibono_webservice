from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from cuibono_webservice.api.handlers import AdHandler

auth = HttpBasicAuthentication(realm="Cuibono")
ad_auth = { 'authentication' : auth }

ad_resource = Resource(handler=AdHandler, **ad_auth)

urlpatterns += patterns('',
    url(r'^ad/(?P<audio_hash>[^/]+)/$', ad_resource), 
)
