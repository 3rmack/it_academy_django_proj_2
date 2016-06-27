from __future__ import unicode_literals

from django.db import models


class DataFormModel(models.Model):
    name = models.CharField(max_length=50)
    favourite_color = models.CharField(max_length=50)
    email = models.EmailField()
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
