from django.db import models
from django import forms

class TagType(models.Model):
    name = models.CharField(max_length=200)

class Tag(models.Model):
    value = models.CharField(max_length=200)
    type = models.ForeignKey(TagType)

class Article(models.Model):
    title = models.CharField(max_length=200)
    raw_content = models.CharField(max_length=10000)
    source = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    url = models.CharField(max_length=500)
    def __unicode__(self):
        return self.title

class Quotation(models.Model):
    article = models.ForeignKey('Article')
    
class Ad(models.Model):
    title = models.CharField(max_length=200)
    transcript = models.CharField(max_length=500, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    audio_hash = models.CharField(max_length=5000)
    articles = models.ManyToManyField(Article, blank=True)
    def __unicode__(self):
        return self.title