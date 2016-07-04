from __future__ import unicode_literals

from django.db import models


class Sections(models.Model):
    section_header = models.CharField(max_length=100)
    age_qualification = models.IntegerField()


class Articles(models.Model):
    article_header = models.CharField(max_length=100)
    contents = models.CharField(max_length=100)
    author = models.CharField(max_length=100)


class Connections(models.Model):
    article = models.ForeignKey(Articles)
    section = models.ForeignKey(Sections)
