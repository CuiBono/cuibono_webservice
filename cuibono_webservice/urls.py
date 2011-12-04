from django.conf.urls import patterns, include, url
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from api.handlers import AdHandler

from django.contrib import admin
admin.autodiscover()
#auth = HttpBasicAuthentication(realm="Cuibono")
#ad_auth = { 'authentication' : auth }

ad_resource = Resource(handler=AdHandler)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cuibono_webservice.views.home', name='home'),
    # url(r'^cuibono_webservice/$', include('cuibono_webservice.api.urls')),
    url(r'^api/ad/(?P<the_hash>[^/]+)/$', ad_resource), 

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
