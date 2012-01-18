from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from api.handlers import AdHandler

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


ad_resource = Resource(handler=AdHandler)

urlpatterns = patterns('',
    
    url(r'^ad/(?P<the_hash>[^/]+)/$', ad_resource, { 'emitter_format': 'json' }), # Where is ad_resource?
    
)
