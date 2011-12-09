import re

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

    def read(self, request, the_hash):
		try:
			ad = Ad.objects.get(audio_hash=the_hash)
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


