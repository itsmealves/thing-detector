# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Detection(models.Model):
    key = models.CharField(max_length=20)
    url = models.CharField(max_length=200)
