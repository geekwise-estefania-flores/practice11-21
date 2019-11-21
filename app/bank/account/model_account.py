from __future__ import unicode_literals

from django.db import models

class Account(models.Model):
    account_number = models.CharField(max_length = 4)
    