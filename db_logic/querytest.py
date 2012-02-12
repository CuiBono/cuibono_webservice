from cuibono_webservice.cuibono.models import Ad

for ad in Ad.objects.filter(ingested=False):
    print ad
