import re
import sys
import os
import subprocess
try:
    import json
except ImportError:
    import simplejson as json
#import fp

from piston.handler import BaseHandler
from piston.utils import rc, throttle
from django.core.exceptions import ObjectDoesNotExist

from cuibono.models import Ad

class AdHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'DELETE')
    fields = ('title','transcript',('tags', ('value','type')), ('articles', ('title','source','url')))
    exclude = ('id', re.compile(r'^private_'))
    model = Ad

    @classmethod
    def content_size(self, ad):
        return len(ad.content)

    def lookup(self,the_hash):
        return the_hash
 #       if len(the_hash):
 #           decoded = fp.decode_code_string(the_hash)
 #           result = fp.best_match_for_query(decoded)
 #           if result.TRID:
 #               return result.TRID
 #           else:
 #               return 0
 #       else:
 #           return 0

    def read(self, request, the_hash):
        try:
            ad = Ad.objects.get(audio_hash=lookup(the_hash))
            return ad
        except ObjectDoesNotExist:
            return None

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


