from __future__ import unicode_literals

from django.db import models


class Workers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_year = models.IntegerField()


class Equipments(models.Model):
    equipment_owner = models.ForeignKey(Workers, null=True, blank=True)
    equipment_name = models.CharField(max_length=100)
    inventory_id = models.IntegerField()
    cost = models.IntegerField()
