from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from submit.forms import SubmitAdForm
from cuibono.models import Ad,Article,Tag,Funder
from cuibono.api import fp

import pyechonest.song as song

import datetime
import os

def submit_ad(request):
    errors = []
    if request.method == 'POST':
        form = SubmitAdForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_ad(request.FILES['ad_file'],request.POST)
            return HttpResponseRedirect('/thanks/')
        else:
            errors.append('Form was not valid')
            form = SubmitAdForm()
        return render_to_response('submit_ad.html', 
                                  {'form': form,
                                   'errors':errors},
                                  context_instance=RequestContext(request))
    else:
        form = SubmitAdForm()
    return render_to_response('submit_ad.html',
                              {'errors': errors,
                               'form':form},
                             context_instance=RequestContext(request))

def solr_ingest(newfile,pk):
    fprint = song.util.codegen(open(newfile))
    if len(fp) and "code" in fp[0]:
        data = {"track_id": pk,
                "fp": fprint,
                "length": 0,
                "codever": "4.12"}
        fp.ingest(data)

def handle_uploaded_ad(f,post):
    base,ext = os.path.splitext(f.name)
    fname = '_'.join([post['ad_title'], datetime.datetime.now()]) + ext
    newfile = ''+fname
    destination = open(newfile, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    ad = Ad(title = post['ad_title'], \
            transcript = post['ad_transcript'], \
            media_file_name = newfile) # OOPS, doesn't exist yet!
    for t in post['ad_tags'].replace(',',' ').replace('  ',' ').split(' '):
        ad.tags.add(Tag(name=t))
    ad.audio_hash = solr_ingest(newfile)
    ad.save()
    solr_ingest(newfile,ad.pk)

def thanks(request):
    return render_to_response('thanks.html')
