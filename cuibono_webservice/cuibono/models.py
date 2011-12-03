from django.db import models

class TagType(models.Model):
    name = models.CharField(max_length=200)

class Tag(models.Model):
    value = models.CharField(max_length=200)
    type = models.ForeignKey(TagType)

class Ad(models.Model):
    title = models.CharField(max_length=200)
    transcript = models.CharField(max_length=1000, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)

