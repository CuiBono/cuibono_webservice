from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from submit.forms import SubmitAdForm
from cuibono.models import Ad,Article,Funder#,Tag
from filetransfers.api import prepare_upload

import datetime
import os

#def submit_ad(request):
#    errors = []
#    if request.method == 'POST':
#        form = SubmitAdForm(request.POST, request.FILES)
#        if form.is_valid():
#            handle_uploaded_ad(request.FILES['ad_file'],request.POST)
#            return HttpResponseRedirect('/thanks/')
#        else:
#            for k,v in form.errors.items():
#              errors.append('%s: %s' % (k,v))
#            form = SubmitAdForm()
#        return render_to_response('submit_ad.html', 
#                                  {'form': form,
#                                   'errors':errors},
#                                  context_instance=RequestContext(request))
#    else:
#        form = SubmitAdForm()
#    return render_to_response('submit_ad.html',
#                              {'errors': errors,
#                               'form':form},
#                             context_instance=RequestContext(request))

def solr_ingest(newfile,pk):
    fprint = song.util.codegen(open(newfile))
    if len(fp) and "code" in fp[0]:
        data = {"track_id": pk,
                "fp": fprint,
                "length": 0,
                "codever": "4.12"}
        fp.ingest(data)

#def handle_uploaded_ad(f,post):
#    base,ext = os.path.splitext(f.name)
#    fname = '_'.join([post['ad_title'], datetime.datetime.now()]) + ext
#    newfile = ''+fname
#    destination = open(newfile, 'wb+')
#    for chunk in f.chunks():
#        destination.write(chunk)
#    destination.close()
#    ad = Ad(title = post['ad_title'], \
#            transcript = post['ad_transcript'], \
#            media_file_name = newfile) # OOPS, doesn't exist yet!
#    ad.funders.add(Funder(name=post['ad_funder']))
#    for t in post['ad_tags'].replace(',',' ').replace('  ',' ').split(' '):
#        ad.tags.add(Tag(name=t))
#    for a in post['article_url']:
#        ad.articles.add(Article(title = a,raw_content = a, source = a, pub_date = datetime.now(), url = a))
#    ad.audio_hash = solr_ingest(newfile)
#    ad.save()
#    solr_ingest(newfile,ad.pk)

@login_required
def upload_handler(request):
    view_url = reverse('submit.views.upload_handler')
    if request.method == 'POST':
        form = SubmitAdForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect(view_url)

#        else:
#            for k,v in form.errors.items():
#              errors.append('%s: %s' % (k,v))
#            form = SubmitAdForm()
#        return render_to_response('submit_ad.html', 
    upload_url, upload_data = prepare_upload(request, view_url)
    form = SubmitAdForm()
    return direct_to_template(request, 'submit_ad.html',
                              {'form': form,
                               'upload_url': upload_url,
                               'upload_data': upload_data})

def thanks(request):
    return render_to_response('thanks.html')
