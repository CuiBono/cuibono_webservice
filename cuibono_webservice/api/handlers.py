import re
import sys
import os
import subprocess
try:
    import json
except ImportError:
    import simplejson as json

from echoprint_server_api import fp
# this should work from anywhere, just make sure that the solr connection pool
# is at localhost:8502/solr/fp and that the tokyo tyrant address is at
# localhost:1978

from piston.handler import BaseHandler
from piston.utils import rc, throttle
from django.core.exceptions import ObjectDoesNotExist

from cuibono.models import Ad

class AdHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'DELETE')
    fields = ('title','transcript',('tags', ('name',)), ('articles', ('title','source','url')))
    exclude = ('id', re.compile(r'^private_'))
    model = Ad

    @classmethod
    def content_size(self, ad):
        return len(ad.content)

    def lookup(self,the_hash):
        #THIS WAS JUST FOR TESTING
        # return the_hash  
        if len(the_hash):
            decoded = fp.decode_code_string(the_hash)
            result = fp.best_match_for_query(decoded)
            if result.TRID:
                return result.TRID
            else:
                return 0
        else:
            return 0

    def read(self, request, the_hash):
        try:
            ad = Ad.objects.get(audio_hash=self.lookup(the_hash))
            out = { \
                      "title"      : ad.title, \
                      "transcript" : ad.transcript, \
                      ## COMMENTING THESE OUT FOR NOW.  APPARENTLY THE
                      ## ManyRelatedManager object is not iterable?  uh?
                      #
                      #"tags"       : [tag.name for tag in ad.tags], \
                      #"articles"   : [a.url for a in ad.articles] \
                      "articles"   : ad.articles
                  }
            return out
        except ObjectDoesNotExist:
            return '<br />'.join(["the lookup didn't work.","codegen hash query was:",str(the_hash)])

    #@throttle(5, 10*60)
    def update(self, request, the_hash):
        ad = Ad.objects.get(audio_hash=the_hash)
        ad.title = request.PUT.get('title')
        ad.save()
        return ad

    def delete(self, request, the_hash):
        ad = Ad.objects.get(audio_hash=the_hash)
        ad.delete()
        return rc.DELETED


