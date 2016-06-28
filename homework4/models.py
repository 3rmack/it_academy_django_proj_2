from __future__ import unicode_literals

from django.db import models


class Cities(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return '{0}'.format(self.name)


class Streets(models.Model):
    city = models.OneToOneField(Cities)
    name = models.CharField(max_length=100)
    length = models.IntegerField(null=True)

    def __unicode__(self):
        return '{0}'.format(self.name)
