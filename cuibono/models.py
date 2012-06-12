from django.db import models
from django import forms

#class TagType(models.Model):
#class Tag(models.Model):
#    name = models.CharField(max_length=200)
#    def __unicode__(self):
#        return self.name
#       
#    class Admin:
#        pass

#class Tag(models.Model):
#    value = models.CharField(max_length=200)
#    type = models.ForeignKey(TagType)
#    def __unicode__(self):
#        return self.value
#        
#    class Admin:
#        pass

class Article(models.Model):
    title = models.CharField(max_length=200)
    raw_content = models.CharField(max_length=10000)
    source = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    url = models.CharField(max_length=500)
    def __unicode__(self):
        return self.title
        
    class Admin:
        pass

#class Quotation(models.Model):
#    segment = models.CharField(max_length=500)
#    article = models.ForeignKey('Article')
#
#    class Admin:
#        pass

class Funder(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

    class Admin:
        pass

class Ad(models.Model):
    file = models.FileField(upload_to='ad_media/%Y/%m/%d/%H/%M/%S/')
    title = models.CharField(max_length=200)
    transcript = models.TextField(max_length=5000, blank=True)
    # taking this out until we can make it more dynamic
    # tags = models.ManyToManyField(Tag, blank=True)
    tags = models.CharField(max_length=140)
    articles = models.ManyToManyField(Article, blank=True)
    funders = models.ManyToManyField(Funder)
    ingested = models.BooleanField(default=False)
    duplicate = models.BooleanField(default=False)
    def __unicode__(self):
        return self.title
        
    class Admin:
        pass

#class DuplicateOf(models.Model):
#    original_ad = models.ForeignKey(Ad)
#    duplicate_ad = models.ForeignKey(Ad)

# for filetransfers
#class UploadModel(models.Model):
#    file = models.FileField(upload_to='uploads/%Y/%m/%d/%H/%M/%S/')
