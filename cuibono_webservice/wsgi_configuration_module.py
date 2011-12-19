import os
import sys

sys.path.append('/var/www/')
sys.path.append('/var/www/cuibono_webservice/')

os.environ['PYTHON_EGG_CACHE'] = '/var/www/cuibono_webservice/.python-egg'

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()

