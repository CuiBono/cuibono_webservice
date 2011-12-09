from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from api.handlers import AdHandler

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cuibono_webservice.views.home', name='home'),
    # url(r'^cuibono_webservice/', include('cuibono_webservice.foo.urls')),
    
    #url(r'^api/ad/(?P<the_hash>[^/]+)/$', ad_resource), -- Where is ad_resource?
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
