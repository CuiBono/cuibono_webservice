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
    fields = ('title','transcript','funder',('tags', ('name',)), ('articles', ('title','source','url')))
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
            ad = Ad.objects.get(pk=self.lookup(the_hash))
            articles = {}
            article_data = [(a.title,a.source,a.url) for a in ad.articles.all()]
            for title,source,url in article_data:
                articles[title] = {"source": source, "url": url}
            top_article = ad.articles.all()[0]
            top_funder = str(ad.funders.all()[0])
            out = { \
                      "title"      : ad.title, \
                      "transcript" : ad.transcript, \
                      "funder" : top_funder \
                      "url" : top_article.url\
                  }
            return out
        except ObjectDoesNotExist:
            return {  "title" : "None Found", \
                      "transcript" : "N/A", \
                      "funder" : "N/A", \
                      "url" : "N/A" \
                   }

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


