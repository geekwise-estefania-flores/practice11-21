from __future__ import unicode_literals

from django.db import models

class Branch(models.Model):
  
  class Meta:
    verbose_name_plural = "branches"

  bank = models.ForeignKey('auth.User', related_name='bank', null=True,
    on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.bank}'