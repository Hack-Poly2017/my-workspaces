from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Comments(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=255)