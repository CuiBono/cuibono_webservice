from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
<<<<<<< Updated upstream
#from api.handlers import AdHandler
=======
from api.handlers import AdHandler
from cuibono_webservice.views import *
>>>>>>> Stashed changes

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
<<<<<<< Updated upstream
                       url(r'^api/', include('cuibono_webservice.api.urls')),
                       url(r'^submit/',include('cuibono_webservice.submit.urls')),
                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                      )
=======
    url(r'^api/', include('cuibono_webservice.api.urls')),
    (r'^welcome/', WelcomeView.as_view()),
    (r'^about/', AboutView.as_view()),
    (r'^submit/', SubmitView.as_view()),
    
    
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
>>>>>>> Stashed changes

