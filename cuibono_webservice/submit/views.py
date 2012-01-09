from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response

from submit.forms import SubmitAdForm
from cuibono.models import Ad,Article,Tag,Funder

import datetime
import os

def submit_ad(request):
    if request.method == 'POST':
        form = SubmitAdForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_ad(request.FILES['ad_file'],request.POST)
            return HttpResponseRedirect('/thanks/')
        else:
            form = UploadFileForm()
        return render_to_response('submit_ad.html', {'form': form})

def handle_uploaded_ad(f,post):
    base,ext = os.path.splitext(f.name)
    fname = '_'.join([post['ad_title'], datetime.datetime.now()]) + ext
    newfile = '/var/www/cuibono_webservice/media_files/'+fname
    destination = open(newfile, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    ad = Ad(title = post['ad_title'], \
            transcript = post['ad_transcript'], \
            media_file = newfile) # OOPS, doesn't exist yet!
    for t in post['ad_tags'].replace(',',' ').replace('  ',' ').split(' '):
        ad.tags.add(Tag(name=t))
    ad.save()
            
